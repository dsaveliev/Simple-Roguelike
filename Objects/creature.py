from modules import *

class Creature(Object, Stats, Fight, Ai):
  list = []
  """ Description of creature """
  def __init__(self, position, type):
    params = CREATURES[type]

    Object.__init__(self, position, params['OBJECT'])
    Stats.__init__(self, params['STATS'])
    Ai.__init__(self)

    self.torch_radius = params['TORCH_RADIUS']
    self.policy = params['POLICY']
    self.prevalence = params['PREVALENCE']
    self.inventory = []
    self.stats['SP'].value = 0

    Creature.list.append(self)

  ### ACTIONS #################################################################
  def move(self, dx, dy):
    obstacle = self.world.tile_blocked(self.x + dx, self.y + dy)
    if not obstacle:
      self.x += dx
      self.y += dy
    else:
      return obstacle

  def drop(self, item):
    if isinstance(item, Item):
      self.inventory.remove(item)
      item.x, item.y = self.x, self.y
      Item.list.append(item)
      Text.event_drop(self.world.panel, self.name, item.name)

  def drop_all(self):
    while len(self.inventory) > 0:
      self.drop(self.inventory[0])

  def death(self):
    corpse = Item((self.x, self.y), 'CORPSE')
    corpse.name = Text.corpse_name(self.name)
    corpse.weight = self.weight
    Creature.list.remove(self)
    self.drop_all()
    Text.event_death(self.world.panel, self.name)
  #############################################################################

  def draw(self):
    visible = libtcod.map_is_in_fov(self.world.map.fov_map, self.x, self.y)
    if visible:
      super(Creature, self).draw()

  def inventory_weight(self):
    total_weight = 0
    for item in self.inventory:
      total_weight += item.weight
    return total_weight

  def get_surrounding_creatures(self, range_value):
    surroundings = []
    for x in range(-range_value, range_value + 1):
      for y in range(-range_value, range_value + 1):
        target_x, target_y = self.x + x, self.y + y
        creatures = Creature.get_by_position(target_x, target_y)
        for creature in creatures:
          if creature != None and creature != self:
            surroundings.append(creature)
    return surroundings

  def get_nearest_creature(self, range_value):
    nearest_creature = None
    min_distance = range_value
    surrounding = self.get_surrounding_creatures(range_value)
    for creature in surrounding:
      distance = self.distance_to(self, creature)
      if distance <= min_distance:
        min_distance = distance
        nearest_creature = creature
    return nearest_creature

  @staticmethod
  def get_random_type(policy):
    creature = ''
    max_prevalence = 0
    for c in CREATURES:
      if CREATURES[c]['POLICY'] == policy and CREATURES[c]['PREVALENCE'] > 0:
        prevalence = libtcod.random_get_int(0, 1, CREATURES[c]['PREVALENCE'])
        if prevalence > max_prevalence:
          max_prevalence = prevalence
          creature = c
    return creature
