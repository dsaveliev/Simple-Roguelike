from world import *

class Stat(object):
  """docstring for Stat"""
  def __init__(self, type, value):
    params = STATS[type]
    self.full_name = params['NAME']
    self.name = type
    self.restorable = params['RESTORABLE']
    self.updatable = params['UPDATABLE']
    self.base_value = value
    self.value = value

