# -*- coding: utf-8 -*-


from modules import *

### Tiles
TILES = {
  'FLOOR':{
    'OBJECT':{
      'NAME':'Floor',
      'CHAR':'.',
      'COLOR':COLOR_LIGHT_GROUND,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':0
    },
    'SHADED_COLOR':COLOR_DARK_GROUND
  },

  'WALL':{
    'OBJECT':{
      'NAME':'Wall',
      'CHAR':'#',
      'COLOR':COLOR_LIGHT_WALL,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':0
    },
    'SHADED_COLOR':COLOR_DARK_WALL
  }
}
