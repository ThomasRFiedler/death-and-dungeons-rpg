import random,time
from . import enemy
class Skeleton(enemy.Enemy):
  weight = 10
  hp = 10
  max_hp = 10
  gold = random.randint(1, 10)
  xp = random.randint(10, 15)
  
  runDifficulty = 2

  def damage(self):
    time.sleep(0.5)
    print('The skeleton swings at you!')
    time.sleep(0.5)
    return random.randint(1,2)
  
  # Skeleton fight
  def ambience(self):
    print('An undead human skeleton approaches!')
    #self.damage