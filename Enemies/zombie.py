import random,time
from . import enemy
class Human(enemy.Enemy):
  hp = 30
  max_hp = 30
  gold = random.randint(10, 30)
  xp = random.randint(30, 40)

  runDifficulty = 3

  def damage(self):
    time.sleep(0.5)
    pick = random.randint(1,3)
    if pick==1:
      print('The zombie lunges at you!')
      return random.randint(0,1)
    elif pick==2:
      print('The zombie swings at you!')
      return random.randint(0,1)
    else:
      print('The zombie bites you!')
      return random.randint(2,5)
    time.sleep(0.5)
    
  

  def ambience(self):
    print('An undead human zombie approaches!')
    time.sleep(0.5)
    print('Its rotting flesh barely clings on to its body.')
    #self.damage