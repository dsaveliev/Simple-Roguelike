from world import * 

world = World()
#World.generate()
### Main loop
while not libtcod.console_is_window_closed():
  world.tick()
  if world.game_state == 'EXIT':
    break
