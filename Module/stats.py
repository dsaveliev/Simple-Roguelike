from world import *

class Stats(object):
  """docstring for Stats"""
  def __init__(self, params):
    self.stats = {}
    for s in params.keys():
      self.stats[s] = Stat(s, params[s])

  def stat_show(self, stat_type, ratio = None):
    stat = self.stats[stat_type]
    if ratio:
      return stat.name + ':' + "{0:3}".format(stat.value) + '/' + str(stat.base_value)
    else:
      return stat.name + ':' + "{0:3}".format(stat.value)
