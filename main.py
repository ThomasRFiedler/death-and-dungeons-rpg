import random,time,player,Enemies.dragon,Enemies.test_enemy

class Game:

  '''
  Creates a new player object and sets its values to the values imported from the file.
  Called whenever the player runs the program. 
  Code written by Zachary Banks
  '''
  def load(self):
    global player
    load_game = input("Load Game? (yes/no): ")
    if load_game == "yes":
      from save import xp
      from save import max_hp
      from save import hp
      from save import strength
      from save import dexterity
      from save import attack
      from save import gold
      from save import name
      from save import level
      from save import inventory
      from save import equipped
      from save import discovered_areas
      from save import current_region
      from save import location
    
      player = player.Player(name)
      player.xp = xp
      player.max_hp = max_hp
      player.hp = hp
      player.strength = strength
      player.dexterity = dexterity
      player.attack = attack
      player.gold = gold
      player.level = level
      player.inventory = inventory
      player.equipped = equipped
      player.discovered_areas = discovered_areas
      player.current_region = current_region
      player.location = location

      self.save = True
    

  # Starts the game and initializes territories
  def startLoop(self):
    global player
    self.save = False

    # Prompts user if they want to load a game
    self.load()
      
    # Creates new character
    if not self.save:
      name = input('Enter thou name!\n> ')
      player = player.Player(name)
      print('Welcome to Eia,',name+'.')       
      time.sleep(1.0)
      print('Be wary.')
      time.sleep(1.0)
      from termcolor import colored
      print(colored('Dark creatures roam these lands.','red'))
      time.sleep(2.0)
    #ddragon = Enemies.dragon.NormalDragon('big boi draggy')
    #player.fight(ddragon)
    enemy = Enemies.test_enemy.BigRooster('Big Mean Rooster')
    enemy.ambience()
    time.sleep(0.5)
    player.fight(enemy)

    '''ask = input('Debug? (yes/no): ')
    if ask == 'yes':
      while True:
        player.ask()'''
    

    # The main loop. Everything other than save/load happens here 
    while True:
      
      try:
        player.ask()
      except Exception as e:
        print('Error: ' + str(e))

# Source for banner: https://manytools.org/hacker-tools/ascii-banner/
print('''
 ######                             
 #     # ######   ##   ##### #    # 
 #     # #       #  #    #   #    # 
 #     # #####  #    #   #   ###### 
 #     # #      ######   #   #    # 
 #     # #      #    #   #   #    # 
 ######  ###### #    #   #   #    # 
''')
time.sleep(0.5)
print('''
                  
   ##   #    # #####  
  #  #  ##   # #    # 
 #    # # #  # #    # 
 ###### #  # # #    # 
 #    # #   ## #    # 
 #    # #    # #####  
                      
''')
time.sleep(0.5)
print('''                                                  
 #####  #####    ##    ####   ####  #    #  ####  
 #    # #    #  #  #  #    # #    # ##   # #      
 #    # #    # #    # #      #    # # #  #  ####  
 #    # #####  ###### #  ### #    # #  # #      # 
 #    # #   #  #    # #    # #    # #   ## #    # 
 #####  #    # #    #  ####   ####  #    #  ####  
''')
time.sleep(0.5)
# Creates game object and begins the loop
game = Game()
game.startLoop()