from modules import *

class Player(Creature):
  """ Description of player """
  def __init__(self, position = (0, 0)):
    super(Player, self).__init__(position, 'PLAYER')
    self.state = 'DIDNT_TAKE_TURN'
    self.is_fov_recompute = True

  ### ACTIONS #################################################################
  def move_or_attack(self, dx, dy):
    if self.world.game_state == 'PLAYING':
      object = self.move(dx, dy)
      if not object:
        self.is_fov_recompute = True
        self.show_objects_under_player()
      elif isinstance(object, Creature):
        self.attack(object)

  def pick_up(self):
    items = Item.get_by_position(self.x, self.y)
    if len(items) == 0:
      if self == self.world.player: Text.event_nothing_to_pick_up(self.world.panel)
      return None

    index = 0
    if len(items) > 1:
      index = self.world.menu.show(Text.inventory_pick_up(), 
        [item.name for item in items])
    if index != None:
      item = items[index]
      if len(self.inventory) >= INVETORY_LIMIT:
        if self == self.world.player: Text.event_inventory_full(self.world.player, item.name)
        return
      elif self.inventory_weight() + item.weight <= self.stats['SP'].base_value:
        Item.list.remove(item)
        self.inventory.append(item)
        self.stats['SP'].value = self.inventory_weight()
        if self == self.world.player: Text.event_pick_up_item(self.world.panel, item.name)
      else:
        if self == self.world.player: Text.event_overload(self.world.panel)
        return None

  def use(self, action = 'GENERAL'):
    item = self.get_item_from_inventory(Text.inventory_use(), action)
    if item:
      Action.apply(item, self, action)
      self.stats['SP'].value = self.inventory_weight()

  def death(self):
    your_corpse = Item((self.x, self.y), 'CORPSE')
    your_corpse.name = Text.corpse_name(self.name)
    #Why? I don't know, lol
    your_corpse.weight = self.weight
    Creature.list.remove(self)
    self.world.game_state = 'DEAD'
    self.drop_all()
    Text.event_death(self.world.panel, self.name)
    del self

  def drop(self, item=None):
    if not item:
      item = self.get_item_from_inventory(Text.inventory_drop())
    if item:
      self.inventory.remove(item)
      item.x, item.y = self.x, self.y
      Item.list.append(item)
      Text.event_drop(self.world.panel, self.name, item.name)

  def action_on_target(self, effect, params):
    self.world.aim.activate(effect, params)

  def action_on_area(self, effect, params):
    targets = self.get_surrounding_creatures(params[1])
    for target in targets:
      effect(params, target)
  
  def action_on_nearest_target(self, effect, params):
    target = self.get_nearest_creature(params[1])
    effect(params, target)
  
  def action_on_himself(self, effect, params):
    effect(params, self)
  #############################################################################

  def get_item_from_inventory(self, header, action = 'GENERAL'):
    inventory_hash = {}
    filtered = self.inventory[:]
    options = []

    if len(self.inventory) == 0:
      self.world.menu.show(header, [Text.inventory_empty()])
      return None
    else:
      if action != 'GENERAL':
        filtered =  [item for item in self.inventory if action in item.actions][:]
      for item in filtered:
        if item.name in inventory_hash.keys():
          inventory_hash[item.name] += 1
        else: inventory_hash[item.name] = 1

      for item in inventory_hash:
        if inventory_hash[item] > 1:
          options.append(item + ' x' + str(inventory_hash[item]))
        else: options.append(item)

      index = self.world.menu.show(header, options)
      if index != None:
        name = inventory_hash.keys()[index]
        for item in self.inventory:
          if item.name == name: return item
      else: return None

  def show_objects_under_player(self):
    names = self.world.get_names_at_position(self.x, self.y, False)
    Text.event_observation(self.world.panel, names)


