class World(object):
  _instance = None
  _initialized = None

  def __new__(cls, *args, **kwargs):
    if not cls._instance:
      cls._instance = super(World, cls).__new__(
        cls, *args, **kwargs)
    return cls._instance

  def __init__(self):
    if not self._initialized:
      ### States
      self._initialized = True
      self.game_state = 'PLAYING'
      ### Helpers
      self.panel = Panel()
      self.menu = Menu()
      self.control = Control()
      ### Map
      self.map = Map()
      ### Objects
      self.player = Player()
      self.aim = Aim()
      ### World generation
      self.generate()

  def get_names_at_position(self, x, y, include_player = True):
    names = []
    if libtcod.map_is_in_fov(self.map.fov_map, x, y):
      objects = Creature.get_by_position(x, y)
      objects.extend(Item.get_by_position(x, y))
      if not include_player and self.player in objects:
        objects.remove(self.player)
      for obj in objects:
        names.append(obj.name)
    return ', '.join(names)

  def render_names_at_position(self, x, y):
    names = self.get_names_at_position(x, y)
    self.panel.info(names)

  def tile_blocked(self, x, y):
    if not self.map.get_tile(x, y).passable:
      return True
    objects = Creature.get_by_position(x, y)
    for object in objects:
      if object and not object.passable:
        return object

  def generate_objects(self):
    for room in self.map.rooms:
      num_monsters = libtcod.random_get_int(0, 0, MAX_ROOM_CREATURES)
      for i in range(num_monsters):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        monster = Creature((x,y), Creature.get_random_type('CHAOTIC'))
        num_monsters_items = libtcod.random_get_int(0, 0, MAX_CREATURE_ITEMS)
        for j in range(num_monsters_items):
          monster.inventory.append(Item(None, Item.get_random_type()))
      num_items = libtcod.random_get_int(0, 0, MAX_ROOM_ITEMS)
      for i in range(num_items):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        Item((x,y), Item.get_random_type())

  def generate(self):
    self.map.generate()
    self.player.set_position((self.map.start[0], self.map.start[1]))
    self.generate_objects()
    Text.event_welcome(self.panel, self.player.name)

  def draw(self):
    self.map.draw()
    Item.draw_all()
    Creature.draw_all()
    Object.draw_all()
    self.panel.draw()

  ### Make turn ###############################################################
  def clear(self):
    Creature.clear_all()
    Item.clear_all()

  def turn_creatures(self):
    if self.game_state == 'PLAYING' and self.player.state != 'DIDNT_TAKE_TURN':
      for creature in Creature.list:
        if creature != self.player:
          creature.take_turn()

  def turn(self):
    self.clear()
    self.control.handle_input()
    self.turn_creatures()
  #############################################################################

  def tick(self):
    libtcod.console_clear(con)
    self.draw()
    libtcod.console_blit(con, 0, 0, MAP['WIDTH'], MAP['HEIGHT'], 0, 0, MAP['Y'])
    libtcod.console_flush()
    self.turn()


from modules import *
