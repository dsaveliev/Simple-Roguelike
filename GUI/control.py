from modules import *

class Control(object):
  def __init__(self):
    self.game = Game()
    self.key = libtcod.Key()
    self.mouse = libtcod.Mouse()
    self.agent = None

  def handle_input(self):
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, self.key, self.mouse)
    self.handle_mouse()
    if self.game.game_state == 'AIM':
      self.agent = self.game.aim
    elif self.game.game_state == 'PLAYING':
      self.agent = self.game.player
    return self.handle_keyboard()

  ### Mouse ###################################################################
  def handle_mouse(self):
    self.show_objects_under_mouse()

  def get_mouse_position(self):
    (x, y) = (self.mouse.cx - MAP['X'], self.mouse.cy - MAP['Y'])
    return (x, y)

  def show_objects_under_mouse(self):
    (x, y) = self.get_mouse_position()
    self.game.render_names_at_position(x, y)
  #############################################################################

  ### Keyboard ################################################################
  def handle_menu_keys(self):
    if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
      libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif self.key.vk == libtcod.KEY_ESCAPE:
      self.game.game_state = 'EXIT'
    elif self.key.vk == libtcod.KEY_PRINTSCREEN:
      libtcod.sys_save_screenshot('screenshot.png')
      
  def handle_move_keys(self):
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
    if self.key.c == KEY_FIRE:
      self.agent.aim()
    else:
      return None
    return True
  
  def handle_action_keys(self):
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
    state = self.handle_move_keys()
    if self.game.game_state == 'AIM':
      state = state or self.handle_aim_keys()
    elif self.game.game_state == 'PLAYING':
      state = state or self.handle_action_keys()

    if state:
      self.agent.state = 'TAKE_TURN'
    else:
      self.agent.state = 'DIDNT_TAKE_TURN'

    return self.handle_menu_keys()
###############################################################################
