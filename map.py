# -*- coding: utf-8 -*-
from modules import *

class Rect(object):
  def __init__(self, x, y, w, h):
    self.x1 = x
    self.y1 = y
    self.x2 = x + w
    self.y2 = y + h
  
  def center(self):
    center_x = (self.x1 + self.x2) / 2
    center_y = (self.y1 + self.y2) / 2
    return (center_x, center_y)

  def intersect(self, other):
    return (self.x1 <= other.x2 and self.x2 >= other.x1 and
      self.y1 <= other.y2 and self.y2 >= other.y1)

class Map(object):
  """ Description for map """
  def __init__(self, game, map = [[]]):
    self.game = game
    self.map = map
    self.start = [0, 0]
    self.fov_map = libtcod.map_new(MAP['WIDTH'], MAP['HEIGHT'])
    self.rooms = []

  def generate(self):
    self.map = [[ Tile((x, y), 'WALL')
      for y in range(MAP['HEIGHT']) ]
        for x in range(MAP['WIDTH']) ]
    self.simple_algorithm()
    self.prepare_fov()

  def recompute_fov(self):
    if self.game.player.is_fov_recompute:
      self.game.player.is_fov_recompute = False
      libtcod.map_compute_fov(self.fov_map, 
          self.game.player.x, 
          self.game.player.y, 
          self.game.player.torch_radius, 
          FOV_LIGHT_WALLS, 
          FOV_ALGO)
      for y in range(MAP['HEIGHT']):
        for x in range(MAP['WIDTH']):
          visible = libtcod.map_is_in_fov(self.fov_map, x, y)
          tile = self.map[x][y]
          if not visible:
            tile.set_out_fov()
          else:
            tile.set_in_fov()
            tile.explored = True

  def prepare_fov(self):
    self.fov_map = libtcod.map_new(MAP['WIDTH'], MAP['HEIGHT'])
    for raw in self.map:
      for tile in raw:
        libtcod.map_set_properties(self.fov_map, tile.x, tile.y, tile.transparent, tile.passable)

  def draw(self):
    for raw in self.map:
      for tile in raw:
        if tile.explored: tile.draw()
    self.recompute_fov()

  def get_tile(self, x, y):
    return self.map[x][y]

  def tile_blocked(self, x, y):
    if not self.get_tile(x, y).passable:
      return True
    objects = Creature.get_by_position(x, y)
    for object in objects:
      if object and not object.passable:
        return object

  def get_names_at_position(self, x, y, player = None):
    names = []
    if libtcod.map_is_in_fov(self.fov_map, x, y):
      objects = Creature.get_by_position(x, y)
      objects.extend(Item.get_by_position(x, y))
      if player and player in objects:
        objects.remove(player)
      for obj in objects:
        names.append(obj.name)
    return ', '.join(names)

  def create_room(self, room):
    for x in range(room.x1 + 1, room.x2):
      for y in range(room.y1 + 1, room.y2):
        self.map[x][y] = Tile((x, y), 'FLOOR')
  
  def create_h_tunnel(self, x1, x2, y):
    for x in range(min(x1, x2), max(x1, x2) + 1):
      self.map[x][y] = Tile((x, y), 'FLOOR')

  def create_v_tunnel(self, y1, y2, x):
    for y in range(min(y1, y2), max(y1, y2) + 1):
      self.map[x][y] = Tile((x, y), 'FLOOR')

  def simple_algorithm(self):
    num_rooms = 0
    for r in range(MAX_ROOMS):
      w = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
      h = libtcod.random_get_int(0, ROOM_MIN_SIZE, ROOM_MAX_SIZE)
      x = libtcod.random_get_int(0, 0, MAP['WIDTH'] - w - 1)
      y = libtcod.random_get_int(0, 0, MAP['HEIGHT'] - h - 1)
      new_room = Rect(x, y, w, h)
      failed = False
      for other_room in self.rooms:
        if new_room.intersect(other_room):
          failed = True
          break
      if not failed:
        self.create_room(new_room)
        (new_x, new_y) = new_room.center()
        if num_rooms == 0:
          self.start[0] = new_x
          self.start[1] = new_y
        else:
          (prev_x, prev_y) = self.rooms[num_rooms - 1].center()
          if libtcod.random_get_int(0, 0, 1) == 1:
              self.create_h_tunnel(prev_x, new_x, prev_y)
              self.create_v_tunnel(prev_y, new_y, new_x)
          else:
              self.create_v_tunnel(prev_y, new_y, prev_x)
              self.create_h_tunnel(prev_x, new_x, new_y)
        self.rooms.append(new_room)
        num_rooms += 1
