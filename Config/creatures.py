# -*- coding: utf-8 -*-
from modules import *

AIM = {
  'OBJECT':{
    'NAME':'Aim',
    'CHAR':'X',
    'COLOR':libtcod.white,
    'TRANSPARENT':False,
    'PASSABLE':False,
    'WEIGHT':0
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
