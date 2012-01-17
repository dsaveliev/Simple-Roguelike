from world import *

class Control(object):
  def __init__(self):
    self.world = World()
    self.key = libtcod.Key()
    self.mouse = libtcod.Mouse()

  def handle_input(self):
    libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, self.key, self.mouse)
    self.handle_mouse_for_map()
    self.handle_game_keys()
    return self.handle_menu_keys()

  def handle_mouse_for_map(self):
    (x, y) = (self.mouse.cx - MAP['X'], self.mouse.cy - MAP['Y'])
    self.world.render_names_at_position(x, y)

  def handle_menu_keys(self):
    if self.key.vk == libtcod.KEY_ENTER and self.key.lalt:
      libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
    elif self.key.vk == libtcod.KEY_ESCAPE:
      self.world.game_state = 'EXIT'
    elif self.key.vk == libtcod.KEY_PRINTSCREEN:
      libtcod.sys_save_screenshot('screenshot.png')

  def handle_game_keys(self):
    if self.world.game_state == 'PLAYING':
      self.world.player.state = 'TAKE_TURN'
      if self.key.c == KEY_UP:
        self.world.player.move_or_attack(0, -1)
      elif self.key.c == KEY_DOWN:
        self.world.player.move_or_attack(0, 1)
      elif self.key.c == KEY_LEFT:
        self.world.player.move_or_attack(-1, 0)
      elif self.key.c == KEY_RIGHT:
        self.world.player.move_or_attack(1, 0)
      elif self.key.c == KEY_RIGHT_UP:
        self.world.player.move_or_attack(1, -1)
      elif self.key.c == KEY_RIGHT_DOWN:
        self.world.player.move_or_attack(1, 1)
      elif self.key.c == KEY_LEFT_UP:
        self.world.player.move_or_attack(-1 ,-1)
      elif self.key.c == KEY_LEFT_DOWN:
        self.world.player.move_or_attack(-1 ,1)
      elif self.key.c == KEY_PICK_UP:
        self.world.player.pick_up()
      elif self.key.c == KEY_INVENTORY:
        self.world.player.use('GENERAL')
      elif self.key.c == KEY_DROP:
        self.world.player.drop()
      else:
        self.world.player.state = 'DIDNT_TAKE_TURN'


