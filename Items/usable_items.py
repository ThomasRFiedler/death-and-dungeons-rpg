from . import items
import random

class UsableItem(items.Item):
  def use(self,player):
    pass





class GoldCoins(UsableItem):

  def onInteract(self,player):
  
    # Adds gold based on the player's location
    if player.current_location.name=='abandoned house':
      gold_added = random.randint(1,20)
      player.gold+=gold_added
    else:
      gold_added = random.randint(1,10)
    print(' + ' +str(gold_added) + ' gold!')
    player.current_location.map.pop('Gold Coins')






class PileOfGold(UsableItem):

  def onInteract(self,player):
    gold_added = random.randint(100,300)
    player.gold+=gold_added
    print(' + ' +str(gold_added) + ' gold!')

    #if player.current_location.name=='suspicious cave':
    #  player.current_location.takeItem()
    
    player.current_location.map.pop('Pile of Gold')






class WeakHealthPotion(UsableItem):

  def use(self,player):
    heal = random.randint(5,10)
    player.hp += heal
    
    if player.max_hp < player.hp:
      player.hp = player.max_hp
    
    print(' +', heal,' Health')
    print(str('Health [{}/{}]').format(player.max_hp,player.hp))
