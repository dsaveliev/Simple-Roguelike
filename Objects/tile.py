# -*- coding: utf-8 -*-
from modules import *

class Tile(Object):
  """ Description of tile """
  def __init__(self, position, type):
    params = TILES[type]
    Object.__init__(self, position, params['OBJECT'])
    self.in_fov_color = self.color
    self.out_fov_color = params['SHADED_COLOR']
    self.explored = False

  def set_in_fov_color(self, color):
    self.color = color
    self.in_fov_color = color

  def set_in_fov(self):
    self.color = self.in_fov_color

  def set_out_fov(self):
    self.color = self.out_fov_color
