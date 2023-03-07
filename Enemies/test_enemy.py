from . import enemy
class BigRooster(enemy.Enemy):
  hp=2
  max_hp=2
  gold=100
  xp=100
  run_difficulty=100

  # Added a bunch of loot for video
  def generateLoot(self):
    import Items.items_registry
    self.drops.append(Items.items_registry.items['Mythril Broad Sword'])
    self.drops.append(Items.items_registry.items['Weak Health Potion'])
    self.drops.append(Items.items_registry.items['Bronze Helmet'])

  def damage(self):
    from random import randint
    from time import sleep
    roll = randint(1,3)
    if roll != 3:
      print('The rooster pecks at you!')
      sleep(0.5)
      return 1
    else:
      print('The rooster tries to fly!')
      sleep(0.5)
      print('...')
      sleep(0.5)
      roll = randint(1,2)
      if roll==1:
        print('It claws at your face!')
        return 2
      else:
        print("He can't get off the ground!")
        return 0
  
  def ambience(self):
    from time import sleep
    sleep(0.5)
    print('A big rooster struts your way!')
    sleep(0.5)
    print('...')
    sleep(0.5)
    print('Prepare to fight!')
    sleep(0.5)