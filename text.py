from initialize import *

### TEXT
def corpse_name(name):
  return 'Corpse of ' + name

def inventory_use():
  return 'Use item'

def inventory_drop():
  return 'Drop item'

def inventory_pick_up():
  return 'Pick up item'

def inventory_empty():
  return 'Inventory empty'

### EVENTS
def event_death(panel, name):
  if name != '':
    panel.message(name + ' is dead!', libtcod.dark_red)

def event_successful_attack(panel, fighter, target, damage):
  if fighter != '' and target != '' and damage != '':
    panel.message(fighter + ' attacks ' + target + ' for ' + damage + ' hit points.', libtcod.lighter_grey)

def event_unsuccessful_attack(panel, fighter, target):
  if fighter != '' and target != '':
    panel.message(fighter + ' attacks ' + target + ' but it has no effect!', libtcod.lighter_grey)

def event_welcome(panel, name):
  if name != '':
    panel.message('Welcome ' + name + '! Prepare to perish in the Tombs of the Ancient Kings.', libtcod.dark_yellow)

def event_observation(panel, item):
  if item != '':
    panel.message('You see ' + item, libtcod.dark_green)

def event_overload(panel):
  panel.message('You are overloaded!', libtcod.dark_orange)

def event_pick_up_item(panel, item):
  if item != '':
    panel.message('You picked up a ' + item, libtcod.light_green)

def event_nothing_to_pick_up(panel):
  panel.message('You don\'t see anything that could be picked up', libtcod.dark_orange)

def event_inventory_full(panel, name):
  if name != '':
    panel.message('Your inventory is full, cannot pick up ' + name + '.', libtcod.dark_orange)

### ACTIONS ###################################################################
def event_quaff(panel, owner, name):
  if name != '' and owner != '':
    panel.message(owner + ' quaff ' + name + '.', libtcod.light_green)

def event_eat(panel, owner, name):
  if name != '' and owner != '':
    panel.message(owner + ' eat ' + name + '.', libtcod.light_green)

def event_read(panel, owner, name):
  if name != '' and owner != '':
    panel.message(owner + ' read ' + name + '.', libtcod.light_green)

def event_drop(panel, owner, name):
  if name != '' and owner != '':
    panel.message(owner + ' drop ' + name + '.', libtcod.light_flame)
###############################################################################


### EFFECTS ###################################################################
def event_heal(panel, owner, value):
  if value != '' and owner != '':
    panel.message(owner + ' is healed for ' + value + ' HP', libtcod.white)

def event_poison(panel, owner, value):
  if value != '' and owner != '':
    panel.message(owner + ' is poisoned for ' + value + ' HP', libtcod.yellow)

def event_lightning_sphere(panel, target, value):
  if value != '' and target != '':
    panel.message('Lightning sphere strikes ' + target + ' for ' + value + ' HP', libtcod.light_yellow)

def event_lightning_bolt(panel, target, value):
  if value != '' and target != '':
    panel.message('Lightning bolt strikes ' + target + ' for ' + value + ' HP', libtcod.dark_yellow)

def event_confusion(panel, target, value):
  if value != '' and target != '':
    panel.message('The eyes of the ' + target + ' look vacant, as he starts to stumble around!', libtcod.light_cyan)

def event_base_behavior(panel, target):
  if target != '':
    panel.message(target + ' again begins the hunt for you!', libtcod.light_red)
###############################################################################
