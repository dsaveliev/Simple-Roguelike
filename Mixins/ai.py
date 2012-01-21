class Ai(object):
  """docstring for Ai"""
  def __init__(self):
    self.behavior = self.base_behavior
    self.deviation_time = 0

  ### HELPERS #################################################################
  def move_towards(self, goal_x, goal_y):
    variants = {}
    class Point:
      pass
    start = Point()
    goal = Point()
    for x in range(-1, 2):
      for y in range(-1, 2):
        goal.x, goal.y = goal_x, goal_y
        start.x, start.y = self.x + x, self.y + y
        variants[(x, y)] = self.distance_to(start, goal)
    variants = sorted(variants.iteritems(), key=operator.itemgetter(1))
    for v in variants:
      obstacle = self.move(v[0][0], v[0][1])
      if not obstacle: break

  def confuse(self, time):
    self.deviation_time = time
    self.behavior = self.confused_behavior

  def check_deviation_time(self):
    self.deviation_time -= 1
    if self.deviation_time <= 0: 
      self.behavior = self.base_behavior
      Text.event_base_behavior(self.game.panel, self.name)
  #############################################################################

  def base_behavior(self):
    if self.distance_to(self, self.game.player) <= self.torch_radius:
      if self.distance_to(self, self.game.player) >= 2:
        self.move_towards(self.game.player.x, self.game.player.y)
      else:
        self.attack(self.game.player)

  def confused_behavior(self):
    self.check_deviation_time()
    self.move(libtcod.random_get_int(0, -1, 1), libtcod.random_get_int(0, -1, 1))

  def take_turn(self):
    self.behavior()

from modules import *
