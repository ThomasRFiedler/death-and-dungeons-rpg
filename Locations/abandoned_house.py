from . import location
import random,time,Items.items_registry,NPC.npc,Enemies.zombie,Enemies.skeleton

class AbandonedHouse(location.Location):
  
  class Upstairs(location.Location):
    map = {}

    def exit(self,player):
      if len(player.command) > 1:
        if player.command[1] == 'downstairs':
          print('You go downstairs.')
      else:
        print('You exit the ' + self.name + '.')
      
      player.last_location = self.name
      player.current_location = None
      player.location = 'The Wilderness'
      return True
    
    def generate(self):
      
      self.isGenerated = True

      human_zombie = Enemies.zombies.Human('Undead Human')
      gold_coins = Items.items_registry.items['Gold Coins']
      weak_health_potion = Items.items_registry.items['Weak Health Potion']

      possible_generate = (
        {'Undead Human':human_zombie},
        {'Gold Coins':gold_coins},
        {'Weak Health Potion':weak_health_potion}
      )
      generate_number = random.randint(1,2)
      i = 0
      while i < generate_number:
        i+=1
        thing = random.choice(possible_generate)
        self.map.update(thing)

    def enter(self,player):
      player.location = 'Abandoned House'
      downstairs = player.current_location
      
      if player.current_location != None:
        player.current_location.exit(player)
      
      print('You walk up the creaky steps...')
      time.sleep(0.5)
      print('...')
      time.sleep(0.5)

      player.current_location = self
      if not self.isGenerated:
        self.generate()
  
      if 'Undead Human' in self.map:
        self.map['Undead Human'].ambience()
        player.fight(self.map['Undead Human'])
      else:
        skeleton = Enemies.skeleton.Skeleton('Skeleton')
        skeleton.ambience()
        player.fight(skeleton)

      self.map.update({'Downstairs':downstairs})
  




  def exit(self,player):
  
    if len(player.command) > 1:
      if player.command[1] == 'upstairs':
        print('You go upstairs.')
    else:
      print('You exit the ' + self.name + '.')

    player.last_location = self.name
    player.current_location = None
    player.location = 'The Wilderness'
    return True
    
  def generate(self):
    self.isGenerated=True
    self.map = {}

    upstairs = self.Upstairs('Upstairs')
    goblin = NPC.npc.NPC('Goblin')
    
    # Picks the amount of times to iterate thru the while loop to generate what's nearby
    number_nearby = random.randint(1, 3)
    
    possible_nearby = (
      {'Short Sword':Items.items_registry.items['Short Sword']}, 
      {'Goblin':goblin},
      {'Gold Coins':Items.items_registry.items['Gold Coins']}, 
      {'Upstairs':upstairs},
    )
    
    # Randomly generates what's in the abandoned house
    i = 0
    while i < number_nearby:
      i+=1
      thing = random.choice(possible_nearby)
      
      self.map.update(thing)
    
    
    upstairs = {
      'Downstairs':self,
    }
    
  def enter(self, player):
    if player.current_location != None and player.current_location != self:
      player.current_location.exit(player)
    if player.last_location == 'Upstairs':
      print('You walk down the creaky steps...')
    else:
      print('You walk into an old, creepy house...')
      player.current_location = self
      
      if not self.isGenerated:
        self.generate()

      if 'Goblin' in self.map:
        time.sleep(0.5)
        print('A goblin snarls at you.')
      
      if 'Gold Coins' in self.map or 'Short Sword' in self.map:
        time.sleep(0.5)
        print('You see something glimmer out of the corner of your eye.')
      
      if 'Upstairs' in self.map:
        time.sleep(0.5)
        print('There is an upstairs.')
    
    time.sleep(0.5)