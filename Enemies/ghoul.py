import time,random
from . import enemy
class Ghoul(enemy.Enemy):
    max_hp = 10 + random.randint(-2,10)
    hp = max_hp
    xp = 20 + random.randint(5,20)
    gold = 20 + random.randint(5,20)

    runDifficulty = 3

    def damage(self):
        roll = random.randint(1,5)
        if roll < 4:
            print('The ghoul bites you!')
            return random.randint(2,5)
        elif roll == 4:
            print('The ghoul misses!')
            return 0
        elif roll == 5:
            print('The ghoul tears your flesh, consuming it!')
            time.sleep(0.5)
            heal = random.randint(1,2)
            if (self.hp + heal) > self.max_hp:
                self.hp = self.max_hp
            else:
                self.hp+=heal
            print(' +', heal)
            print('Ghoul Health:', '['+ str(self.max_hp) +'/'+ str(self.hp) +']')
            time.sleep(0.5)

            return random.randint(8,14)

                    
    def ambience(self):
        print('A ghoul')
        time.sleep(0.25)
        print('--a flesh-craving monster unable to feel pain--')
        time.sleep(0.25)
        print('Approaches you!')