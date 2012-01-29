# -*- coding: utf-8 -*-
from modules import *

class Object(object):
  list = []

  """ General model for game instance. """
  def __init__(self, position, params):
    self.x = position[0]
    self.y = position[1]
    self.name = params['NAME']
    self.char = params['CHAR']
    self.color = params['COLOR']
    self.passable = params['PASSABLE']
    self.transparent = params['TRANSPARENT']
    self.weight = params['WEIGHT']

  def draw(self):
    libtcod.console_set_default_foreground(con, self.color)
    libtcod.console_put_char(con, self.x, self.y, self.char)

  def clear(self):
    libtcod.console_put_char(con, self.x, self.y, ' ')

  def distance_to(self, start, goal):
    dx = goal.x - start.x
    dy = goal.y - start.y
    return math.sqrt(dx ** 2 + dy ** 2)

  def set_position(self, position):
    self.x = position[0]
    self.y = position[1]

  @classmethod
  def clear_all(cls):
    for object in cls.list:
      object.clear()

  @classmethod
  def draw_all(cls, fov_map=None):
    if fov_map:
      for object in cls.list:
        if libtcod.map_is_in_fov(fov_map, object.x, object.y):
          object.draw()
    else:
      for object in cls.list:
        object.draw()

  @classmethod
  def get_by_position(cls, x, y):
    objects = []
    for object in cls.list:
      if object.x == x and object.y == y:
        objects.append(object)
    return objects


