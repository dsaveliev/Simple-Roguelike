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
    Text.event_heal(owner.world.panel, owner.name, str(params[0]))
    heal(params, owner)
  elif effect == 'POISON':
    Text.event_poison(owner.world.panel, owner.name, str(params[0]))
    poison(params, owner)
  elif effect == 'LIGHTNING SPHERE':
    lightning_sphere(params, owner)
  elif effect == 'LIGHTNING BOLT':
    lightning_bolt(params, owner)
  elif effect == 'CONFUSION':
    confusion(params, owner)

def heal(params, owner):
  owner.stats['HP'].value += params[0]
  if owner.stats['HP'].value > owner.stats['HP'].base_value:
    owner.stats['HP'].value = owner.stats['HP'].base_value

def poison(params, owner):
  owner.stats['HP'].value -= params[0]
  if owner.stats['HP'].value <= 0:
    owner.death()

def lightning_sphere(params, owner):
  targets = owner.get_surrounding_creatures(params[1])
  for target in targets:
    Text.event_lightning_sphere(owner.world.panel, target.name, str(params[0]))
    target.take_damage(params[0])

def lightning_bolt(params, owner):
  target = owner.get_nearest_creature(params[1])
  if target:
    Text.event_lightning_bolt(owner.world.panel, target.name, str(params[0]))
    target.take_damage(params[0])

def confusion(params, owner):
  target = owner.get_nearest_creature(params[1])
  if target:
    Text.event_confusion(owner.world.panel, target.name, str(params[0]))
    target.confuse(params[0])
  
    
from modules import *
