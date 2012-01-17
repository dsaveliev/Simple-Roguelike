import libtcodpy as libtcod
import os

### Stuff
LIMIT_FPS     = 20
FONT          = 'Fonts/arial12x12.png'
TITLE         = 'Tombs of the Ancient Kings'

### Set terminal size
SCREEN_WIDTH  = 80
SCREEN_HEIGHT = 55

### Set menu size
PANEL = {
  'HEIGHT':9,
  'WIDTH':SCREEN_WIDTH,
  'X':0,
  'Y':0
}

### Bar size
BAR = {
  'HEIGHT':1,
  'WIDTH':11,
  'X':1,
  'Y':1,
  'INDENT':2
}

### Set map size
MAP = {
  'HEIGHT':SCREEN_HEIGHT - PANEL['HEIGHT'],
  'WIDTH':SCREEN_WIDTH,
  'X':0,
  'Y':PANEL['HEIGHT']
}

### Message log
MSG = {
  'HEIGHT':PANEL['HEIGHT'] - 3,
  'WIDTH':PANEL['WIDTH'] - BAR['WIDTH'] - 3,
  'X':BAR['WIDTH'] + 2,
  'Y':0
}

### Set movement keys
KEY_LEFT        = ord('h')
KEY_RIGHT       = ord('l')
KEY_DOWN        = ord('j')
KEY_UP          = ord('k')
KEY_LEFT_UP     = ord('y')
KEY_RIGHT_UP    = ord('u')
KEY_LEFT_DOWN   = ord('b')
KEY_RIGHT_DOWN  = ord('n')
KEY_PICK_UP     = ord('g')
KEY_INVENTORY   = ord('i')
KEY_USE         = ord('a')
KEY_DROP        = ord('d')

### Rooms params
ROOM_MAX_SIZE = 10
ROOM_MIN_SIZE = 6
MAX_ROOMS     = 30
MAX_ROOM_CREATURES = 3
MAX_ROOM_ITEMS = 1
MAX_CREATURE_ITEMS = 1
INVETORY_LIMIT = 26
BLOODY_BATTLES = 50 # from 0 to 100%

### FOV
FOV_ALGO = 0  #default FOV algorithm
FOV_LIGHT_WALLS = True

### Colors
COLOR_DARK_WALL     = libtcod.darker_sepia
COLOR_DARK_GROUND   = libtcod.darker_orange
COLOR_LIGHT_WALL    = libtcod.light_sepia
COLOR_LIGHT_GROUND  = libtcod.light_orange
COLOR_BACKGROUND    = libtcod.black
COLOR_FOREGROUND    = libtcod.white
COLOR_BLOOD         = libtcod.dark_red

### Game states
GAME_STATES = [
  'PLAYING',
  'EXIT',
  'DEAD',
  'MENU'
]
### Stats
STATS = {
  'HP':{
    'NAME':'Health',
    'UPDATABLE':True,
    'RESTORABLE':True
  },
  'XP':{
    'NAME':'Expirience',
    'UPDATABLE':None,
    'RESTORABLE':None
  },
  'MP':{
    'NAME':'Mana',
    'UPDATABLE':True,
    'RESTORABLE':True
  },
  'SP':{
    'NAME':'Strength',
    'UPDATABLE':True,
    'RESTORABLE':None
  },
  'DP':{
    'NAME':'Defence',
    'UPDATABLE':True,
    'RESTORABLE':None
  },
  'AP':{
    'NAME':'Attack',
    'UPDATABLE':True,
    'RESTORABLE':None
  }
}

### Creatures
CREATURES = {
  'PLAYER':{
    'OBJECT':{
      'NAME':'Drunken Elk',
      'CHAR':'@',
      'COLOR':libtcod.white,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':15
    },
    'STATS':{
      'HP':20,
      'XP':0,
      'MP':0,
      'SP':15,
      'DP':3,
      'AP':5
    },
    'TORCH_RADIUS':10,
    'PREVALENCE':0,
    'POLICY':'POLICYFUL'
  },

  'DRAGON':{
    'OBJECT':{
      'NAME':'Red Dragon',
      'CHAR':'D',
      'COLOR':libtcod.red,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':25
    },
    'STATS':{
      'HP':25,
      'XP':0,
      'MP':0,
      'SP':25,
      'DP':3,
      'AP':6
    },
    'TORCH_RADIUS':10,
    'PREVALENCE':20,
    'POLICY':'CHAOTIC'
  },

  'TROLL':{
    'OBJECT':{
      'NAME':'Troll',
      'CHAR':'T',
      'COLOR':libtcod.darker_green,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':16
    },
    'STATS':{
      'HP':16,
      'XP':0,
      'MP':0,
      'SP':16,
      'DP':2,
      'AP':5
    },
    'TORCH_RADIUS':5,
    'PREVALENCE':25,
    'POLICY':'CHAOTIC'
  },

  'ORC':{
    'OBJECT':{
      'NAME':'Orc',
      'CHAR':'o',
      'COLOR':libtcod.desaturated_green,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':10
    },
    'STATS':{
      'HP':10,
      'XP':0,
      'MP':0,
      'SP':10,
      'DP':1,
      'AP':4
    },
    'TORCH_RADIUS':10,
    'PREVALENCE':40,
    'POLICY':'CHAOTIC'
  },

  'GOBLIN':{
    'OBJECT':{
      'NAME':'Goblin',
      'CHAR':'g',
      'COLOR':libtcod.light_green,
      'TRANSPARENT':False,
      'PASSABLE':False,
      'WEIGHT':8
    },
    'STATS':{
      'HP':8,
      'XP':0,
      'MP':0,
      'SP':8,
      'DP':0,
      'AP':4
    },
    'TORCH_RADIUS':12,
    'PREVALENCE':60,
    'POLICY':'CHAOTIC'
  }
}

### Items
ACTIONS = [
  'GENERAL', # First possible
  'EAT',
  'QUAFF',
  'READ',
  'CAST',
  'EQUIP',
  'THROW'
]

EFFECTS = [
  'HEAL', # hit points
  'POISON', # hit points
  'LEARN', # ...
  'LIGHTNING BOLT', # range, hit points
  'LIGHTNING SPHERE', # range, hit points
  'CONFUSION' # turns, hit points
]

DURABILITY = [
  'DISPOSABLE',
  'REUSABLE'
]


ITEMS = {
  'CORPSE':{
    'OBJECT':{
      'NAME':'Corpse',
      'CHAR':'%',
      'COLOR':libtcod.light_red,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'RANDOM',
    'EFFECTS':{
      'HEAL':[3],
      'POISON':[3]
    },
    'ACTIONS':[
      'EAT'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':0
  },

  'HEALING POTION':{
    'OBJECT':{
      'NAME':'Healing potion',
      'CHAR':'!',
      'COLOR':libtcod.light_violet,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'ALL',
    'EFFECTS':{
      'HEAL':[5] # hit points
    },
    'ACTIONS':[
      'QUAFF',
      'THROW'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':60
  },

  'SCROLL OF LIGHTNING SPHERE':{
    'OBJECT':{
      'NAME':'Scroll of lightning sphere',
      'CHAR':'#',
      'COLOR':libtcod.light_yellow,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'ALL',
    'EFFECTS':{
      'LIGHTNING SPHERE':[15, 1] # hit points, range
    },
    'ACTIONS':[
      'READ'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':10
  },

  'SCROLL OF LIGHTNING BOLT':{
    'OBJECT':{
      'NAME':'Scroll of lightning bolt',
      'CHAR':'#',
      'COLOR':libtcod.dark_yellow,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'ALL',
    'EFFECTS':{
      'LIGHTNING BOLT':[15, 4] # hit points, range
    },
    'ACTIONS':[
      'READ'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':30
  },

  'SCROLL OF CONFUSION':{
    'OBJECT':{
      'NAME':'Scroll of confusion',
      'CHAR':'#',
      'COLOR':libtcod.light_cyan,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'ALL',
    'EFFECTS':{
      'CONFUSION':[15, 5] # time, range
    },
    'ACTIONS':[
      'READ'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':40
  }

}

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
