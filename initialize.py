# -*- coding: utf-8 -*-
from modules import *

### Set terminal font
libtcod.console_set_custom_font(FONT, libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

### Init terminal (width, height, title, fullscreen)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, TITLE, False, libtcod.RENDERER_SDL)

### Limit FPS
libtcod.sys_set_fps(LIMIT_FPS)

### Console
con = libtcod.console_new(MAP['WIDTH'], MAP['HEIGHT'])
