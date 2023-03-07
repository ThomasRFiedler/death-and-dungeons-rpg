import random,time,player
from . import enemy
# Code written by Jack Feinstein, edited by Tommy Fiedler
class Dragon(enemy.Enemy):
  runDifficulty = 12
  
  breathWeaponRecharge = False
  dragonDamageMultiplier = 1
  #weight = 10000
  airSpeed = 60
  hp = 400
  max_hp = 400

  def groundPoundAttack(self):
    return (random.randint(1,4) + 3) * self.dragonDamageMultiplier

  def fangAttack(self):
    return (random.randint(1,8) + 3) * self.dragonDamageMultiplier
    
  # Dragon breathWeaponDamage recharge
  def breathWeaponRechargeRoll(self):
    self.recharge = random.randint(1,6)
    if self.recharge >= 5:
      self.breathWeaponRecharge = True
    else:
      self.breathWeaponRecharge = False
      
  # Breath Weapon Attack
  def breathWeapon(self):
    #if self.breathWeaponRecharge == True:
    return (random.randint(1,20) + 5) * self.dragonDamageMultiplier
  
  def damage(self):
    #while player.isFighting:
    if not self.breathWeaponRecharge:
      self.breathWeaponRecharge = True
      print('The dragon opens its mouth wide...')
      time.sleep(.5)
      print("...")
      time.sleep(.5)
      print('A rush of flame bursts from its mouth!')    
      #damage = self.breathWeapon()
      #print(damage)
      return self.breathWeapon()
      #return damage
      #self.breathWeaponRechargeRoll()
    else:
      #roll = random.randint(1,2)
      #if roll==1:
      #  self.breathWeaponRecharge = False
      self.breathWeaponRechargeRoll()
      attack = random.choice((self.fangAttack(),self.groundPoundAttack()))
      if attack == self.fangAttack():
        print('The dragon slashes you with its claws!')
        return self.fangAttack()
      else:
        print('The dragon flies into the air and attempts to land onto you!')
        return self.groundPoundAttack()
  
class NormalDragon(Dragon):
  xp = 1000+random.randint(-300,600)
  gold = 250+ random.randint(-100,100)
  max_hp = 400 + random.randint(-100,100)
  hp = max_hp

  
class MagicInfusedDragon(Dragon):
  xp = 2000+random.randint(-600,1200)
  gold = 500 + random.randint(-150,150)
  dragonDamageMultiplier = 1.5
  max_hp = 600 + random.randint(-200,200)
  hp = max_hp


class AncientDragon(Dragon):
  xp = 10000+random.randint(-3000,6000)
  gold = 1000 + random.randint(-300,600)
  max_hp = 800 + random.randint(-200,200)
  hp = max_hp
  dragonDamageMultiplier = 2
  airSpeed = 30
    
  #breathWeaponDamage = (random.randint(1,20) + 5) * dragonDamageMultiplier

'''# Dragon index
def TypeDragon():
  normal_dragon = NormalDragon('Normal Dragon')
  magic_infused_dragon = MagicInfusedDragon('Magic Infused Dragon')
  ancient_dragon = AncientDragon('Ancient Dragon')
  DragonIndex = [normal_dragon, magic_infused_dragon, ancient_dragon]
  return random.choice(DragonIndex)'''


''' 
Normal dragon has fangs, breath weapon, landing,

Magic infused dragon has magical fangs, magical breath weapon, boost to its AirSpeed

Ancient dragon has damage boost, insane breath weapon, low AirSpeed

'''