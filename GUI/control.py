# -*- coding: utf-8 -*-
from modules import *

class Control(object):
  """
  Класс - обработчик пользовательского ввода.
  """
  def __init__(self, game):
    self.game = game
    self.key = libtcod.Key()
    self.mouse = libtcod.Mouse()
    self.agent = None

  def handle_input(self):
    """
    Обработка пользовательского ввода. 
    В зависимости от состояния игры, объектом управления может быть 
    либо сам игрок @ либо прицел X.
    """
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, 
      self.key, self.mouse)
    if self.game.state == 'AIM':
      self.agent = self.game.aim
    elif self.game.state == 'PLAYING':
      self.agent = self.game.player
    self.handle_mouse()
    return self.handle_keyboard()

  ### Mouse ###################################################################
  def handle_mouse(self):
    """
    Обработка событий мыши.
    """
    self.show_objects_under_mouse()

  def get_mouse_position(self):
    """
    Получение координат курсора.
    """
    (x, y) = (self.mouse.cx - MAP['X'], self.mouse.cy - MAP['Y'])
    return (x, y)

  def show_objects_under_mouse(self):
    """
    Отображение объектов под курсором.
    """
    (x, y) = self.get_mouse_position()
    self.game.render_names_at_position(x, y)
  #############################################################################

  ### Keyboard ################################################################
  def handle_menu_keys(self):
    """
    Обработка клавиш, не связанных с игровым процессом.
    """
    if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
      libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif self.key.vk == libtcod.KEY_ESCAPE:
      self.game.state = 'EXIT'
    elif self.key.vk == libtcod.KEY_PRINTSCREEN:
      libtcod.sys_save_screenshot('./Images/screenshot.png')
      
  def handle_move_keys(self):
    """
    Обработка клавиш, связанных с передвижением.
    """
    if self.key.c == KEY_UP:
      self.agent.move_or_attack(0, -1)
    elif self.key.c == KEY_DOWN:
      self.agent.move_or_attack(0, 1)
    elif self.key.c == KEY_LEFT:
      self.agent.move_or_attack(-1, 0)
    elif self.key.c == KEY_RIGHT:
      self.agent.move_or_attack(1, 0)
    elif self.key.c == KEY_RIGHT_UP:
      self.agent.move_or_attack(1, -1)
    elif self.key.c == KEY_RIGHT_DOWN:
      self.agent.move_or_attack(1, 1)
    elif self.key.c == KEY_LEFT_UP:
      self.agent.move_or_attack(-1 ,-1)
    elif self.key.c == KEY_LEFT_DOWN:
      self.agent.move_or_attack(-1 ,1)
    else:
      return None
    return True

  def handle_aim_keys(self):
    """
    Обработка клавиш, связанных с дистанционной атакой.
    """
    if self.key.c == KEY_FIRE:
      self.agent.aim()
    else:
      return None
    return True
  
  def handle_action_keys(self):
    """
    Обработка клавиш, связанных с игровым процессом.
    """
    if self.key.c == KEY_PICK_UP:
      self.agent.pick_up()
    elif self.key.c == KEY_INVENTORY:
      self.agent.use('GENERAL')
    elif self.key.c == KEY_DROP:
      self.agent.drop()
    else:
      return None
    return True

  def handle_keyboard(self):
    """
    Обработка событий клавиатуры.
    """
    if self.agent.state != 'DEAD':
      state = self.handle_move_keys()
      if self.game.state == 'AIM':
        state = state or self.handle_aim_keys()
      elif self.game.state == 'PLAYING':
        state = state or self.handle_action_keys()
      self.agent.take_turn = state
    else:
      self.agent.take_turn = None

    return self.handle_menu_keys()
###############################################################################
