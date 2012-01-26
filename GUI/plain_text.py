from modules import *

class PlainText(object):
  """docstring for Menu"""
  def __init__(self, file):
    self.file = file
    self.window = None

  def show(self, position = (None, None, None, None)):
    if not self.window:
      self.window = libtcod.console_new(position[2], position[3])
    libtcod.console_clear(self.window)

    libtcod.console_set_default_foreground(self.window, libtcod.lighter_sepia)

    current_line = 0
    for line in open(self.file,'r'):
      libtcod.console_print(self.window, 1, 1 + current_line, line)
      current_line += 1
    
    libtcod.console_blit(self.window, 0, 0, position[2], position[3], 
        0, position[0], position[1], 1.0, 0.8)
    libtcod.console_flush()

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse, None)

    if key.vk == libtcod.KEY_ESCAPE:
      return True
