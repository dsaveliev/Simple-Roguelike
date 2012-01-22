### self - Item, owner - Creation
def apply_all(item, owner):
  if item.effects_use == 'ALL':
    for effect in item.effects:
      params = item.effects[effect]
      apply(effect, params, owner)
  elif item.effects_use == 'RANDOM':
    index = libtcod.random_get_int(0, 0, len(item.effects) - 1)
    effect = item.effects.keys()[index]
    params = item.effects[effect]
    apply(effect, params, owner)

def apply(effect, params, owner):
  if effect == 'HEAL':
    owner.action_on_himself(heal, params)
  elif effect == 'POISON':
    owner.action_on_himself(poison, params)
  elif effect == 'LIGHTNING SPHERE':
    owner.action_on_area(lightning_bolt, params)
  elif effect == 'LIGHTNING BOLT':
    owner.action_on_nearest_target(lightning_bolt, params)
  elif effect == 'CONFUSION':
    owner.action_on_target(confusion, params)
  elif effect == 'FIREBALL':
    owner.action_on_target(fireball, params)

def heal(params, target):
  Text.event_heal(target.name, str(params[0]))
  target.stats['HP'].value += params[0]
  if target.stats['HP'].value > target.stats['HP'].base_value:
    target.stats['HP'].value = target.stats['HP'].base_value

def poison(params, target):
  Text.event_poison(target.name, str(params[0]))
  target.stats['HP'].value -= params[0]
  if target.stats['HP'].value <= 0:
    target.death()

def lightning_bolt(params, target):
  Text.event_lightning_bolt(target.name, str(params[0]))
  target.take_damage(params[0])

def confusion(params, target):
  Text.event_confusion(target.name, str(params[0]))
  target.confuse(params[0])
  
def fireball(params, target):
  Text.event_fireball(target.name, str(params[0]))
  target.take_damage(params[0])
    
from modules import *
