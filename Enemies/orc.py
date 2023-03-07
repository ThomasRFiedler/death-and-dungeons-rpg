import random,time
from . import enemy
class Orc(enemy.Enemy):
  weight = 10
  hp = 8
  max_hp = 8
  gold = random.randint(5, 20)
  xp = random.randint(10,15)
  runDifficulty = 2
  

  def damage(self):
    time.sleep(0.5)
    choose = random.randint(1,4)
    if choose==1 or choose==2:
      print('The orc strikes you!')
      return random.randint(3,6)
    elif choose==3:
      print('The orc misses!')
      return 0
    elif choose==4:
      print('The orc lands a critical blow!')
      return random.randint(7,13)

  
  def ambience(self):
    print("I'm gonna slice me up some man-flesh!")