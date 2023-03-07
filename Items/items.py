import random,time

class Item:
    
    item_type = ''
    armor_type = ''

    value = 0

    def take(self,player):
        
        self.onInteract(player)
        
        isFull = True
        for slot in player.inventory:

            if player.inventory[slot] == '':
                print(' +', self.name)
                player.inventory[slot] = self.name
                isFull = False
                break

        if isFull:
            print('Your inventory is full!')
            time.sleep(0.5)
            print('Items dropped.')

            if self.current_location != None:
                player.current_location.map.update({self.name: self})

    # Called to equip an item to the player
    def equip(self, player):
        print("You can't equip",self.name+'!')
    
    # Occurs when the player attemps to 'get' an item
    def onInteract(self, player):
        pass

    
    # Called when the player uses the item
    def use(self,player):
        print("You can't use this!")

    
    def __init__(self, name):
        self.name = name