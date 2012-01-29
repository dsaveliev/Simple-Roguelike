# -*- coding: utf-8 -*-
class Game(object):
  """
  Главный класс, представляющий игру. 
  В конструкторе задается начальное состояние игры
  и вызывается метод, создающий необходимые параметры.
  """
  def __init__(self):
    self.__initialize()
    self.state = 'PLAYING'

  def __initialize(self):
    """
    Инициализация параметров игры.
    """
    """ Главное меню """
    self.menu     = Menu(self)
    """ Окно помощи """
    self.help     = PlainText('./Texts/help')
    """ Панель, отображающая состояние игры """
    self.panel    = Panel(self)
    """ Обработчик пользовательского ввода """
    self.control  = Control(self)
    """ Прицел для дистанционных атак """
    self.aim      = Aim(self)
    """ Объект, представляющий текущую карту """
    self.map      = Map(self)
    """ Списки существ, вещей и прочих игровых объектов """
    Creature.list = []
    Item.list     = []
    Object.list   = []

  def main_menu(self):
    """ 
    Главное меню.
    Здесь задается фоновая картинка и происходит
    обработка пунктов меню.
    """
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
        choice = None
      elif choice == 3:
        break
      else:
        choice = self.menu.show(Text.main_menu(), 
          Text.main_menu_options(), (5, None))

  """
  Функции, используемые в главном меню.
  """
  def __show_help(self):
    """
    Вывод окна помощи.
    """
    while not libtcod.console_is_window_closed():
     if self.help.show((0,0, SCREEN_WIDTH, SCREEN_HEIGHT)):
        break
  
  def __update(self):
    """
    Обработка объектов, загруженных из сейва. Т.к. объект
    game создается заново, я обновляю его у всех параметров.
    Так же пересоздаю FOV.
    """
    self.menu.game = self
    self.control.game = self
    self.map.game = self
    self.aim.game = self
    for creature in Creature.list:
      creature.game = self
    self.player.is_fov_recompute = True
    self.map.prepare_fov()

  def __save_game(self):
    """
    Сохранение игры с помощью модуля Shelve.
    """
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
    """
    Загрузка игры из сэйва и подготовка загруженных объектов
    в методе __update.
    """
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
    """
    Созадние новой игры.
    """
    self.state = 'PLAYING'
    self.__initialize()
    self.map.generate()
    self.player = Player(self, (self.map.start[0], self.map.start[1]))
    self.__generate_objects()
    Text.event_welcome(self.player.name)

  def __start_game(self):
    """
    Запуск глобального цикла игры.
    """
    while not libtcod.console_is_window_closed():
      """ Очистка игрового экрана """
      libtcod.console_clear(con)
      """ Отрисовка карты, объектов и панели """
      self.__draw()
      """ Блиттинг изображения и вывод его на экран """
      libtcod.console_blit(con, 0, 0, MAP['WIDTH'], MAP['HEIGHT'], 0, 0, MAP['Y'])
      libtcod.console_flush()
      """ Обработка пользовательского ввода и ход AI """
      self.__turn()
      """ Проверка состояния игры """
      if self.state == 'EXIT':
        self.__save_game()
        break

  def __generate_objects(self):
    """
    Генерация игровых объектов.
    
    Цикл проходит по всем комнатам на карте.
    Количество вещей и созданий (далее - объектов) в комнате определяется случайно,
    с учетом глобальных параметров MAX_ROOM_CREATURES и MAX_ROOM_CREATURES.
    
    У каждого объекта есть параметр PREVALENCE, который
    определяет вероятность, с которой объект будет создан. 
    
    Каждому созданию кладется случайное количество
    вещей в инвентарь, на основе глобального параметра MAX_CREATURE_ITEMS.
    """
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

  ### Turn ####################################################################
  def __clear(self):
    """
    Очистка изображений всех созданий и вещей на карте.
    """
    Creature.clear_all()
    Item.clear_all()

  def __turn_creatures(self):
    """
    Если игра не находится в терминальном состоянии, то
    каждое существо делает ход.
    """
    if self.state == 'PLAYING' and self.player.take_turn:
      for creature in Creature.list:
        if creature != self.player:
          creature.take_turn()

  def __turn(self):
    """
    Очистка карты перед ходом. Обработка пользовательского ввода и ход AI.
    """
    self.__clear()
    self.control.handle_input()
    self.__turn_creatures()
  #############################################################################

  ### Draw game ##############################################################
  def __draw(self):
    """
    Отрисовка игровых объектов
    """
    self.map.draw()
    Item.draw_all(self.map.fov_map)
    Creature.draw_all(self.map.fov_map)
    Object.draw_all()
    self.panel.draw()
  #############################################################################

  ### Utilities ###############################################################
  def render_names_at_position(self, x, y):
    """
    Вспомогательная функция, отображает на панели имена существ в
    заданном тайле.
    """
    names = self.map.get_names_at_position(x, y)
    self.panel.info(names)
  #############################################################################

from modules import *
