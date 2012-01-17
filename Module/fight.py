from world import *

class Fight(object):
  """docstring for Fighter"""
  def __init__(self):
    pass

  def take_damage(self, damage):
    if self.stats['HP'].value > 0:
      self.stats['HP'].value -= damage
      if self.stats['HP'].value <= 0:
        self.death()
      self.spread_blood()

  def spread_blood(self):
    probability = libtcod.random_get_int(0, 0, 100)
    if probability < BLOODY_BATTLES:
      x = libtcod.random_get_int(0, -1, 1) + self.x
      y = libtcod.random_get_int(0, -1, 1) + self.y
      tile = self.world.map.get_tile(x, y)
      tile.set_in_fov_color(COLOR_BLOOD)

  def attack(self, target):
    damage = self.stats['AP'].value - target.stats['DP'].value
    if damage > 0:
      Text.event_successful_attack(self.world.panel, self.name, target.name, str(damage))
      target.take_damage(damage)
    else:
      Text.event_unsuccessful_attack(self.world.panel, self.name, target.name)

