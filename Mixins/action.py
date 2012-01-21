### self - Item, target - Creation
def apply(item, owner, action, supply=[]):
  if action == 'GENERAL':
    action = item.actions[0]

  if action == 'QUAFF':
    Text.event_quaff(item.game.panel, owner.name, item.name)
    quaff(item, owner)
  elif action == 'EAT':
    Text.event_eat(item.game.panel, owner.name, item.name)
    eat(item, owner)
  elif action == 'READ':
    Text.event_read(item.game.panel, owner.name, item.name)
    read(item, owner)
  elif action == 'THROW':
    throw(item, owner)
  elif action == 'EQUIP':
    equip(item, owner)

  if item.durability == 'DISPOSABLE':
    owner.inventory.remove(item)
    del item

def quaff(item, owner):
  Effect.apply_all(item, owner)

def eat(item, owner):
  Effect.apply_all(item, owner)

def read(item, owner):
  Effect.apply_all(item, owner)

def throw(item, owner):
  pass

def equip(item, owner):
  pass


from modules import *
