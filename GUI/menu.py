from modules import *

class Menu(object):
  """docstring for Menu"""
  def __init__(self):
    self.world = World()

  def show(self, header, options):
    if len(options) > 26:
      raise ValueError('Cannot have a menu with more than 26 options.')

    margin = {'top':2, 'right':1, 'bottom':2, 'left':1}
    index_width = 4 # --> '(a) '
    width = len(header)
    height = len(options) + margin['top'] + margin['bottom']
    start_index = ord('a')

    for option in options:
      if len(option) > width:
        width = len(option)
    width += index_width + margin['left'] + margin['right']
    window = libtcod.console_new(width, height)

    libtcod.console_print_frame(window, 0, 0, width, height, True, 0, header)
    libtcod.console_set_default_foreground(window, libtcod.amber)
    letter_index = start_index
    for i in range(len(options)):
      text = '[' + chr(letter_index) + '] ' + options[i]
      libtcod.console_print(window, 1, i + margin['top'], text)
      letter_index += 1

    x = SCREEN_WIDTH / 2 - width / 2
    y = SCREEN_HEIGHT / 2 - height / 2
    libtcod.console_blit(window, 0, 0, width, height, 0, x, y, 1.0, 0.7)
    libtcod.console_flush()

    key = libtcod.Key()
    mouse = libtcod.Mouse()
    libtcod.sys_wait_for_event(libtcod.EVENT_KEY_PRESS, key, mouse, None)

    result = key.c - start_index
    if result in range(0,len(options)): return result
    else: return None
