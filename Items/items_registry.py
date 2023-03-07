from . import weapons,usable_items,armor, items

# Weapons
short_sword = weapons.ShortSword('Short Sword')
mythril_broad_sword = weapons.MythrilBroadSword('Mythril Broad Sword')
bandit_dagger = weapons.BanditDagger('Dagger')
torch = weapons.Torch('Torch')
kitchen_knife = weapons.KitchenKnife('Kitchen Knife')
stake = weapons.Stake('Stake')
op_dev_weapon = weapons.OPDevWeapon('OP Dev Weapon')

# Usable Items
pile_of_gold = usable_items.PileOfGold('Pile of Gold')
gold_coins = usable_items.GoldCoins('Gold Coins')
weak_health_potion = usable_items.WeakHealthPotion('Weak Health Potion')

# Armor
bronze_helmet = armor.BronzeHelmet('Bronze Helmet')
bronze_breastplate = armor.BronzeBreastplate('Bronze Breastplate')
bronze_leggings = armor.BronzeLeggings('Bronze Leggings')
bronze_boots = armor.BronzeBoots('Bronze Boots')
bronze_gauntlets = armor.BronzeGauntlets('Bronze Gauntlets')

# Other items
fiedler_manor_key = items.Item('Fiedler Manor Key')
master_bedroom_key = items.Item('Master Bedroom Key')
garlic = items.Item('Garlic')


# Register all items you make here
items = {
  'Short Sword':short_sword,
  'Mythril Broad Sword':mythril_broad_sword,
  'Dagger':bandit_dagger,
  'Torch':torch,
  'Kitchen Knife':kitchen_knife,
  'Gold Coins':gold_coins,
  'Pile of Gold':pile_of_gold,
  'Weak Health Potion':weak_health_potion,
  'Bronze Helmet':bronze_helmet,
  'Bronze Breastplate':bronze_breastplate,
  'Bronze Leggings':bronze_leggings,
  'Bronze Boots':bronze_boots,
  'Bronze Gauntlets':bronze_gauntlets,
  'Fiedler Manor Key':fiedler_manor_key,
  'Master Bedroom Key':master_bedroom_key,
  'Garlic':garlic,
  'Stake':stake,
  'OP Dev Weapon':op_dev_weapon
}