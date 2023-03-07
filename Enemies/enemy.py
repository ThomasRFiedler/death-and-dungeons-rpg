import time


# Base enemy class
class Enemy():
    # [min, max]
    #damage = [0,0]
    #weight = 0
    xp = 0
    hp = 0
    max_hp = 0
    gold = 0
    drops = []
    runDifficulty = 1

    def __init__(self, name):
        self.name = name

    # Look at test_enemy.py for an example on how to implement
    def generateLoot(self):
        pass

    def ambience(self):
        print('A', self.name, 'approaches you, looking for a fight!')

    def die(self, player):
        self.generateLoot()
        print('You defeated the', self.name + '!')
        time.sleep(0.5)
        player.gold += self.gold
        print(' + ' + str(self.gold) + ' gold')
        player.xp += self.xp
        time.sleep(0.5)
        print(' + ' + str(self.xp) + ' xp')
        player.xpEvent()
        time.sleep(0.5)
        if len(self.drops) > 0:
            for item in self.drops:
                item.take(player)

        if player.current_location != None:
            player.current_location.map.pop(self.name)


# sets how strong enemy is related to player

# "MagicInfusedDragon" : 1000, "Dragon" : 800, "Zombie" : 10, "Skeleton" : 10, "Ghouls" : 5, "EvilWizard" : 300
# EvilApprentice : 150, DarkMage :
