from . import items
import random,time


class Weapon(items.Item):

    dexterity_req = 0
    value = 20
    item_type = 'weapon'
    # [min damage, max damage]
    damage = [0, 0]

    # Returns the amount of damage the player will do based on their strength
    def dealDamage(self, player):
        return (random.randint(self.damage[0], self.damage[1]) +
                player.strength)

    def equip(self, player):
        # If the player doesn't have enough dexterity
        if self.dexterity_req > player.dexterity:
            print('Unable to equip.')
            time.sleep(0.5)
            print('Dexterity requirement:',self.dexterity_req)
            time.sleep(0.5)
            print('Your dexterity:',player.dexterity)
        
        else:
            for slot in player.inventory:
              
                if player.inventory[slot]==self.name:
                    
                    # If the player has a weapon equipped, it swaps the weapons
                    if player.equipped['weapon']!='':
                        player.inventory[slot] = player.equipped['weapon']
                    else:
                        player.inventory[slot] = ''
                    
                    break
            
            player.equipped['weapon'] = self.name

            print('Equipped',self.name+'.')
      
        


class ShortSword(Weapon):
    value = 10
    damage = [2, 4]


class MythrilBroadSword(Weapon):
    value = 400
    damage = [12, 15]
    dexterity_req = 1


class BanditDagger(Weapon):
    value = 10
    damage = [1, 3]


class Torch(Weapon):
    value = 5
    damage = [1, 2]


class KitchenKnife(Weapon):
    value = 5
    damage = [1, 3]


class Stake(Weapon):
    value = 5
    damage = [2, 2]

class OPDevWeapon(Weapon):
    value = 0
    damage = [666,666]