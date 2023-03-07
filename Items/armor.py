from . import items

class Armor(items.Item):
  defense = 0
  item_type = 'armor'
  armor_type = ''
  
  def equip(self,player):
    # If the player has an item equipped
    if player.equipped[self.armor_type] != '':
      for slot in player.inventory:
        if player.inventory[slot] == self.name:
          player.inventory[slot] = player.equipped[self.armor_type]
          break

    else:
      for slot in player.inventory:
        
        if player.inventory[slot] == self.name:
          player.inventory[slot] = ''
          break

    player.equipped[self.armor_type] = self.name
    
    print('Equipped',self.name+'.')
  
  # Ex. bronze_helmet = Armor('Bronze Helmet', 'helmet')
  def __init__(self, name):
    self.name = name


class BronzeHelmet(Armor):
  defense = 0.025
  armor_type = 'helmet'


class BronzeBreastplate(Armor):
  defense = 0.05
  armor_type = 'breastplate'


class BronzeLeggings(Armor):
  defense = 0.05
  armor_type = 'leggings'


class BronzeBoots(Armor):
  defense = 0.025
  armor_type = 'boots'


class BronzeGauntlets(Armor):
  defense = 0.015
  armor_type = 'gauntlets'