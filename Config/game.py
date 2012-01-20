from modules import *

### Stuff
LIMIT_FPS     = 20
FONT          = './Fonts/arial12x12.png'
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
  'MENU',
  'AIM'
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


