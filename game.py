class Game(object):
  def __init__(self):
    self.menu = Menu(self)
    self.control = Control(self)
    self.aim = Aim()

  def __save(self):
    file = shelve.open(SAVE_FILE, 'n')
    #file['creatures'] = Creature.list
    #file['items'] = Item.list
    #file['objects'] = Object.list
    #file['map'] = self.map
    #file['panel'] = self.panel
    file['player'] = self.player
    #file = open(SAVE_FILE, 'w')
    #marshal.dump(r, file)
    file.close()

  def __load(self):
    pass

  def new_game(self):
    ### Clean up Objects lists
    Creature.list = []
    Item.list = []
    Object.list = []
    ### Map
    self.map = Map(self)
    self.map.generate()
    self.panel = Panel(self)
    Text.panel = self.panel
    ### Objects
    self.player = Player(self, (self.map.start[0], self.map.start[1]))

    #self.player.set_position((self.map.start[0], self.map.start[1]))
    self.__generate_objects()

    Text.event_welcome(self.player.name)

  def continue_game(self):
    pass

  def start_game(self):
    self.state = 'PLAYING'
    while not libtcod.console_is_window_closed():
      libtcod.console_clear(con)
      self.__draw()
      libtcod.console_blit(con, 0, 0, MAP['WIDTH'], MAP['HEIGHT'], 0, 0, MAP['Y'])
      libtcod.console_flush()
      self.__turn()
      if self.state == 'EXIT':
        self.__save()
        break

  def main_menu(self):
    image = libtcod.image_load(SPLASH_IMAGE)
    while not libtcod.console_is_window_closed():
      libtcod.image_blit_2x(image, 0, 0, 0)
      choice = self.menu.show(Text.main_menu(), 
        Text.main_menu_options(), (5, None))
      if choice == 0: 
        libtcod.console_clear(con)
        self.new_game()
        self.start_game()
      elif choice == 1:
        pass
      elif choice == 2:
        pass
      elif choice == 3:
        break

  ### Generate new game ######################################################
  def __generate_objects(self):
    for room in self.map.rooms:
      num_monsters = libtcod.random_get_int(0, 0, MAX_ROOM_CREATURES)
      for i in range(num_monsters):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        monster = Creature(self, (x,y), Creature.get_random_type('CHAOTIC'))
        num_monsters_items = libtcod.random_get_int(0, 0, MAX_CREATURE_ITEMS)
        for j in range(num_monsters_items):
          monster.inventory.append(Item(None, Item.get_random_type()))
      num_items = libtcod.random_get_int(0, 0, MAX_ROOM_ITEMS)
      for i in range(num_items):
        x = libtcod.random_get_int(0, room.x1 + 1, room.x2 - 1)
        y = libtcod.random_get_int(0, room.y1 + 1, room.y2 - 1)
        Item((x,y), Item.get_random_type())
  #############################################################################

  ### Make turn ###############################################################
  def __clear(self):
    Creature.clear_all()
    Item.clear_all()

  def __turn_creatures(self):
    if self.state == 'PLAYING' and self.player.state != 'DIDNT_TAKE_TURN':
      for creature in Creature.list:
        if creature != self.player:
          creature.take_turn()

  def __turn(self):
    self.__clear()
    self.control.handle_input()
    self.__turn_creatures()
  #############################################################################

  ### Draw game ##############################################################
  def __draw(self):
    self.map.draw()
    Item.draw_all(self.map.fov_map)
    Creature.draw_all(self.map.fov_map)
    Object.draw_all()
    self.panel.draw()
  #############################################################################

  ### Utilities ###############################################################
  def render_names_at_position(self, x, y):
    names = self.map.get_names_at_position(x, y)
    self.panel.info(names)
  #############################################################################

from modules import *
