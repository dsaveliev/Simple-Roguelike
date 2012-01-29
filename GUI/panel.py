# -*- coding: utf-8 -*-
from modules import *

class Panel(object):
  """docstring for Panel"""
  def __init__(self, game):
    self.panel = libtcod.console_new(PANEL['WIDTH'], PANEL['HEIGHT'])
    self.game = game
    self.messages = []
    self.info_string = ''
    libtcod.console_set_background_flag(self.panel, libtcod.BKGND_SET)
    Text.panel = self

  def message(self, msg, color = libtcod.lighter_grey):
    multiline_msg = textwrap.wrap(msg, MSG['WIDTH'])
    for line in multiline_msg:
      if len(self.messages) == MSG['HEIGHT']:
          del self.messages[0]
      self.messages.append((line, color))

  def info(self, text):
    if len(text) > PANEL['WIDTH'] - 2:
      self.info_string = text[0:PANEL['WIDTH'] - 5] + '...'
    else:
      self.info_string = text
  
  def render_bar(self, x, y, text):
    if y % 2 == 0:
      libtcod.console_set_default_background(self.panel, libtcod.darker_sepia)
    else:
      libtcod.console_set_default_background(self.panel, libtcod.darkest_sepia)
    libtcod.console_rect(self.panel, x, y, BAR['WIDTH'], BAR['HEIGHT'], False)
    libtcod.console_set_default_foreground(self.panel, libtcod.lightest_sepia)
    libtcod.console_print(self.panel, BAR['INDENT'], y, text)

  def render_messages(self):
    libtcod.console_set_default_background(self.panel, COLOR_BACKGROUND)
    for i in range(len(self.messages)):
      libtcod.console_set_default_foreground(self.panel, self.messages[i][1])
      libtcod.console_print(self.panel, MSG['X'], i + 1, self.messages[i][0])

  def render_info(self):
    libtcod.console_set_default_foreground(self.panel, libtcod.lighter_gray)
    libtcod.console_print(self.panel, 1, PANEL['HEIGHT'] - 2, self.info_string)

  def render_separator(self):
    libtcod.console_set_default_foreground(self.panel, libtcod.gray)
    libtcod.console_hline(self.panel, PANEL['X'], PANEL['HEIGHT'] - 1, PANEL['WIDTH'])

  def draw(self):
    libtcod.console_set_default_background(self.panel, COLOR_BACKGROUND)
    libtcod.console_clear(self.panel)

    self.render_bar(1, 1, self.game.player.stat_show('HP', True))
    self.render_bar(1, 2, self.game.player.stat_show('MP', True))
    self.render_bar(1, 3, self.game.player.stat_show('XP', True))
    self.render_bar(1, 4, self.game.player.stat_show('SP', True))
    self.render_bar(1, 5, self.game.player.stat_show('AP'))
    self.render_bar(1, 6, self.game.player.stat_show('DP'))
    self.render_messages()
    self.render_info()
    self.render_separator()

    libtcod.console_blit(self.panel, PANEL['X'], PANEL['Y'], 
        PANEL['WIDTH'], PANEL['HEIGHT'], 0, 0, 0)

