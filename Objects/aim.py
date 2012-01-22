from modules import *

class Aim(Object):
  """ Description of Aim """
  def __init__(self, game):
    params = AIM
    super(Aim, self).__init__((0, 0), params['OBJECT'])
    self.owner = None
    self.effect = None
    self.params = None
    self.game = game

  def activate(self, owner, effect, params):
    self.owner = owner
    self.game.state = 'AIM'
    self.set_position((self.owner.x, self.owner.y))
    Object.list.append(self)
    self.effect = effect
    self.params = params

  def move_or_attack(self, dx, dy):
    x = self.x + dx
    y = self.y + dy
    if x >= 0 and y >= 0 and x < MAP['WIDTH'] and y < MAP['HEIGHT']:
      self.x = x
      self.y = y
      names = self.game.map.get_names_at_position(self.x, self.y)
      Text.event_observation(names)

  def aim(self):
    self.owner.game.state = 'PLAYING'
    Object.list.remove(self)
    targets = Creature.get_by_position(self.x, self.y)
    for target in targets:
      if libtcod.map_is_in_fov(self.game.map.fov_map, target.x, target.y):
        self.effect(self.params, target)
