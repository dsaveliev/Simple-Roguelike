from modules import *

class Item(Object):
  list = []
  """ Description of creature """
  def __init__(self, position, type):
    params = ITEMS[type]
    if position:
      super(Item, self).__init__(position, params['OBJECT'])
      Item.list.append(self)
    else:
      super(Item, self).__init__((0, 0), params['OBJECT'])
    self.prevalence = params['PREVALENCE']
    self.actions = params['ACTIONS']
    self.effects = params['EFFECTS']
    self.effects_use = params['EFFECTS USE']
    self.durability = params['DURABILITY']

  def draw(self):
    visible = libtcod.map_is_in_fov(self.game.map.fov_map, self.x, self.y)
    if visible:
      super(Item, self).draw()

  @staticmethod
  def get_random_type():
    item = ''
    max_prevalence = 0
    for i in ITEMS:
      if ITEMS[i]['PREVALENCE'] > 1:
        prevalence = libtcod.random_get_int(0, 1, ITEMS[i]['PREVALENCE'])
        if prevalence > max_prevalence:
          max_prevalence = prevalence
          item = i
    return item
