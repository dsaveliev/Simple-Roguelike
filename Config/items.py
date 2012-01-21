from modules import *

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
  'CONFUSION', # turns, hit points
  'FIREBALL' # range, hit points
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
    'PREVALENCE':1000
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
    'PREVALENCE':700
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
    'PREVALENCE':800
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
    'PREVALENCE':750
  },
  
  'SCROLL OF FIREBALL':{
    'OBJECT':{
      'NAME':'Scroll of fireball',
      'CHAR':'#',
      'COLOR':libtcod.flame,
      'TRANSPARENT':True,
      'PASSABLE':True,
      'WEIGHT':1
    },
    'EFFECTS USE':'ALL',
    'EFFECTS':{
      'FIREBALL':[15, 5] # hit points, range
    },
    'ACTIONS':[
      'READ'
    ],
    'DURABILITY':'DISPOSABLE',
    'PREVALENCE':700
  }

}
