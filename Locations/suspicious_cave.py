from . import location
from termcolor import colored
import Enemies.dragon,time,random,Items.items_registry

class SuspiciousCave(location.Location):

  class SleepingDragon(Enemies.dragon.NormalDragon):
    runDifficulty = 48

    def wake(self,player):
      print('The dragon yawns and stretches...')
      time.sleep(1.0)
      print('It sniffs the air...')
      time.sleep(0.5)
      print('Growls...')
      time.sleep(0.5)
      print('and starts racing toward you!')
      time.sleep(0.5)
      player.fight(self)

  map = {}

  def takeItem(self,player):
    self.map['Dragon'].wake(player)

  def generate(self):
    self.isGenerated = True
    items_generated = random.randint(10,20)
    pile_of_gold = Items.items_registry.items['Pile of Gold']
    mythril_broad_sword = Items.items_registry.items['Mythril Broad Sword']
    dragon = self.SleepingDragon('Dragon')

    possible_map = (
      {'Pile of Gold':pile_of_gold},
      #{'Mythril Bar':mythril_bar},
      {'Mythril Broad Sword':mythril_broad_sword},
      #{'Iron Great Helm':iron_great_helm},
      #{'Iron Breastplate':iron_breastplate},
      #{'Iron Great Sword':iron_great_sword},
    )
    i=0
    while i < items_generated:
      thing = random.choice(possible_map)
      self.map.update(thing)
      i+=1
    self.map.update({'Dragon':dragon})



  def enter(self,player):

    player.current_location = self

    if not self.isGenerated:
      self.generate()

    print('You enter susipcious looking cave...')
    time.sleep(0.5)
    print('Before you, you see a dragon surrounded by heaping amounts of treasures.')
    time.sleep(0.5)
    print(colored('Be careful not to wake the dragon...','red'))

  def investigate(self,player):
    print('The cavern is massive, supported by stalagmites stretching all the way to the floor.')
    time.sleep(0.5)
    print('In the middle of the cavern, you see a massive '+colored('dragon','red')+' sleeping on top of a pile of gold and trinkets.')
    list_view = []
    for thing in self.map:
      list_view.append(thing)
    
    print('Nearby: ' + str(list_view))

    
    
    
    
    