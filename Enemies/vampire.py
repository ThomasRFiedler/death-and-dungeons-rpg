import time, random
from . import enemy
class Vampire(enemy.Enemy):
    max_hp = 30 + random.randint(-10,10)
    hp = max_hp
    xp = 80 + random.randint(-10,30)
    gold = 80 + random.randint(-10,30)
    runDifficulty = 4

    def damage(self):
        roll = random.randint(1,6)
        if roll==1 or roll==5 or roll==6:
            print('The vampire strikes you!')
            return random.randint(2,5)
        elif roll==2:
            print('The vampire bites you, drawing blood!')
            heal = random.randint(1,3)
            if (self.hp + heal) > self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp+=heal
            print(' +', heal)
            print('Vampire Health:', '['+ str(self.max_hp) +'/'+ str(self.hp) +']')
            time.sleep(0.5)
            return random.randint(5,10)
        elif roll==3:
            print('The vampire misses!')
            return 0
        elif roll==4:
            print('The vampire strikes a critical blow!')
            return random.randint(5,10)
    
    def ambience(self):
        print('A vampire')
        time.sleep(0.5)
        print('--An immortal creature of the night--')
        time.sleep(0.5)
        print('Approaches you!')
        time.sleep(0.5)         