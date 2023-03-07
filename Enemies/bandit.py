import time,random
from . import enemy


class Human(enemy.Enemy):
    max_hp = random.randint(5,10)
    hp = max_hp
    xp = random.randint(5,15)
    gold = random.randint(2,10)


    def generateLoot(self):
        roll = random.randint(1,2)
        if roll==1:
            self.drops.append('Dagger')
    
    
    def damage(self):
        roll = random.randint(1,4)
        if roll==1:
            print('The bandit misses!')
        else:
            print('The bandit slashes you!')
            return random.randint(1,2)

    
    def ambience(self):
        print('A bandit jumps in your way.')
        time.sleep(0.5)
        print("I'll cut you up, beyotch!")