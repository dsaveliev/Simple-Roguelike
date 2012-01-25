# -*- coding: utf-8 -*-
import pdb
class Game(object):
  def __init__(self):
    self.__initialize()
    self.state = 'PLAYING'

  def __initialize(self):
    self.menu     = Menu(self)
    self.help     = PlainText('./Texts/help.txt')
    self.control  = Control(self)
    self.panel    = Panel(self)
    self.aim      = Aim(self)
    self.map      = Map(self)
    Creature.list = []
    Item.list     = []
    Object.list   = []

  def main_menu(self):
    image = libtcod.image_load(SPLASH_IMAGE)
    choice = None
    while not libtcod.console_is_window_closed():
      libtcod.image_blit_2x(image, 0, 0, 0)
      libtcod.console_clear(con)
      if choice == 0: 
        self.__new_game()
        self.__start_game()
        choice = None
      elif choice == 1:
        self.__load_game()
        self.__start_game()
        choice = None
      elif choice == 2:
        self.__show_help()
      elif choice == 3:
        break
      else:
        choice = self.menu.show(Text.main_menu(), 
          Text.main_menu_options(), (5, None))

  ### Base game functions #####################################################
  def __show_help(self):
    while not libtcod.console_is_window_closed():
      self.help.show((0,0, SCREEN_WIDTH, SCREEN_HEIGHT))

  def __update(self):
    self.menu.game = self
    self.control.game = self
    self.map.game = self
    self.aim.game = self
    for creature in Creature.list:
      creature.game = self
    self.player.is_fov_recompute = True
    self.map.prepare_fov()

  def __save_game(self):
    if self.player in Creature.list:
      Creature.list.remove(self.player)
    elif self.player.state == 'DEAD':
      pass
    file = shelve.open(SAVE_FILE, 'n')
    file['creatures'] = Creature.list
    file['items'] = Item.list
    file['map'] = self.map
    file['messages'] = self.panel.messages
    file['player'] = self.player
    file['player.state'] = self.player.state
    file.close()

  def __load_game(self):
    file = shelve.open(SAVE_FILE, 'r')
    Creature.list       = file['creatures']
    Item.list           = file['items']    
    self.map            = file['map']      
    self.panel.messages = file['messages']    
    self.player         = file['player']   
    self.player.state   = file['player.state']
    self.state          = 'PLAYING'
    file.close()
    if self.player and self.player.state != 'DEAD':
      Creature.list.append(self.player)
    self.__update()

  def __new_game(self):
    self.state = 'PLAYING'
    self.__initialize()
    self.map.generate()
    self.player = Player(self, (self.map.start[0], self.map.start[1]))
    self.__generate_objects()
    Text.event_welcome(self.player.name)

  def __start_game(self):
    while not libtcod.console_is_window_closed():
      libtcod.console_clear(con)
      self.__draw()
      libtcod.console_blit(con, 0, 0, MAP['WIDTH'], MAP['HEIGHT'], 0, 0, MAP['Y'])
      libtcod.console_flush()
      self.__turn()
      if self.state == 'EXIT':
        self.__save_game()
        break
  #############################################################################

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
    if self.state == 'PLAYING' and self.player.take_turn:
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
