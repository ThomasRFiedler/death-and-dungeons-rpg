'''
The player class. 

This is where most of the game logic including fights and commands takes place.

'''

import time, random, Locations.map, Items.items_registry
from Enemies import dragon


class Player:

    # The player's stats. These may be loaded from the save file.
    #race = 'Human'
    strength = 0
    dexterity = 0
    defense = 0
    max_hp = 10
    hp = 10
    attack = [1, 2]
    xp = 0
    gold = 0
    level = 1

    # Data collection (dictionary)
    # A player has 12 inventory slots.
    inventory = {
        1: '',
        2: '',
        3: '',
        4: '',
        5: '',
        6: '',
        7: '',
        8: '',
        9: '',
        10: '',
        11: '',
        12: '',
    }
    # Data collection (dictionary)
    equipped = {
        'helmet': '',
        'breastplate': '',
        'leggings': '',
        'boots': '',
        'gauntlets': '',
        'weapon': '',
    }

    active_quests = []

    completed_quests = []

    # Data collection (list)
    discovered_areas = []

    current_location = None

    current_region = 'Ancora'
    last_location = 'The Wilderness'
    location = 'The Wilderness'

    # Not implemented yet. This'll prob be similar to the M.C. potion system
    #status = []

    # Data collection (list)
    command = []

    def __init__(self, name):
        self.name = name

    # Lists all available commands
    def printHelp(self):
        print(
            '''\nexplore - wander around\ngo [place] - go somewhere\nstats - display your stats\nmap - open your map\nsave - save your character\nquit - quit the game\ninventory - open your inventory\nget [item] -  get an item\nequip [item] - equip an item from your inventory\ninvestigate - you look around the current area you are in\ntalk [NPC] - talk to someone\nuse [item] - uses an item\nquests - lists active quests
    ''')

    def listQuests(self):
        for quest in self.active_quests:
            print(quest)

    # prints out the inventory in a pretty way
    def printInventory(self):

        item_1 = self.inventory[1]
        item_2 = self.inventory[2]
        item_3 = self.inventory[3]
        item_4 = self.inventory[4]
        item_5 = self.inventory[5]
        item_6 = self.inventory[6]
        item_7 = self.inventory[7]
        item_8 = self.inventory[8]
        item_9 = self.inventory[9]
        item_10 = self.inventory[10]
        item_11 = self.inventory[11]
        item_12 = self.inventory[12]

        items = [
            item_1,
            item_2,
            item_3,
            item_4,
            item_5,
            item_6,
            item_7,
            item_8,
            item_9,
            item_10,
            item_11,
            item_12,
        ]
        item_list = []
        for item in items:
            i = 0

            # if the item's name is too long, it gets cut off with "example item is too lo..."
            if len(item) > 19:
                item = item[0:18] + '...'
                item_list.append(item)
                continue

            # added this loop to make sure they have the currect number of spaces
            i += len(item)
            #while i < 21:
            print('+-----------------------+')

            for i in range(i, 21):
                item += ' '

            print('|', item, '|')

        print('+-----------------------+')
                      

    # The player explores around the current region they are at
    def explore(self):
        from Locations.map import map

        if self.current_location != None:
            exit = self.current_location.exit(self)
            if not exit:
                return

        self.current_location = map[self.current_region]['The Wilderness']
        self.location = 'The Wilderness'
        print('You pick a random direction and start walking...')
        time.sleep(1)

        # 1/3 chance to get ambushed while exploring
        die = self.rollDie()

        if (die == 1 or die == 2):
            print('AMBUSH!!!')

            # Small chance to fight a dragon
            dragon_chance = random.randint(1, 10000) + (10 * self.level)

            if dragon_chance >= 10000:
                #dragon = dragon.typeDragon()
                time.sleep(0.5)
                print('The ground shakes from under you.')
                time.sleep(1.0)
                random_dragon = dragon.TypeDragon()
                random_dragon.ambience()
                self.fight(random_dragon)

            else:
                from Enemies import bandit, skeleton, orc, zombie
                roll = random.randint(1, 6)

                if roll == 1 or roll == 2:
                    enemy = skeleton.Skeleton('Skeleton')

                elif roll == 3 or roll == 4:
                    enemy = bandit.Human('Bandit')

                elif roll == 5:
                    enemy = orc.Orc('Orc')

                elif roll == 6:
                    enemy = zombie.Human('Zombie')

                self.current_location.map.update({enemy.name: enemy})
                enemy.ambience()
                time.sleep(0.5)
                self.fight(enemy)
                return

        # Chooses a random location from map
        new_location = Locations.map.random_location(self)

        # Randomly generates the new location and adds it to the map
        self.location = new_location.name
        new_location.discover(self)

        ask = input('Do you wish to enter? (yes/no):\n> ')

        if ask == 'yes':
            new_location.enter(self)

        # Sets the player location to outside the discovered location
        else:
            self.current_location.map.update({new_location.name: new_location})

    # Displays all the stats
    def displayStats(self):
        time.sleep(0.25)
        print('XP:',self.xp)
        time.sleep(0.25)
        print('Gold:',self.gold)
        time.sleep(0.25)
        print('Level:',self.level)
        time.sleep(0.25)
        print('Strength:',self.strength)
        time.sleep(0.25)
        print('Dexterity:',self.dexterity)
        time.sleep(0.25)
        print('Health: [' + str(self.max_hp) + '/' + str(self.hp) + ']')
        time.sleep(0.25)

    # Displays the inventory and equipped items
    def DisplayInventory(self):
        self.printInventory()

        for equipment in self.equipped:
            time.sleep(0.1)

            if not self.equipped[equipment] == '':
                # Checks if the equipment is a weapon
                if equipment == 'weapon':

                    print(
                        equipment + ':', self.equipped[equipment],
                        Items.items_registry.items[
                            self.equipped[equipment]].damage)

                # Otherwise, if the equipment is an armor piece
                else:
                    print(
                        equipment + ':', self.equipped[equipment],
                        '[' + str(Items.items_registry.items[
                            self.equipped[equipment]].defense * 100) + '%]')
            else:
                print(equipment + ': None.')

    # Displays the map and nearby
    def displayMap(self):
        print('Current Region: ' + self.current_region + '.')
        print('Current Location: ' + self.location + '.')
        places = 'Discovered Areas: '
        if len(self.discovered_areas) > 0:
            i = 0
            for place in self.discovered_areas:
                i += 1
                if (i == len(self.discovered_areas)):
                    if i == 1:
                        pass
                    else:
                        places += ' and '
                    places += place
                    break
                places += place + ','
        else:
            places += 'None'

        print(places + '.')

    # Occurs whenever the player gets xp. Lvl 20 is the max level.
    # Function written by Zachary Banks
    def xpEvent(self):

        # dev command not listed in help (shhh keep secret)
        if len(self.command) > 1:
            try:
                self.xp += int(command[1])
            except:
                return

        # Levels
        LevelDict = {
            1: 43,
            2: 67,
            3: 94,
            4: 133,
            5: 186,
            6: 251,
            7: 370,
            8: 494,
            9: 671,
            10: 900,
            11: 1234,
            12: 1556,
            13: 1957,
            14: 2469,
            15: 3143,
            16: 4345,
            17: 5745,
            18: 7343,
            19: 8943,
            20: 11433,
        }

        for level in LevelDict:
            if level == self.level + 1 and self.xp >= LevelDict[level]:
                self.level = self.level + 1
                print("LEVEL UP!! You are now lvl: " + str(self.level))
                self.xp = self.xp - LevelDict[level]
                # Adds player hp
                self.max_hp = self.level * 5 + 5

                # Player can improve dexterity or strength every certain # of levels
                # Code written by Jack Feinstein
                if self.level % 3 == 0:

                    asking = True
                    while asking:
                        ask = input('Pick a Stat Improvement:\n[Dexterity (' +
                                    str(self.dexterity) + ') / Strength (' +
                                    str(self.strength) + ')]\n> ').lower()

                        if ask == 'strength':
                            self.strength += 1
                            print('Strength: +1\nYour strength is now ' +
                                  str(self.strength))
                            asking = False
                            break

                        elif ask == 'dexterity':
                            self.dexterity += 1
                            print('Dexterity: +1\nYour dexterity is now ' +
                                  str(self.dexterity))
                            asking = False
                            break
                        else:
                            print('Invalid input, try again.')

    # Pretty self explanatory...
    def exitGame(self):
        exit()

    # usage: go [place]
    def go(self):

        isFound = False

        if len(command) > 1:

            # Cycles thru all the places in the map of the current region (currently there's only Ancora)
            for place in Locations.map.map[self.current_region]:

                if command[1] in place.lower():

                    isFound = True

                    if place not in self.discovered_areas:
                        print("You can't go there.")
                        break
                    # Triggers the exit event for the player's current location. Only relevant for places where the player can't leave. For example, look at Locations.fiedler_manor
                    if self.current_location != None:
                        exit = self.current_location.exit(self)
                        if not exit:
                            break

                    self.location = place
                    new_location = Locations.map.map[
                        self.current_region][place]

                    # Triggers the location.enter(player) event
                    if self.current_location == None:
                        new_location.enter(self)

            if not isFound and self.current_location != None:
                # Checks if the place is local (ex. if the player wants to go to the blacksmith in Rome)
                for near in self.current_location.map:
                    if command[1] == near.lower():
                        isFound = True
                        new_location = self.current_location.map[near]
                        new_location.enter(self)
                        break

            if isFound:
                return
            else:
                print('Could not find that place.')

    # Handles the "get [item]" command
    def get(self):

        # Checks if user gave correct input
        if len(command) < 2:
            print('Usage: get [item]')
            return

        isFound = False

        if self.current_location != None:

            for item in self.current_location.map:

                if item.lower() == command[1]:
                    isFound = True

                    if item in Items.items_registry.items:

                        Items.items_registry.items[item].onInteract(self)
                        isFull = True
                        for slot in self.inventory:
                            if self.inventory[slot] == '':
                                isFull = False
                                time.sleep(0.5)
                                print(' + ' + item)
                                time.sleep(0.5)
                                self.inventory[slot] = item
                                break
                        if not isFull:
                            self.current_location.map.pop(item)
                            self.current_location.takeItem(self)
                        else:
                            print('Your inventory is full!')
                        break
                else:
                    continue
        if not isFound:
            print('Could not find that item.')

    # Adds an item to player.equipped
    def equip(self):
        from Items.items_registry import items
        
        if len(command) > 1:
            isFound = False
            for item in items:
                if item.lower() == command[1]:
                    
                    items[item].equip(self)
                    isFound = True
                    break
            if not isFound:
                print("That's not an item.")
        else:
            print('Usage: equip [item]')

    # The player looks around the area they are in. Shows what's nearby the player. For example, if you are in Rome, it will show you the blacksmith.
    def investigate(self):
        print('You look around...')
        time.sleep(1.0)

        # Calls the investigate function for the location class.
        if self.current_location != None:
            self.current_location.investigate(self)
        else:
            print("You don't see anything of note.")

    # Asks the player for a command and then executes it
    def talk(self):
        if self.current_location != None:
            for thing in self.current_location.map:
                #print(place)
                if command[1] == thing.lower():
                    #try:
                    self.current_location.map[thing].talk(self)

                    #except Exception as e:
                    #    print('Error: ' + str(e))

    def use(self):
        if len(command) > 1:
            for slot in self.inventory:
                if command[1] == self.inventory[slot].lower():
                    Items.items_registry.items[self.inventory[slot]].use(self)
                    self.inventory[slot] = ''
        else:
            print('Usage: use [item]')

    '''
  Asks the player for input and runs the command
  All available commands are defined in the commands dictionary object (found in this function)
  '''

    def ask(self):
        global command

        time.sleep(.5)
        raw_command = input('Enter a command.\n> ').lower()

        # List of all commands
        commands = {
            'help': self.printHelp,
            '?': self.printHelp,
            'explore': self.explore,
            'stats': self.displayStats,
            'go': self.go,
            'save': self.save,
            'xp': self.xpEvent,
            'map': self.displayMap,
            'quit': self.exitGame,
            'exit': self.exitGame,
            'inventory': self.DisplayInventory,
            'get': self.get,
            'equip': self.equip,
            'investigate': self.investigate,
            'talk': self.talk,
            'use': self.use,
            'take': self.get,
            'quest': self.listQuests,
            'quests': self.listQuests,
            'suicide': self.die,
        }

        # Turns the input into a list, with values separated at spaces
        isFound = False
        command = []
        for com in commands:

            if com in raw_command[0:len(com)]:

                if len(raw_command) > len(com):
                    command.append(raw_command[:len(com)])
                    command.append(raw_command[1 + len(com):])

                else:
                    command.append(raw_command[:len(com)])

                isFound = True
                self.command = command
                break

        # Checks if the player input is an actual command.
        if not isFound:
            print('Unknown command. Enter "help" for a list of commands.')
        else:
            commands[command[0]]()


    # Combat system
    def fight(self, enemy):

        # The players health gets subtracted by the enemy's
        def attack():

            print('You slash at the ' + enemy.name + '.')
            damage = 0
            if self.equipped['weapon'] != '':
                damage = Items.items_registry.items[self.equipped['weapon']].dealDamage(self)
            else:
                damage = random.randint(self.attack[0], self.attack[1])

            enemy.hp -= damage
            print(' - ' + str(damage))
            print('Enemy health: [' + str(enemy.max_hp) + '/' + str(enemy.hp) + ']')

        def inventory():
            self.printInventory()
            hasItems = False

            for slot in self.inventory:

                if self.inventory[slot] != '':
                    hasItems = True

            if hasItems:
                ask = input('Enter an item to use or equip.\n> ')
                from Items.items_registry import items
                for item in items:
                    if ask == item.lower():
                        if items[item].item_type == 'weapon' or items[
                                item].item_type == 'armor':
                            items[item].equip(self)
                            break

                        Items.items_registry.items[item].use(self)

        
        def run():
            run = random.randint(1, 8)

            if run >= enemy.runDifficulty:
                time.sleep(0.5)

                if self.current_location != None:
                    exit = self.current_location.exit(self)

                    if not exit:
                        time.sleep(0.5)
                        print("You can't get away!")
                        return False

                print('You got away.')

                return True

            else:
                print('The monster caught your leg!')
                return False
                
      

        choices = {
            'attack':attack,
            'run':run,
            'inventory':inventory,
        }
        while True:
            if enemy.hp <= 0:
                enemy.die(self)
                break

            if self.hp <= 0:
                self.die()
                break

            action = input('[Attack, Inventory, Run]\n> ').lower()

            if action == 'attack':
                choices['attack']()

            elif action == 'inventory':
                choices['inventory']()
                continue
            
            elif action == 'run':
                escape = choices['run']()
                if escape:
                    self.current_location = Locations.map.map[self.current_region]['The Wilderness']
                    break
            else:
                continue
            # If the enemy's still alive, then it performs its attack
            if enemy.hp > 0:

                # Takes off a percentage of the attack based on the player's defense
                enemy_damage = round(enemy.damage() * (1 - self.defense))
                self.hp -= (enemy_damage)
                print(' -', enemy_damage)
                time.sleep(0.5)
                print('Health: [' + str(self.max_hp) + '/' + str(self.hp) + ']')

    def die(self):
        print('You died!')

        self.current_location = Locations.map.map[self.current_region]['The Wilderness']

        for slot in self.inventory:
            self.inventory[slot] = ''

        self.gold = 0
        self.hp = self.max_hp

        for item in self.equipped:
            self.equipped[item] = ''

        return

    # Saves the player's stats to the save.py file
    # Code written by Zachary Banks
    def save(self):

        save_file = open('save.py', 'w')
        save_file.write("xp = " + str(self.xp))
        save_file.write('\nmax_hp = ' + str(self.max_hp))
        save_file.write('\nhp = ' + str(self.hp))
        save_file.write('\nattack = ' + str(self.attack))
        save_file.write('\nstrength = ' + str(self.strength))
        save_file.write('\ndexterity = ' + str(self.dexterity))
        save_file.write('\ngold = ' + str(self.gold))
        save_file.write('\nname = ' + '"' + str(self.name) + '"')
        save_file.write('\nlevel = ' + str(self.level))
        save_file.write('\ninventory = ' + str(self.inventory))
        save_file.write('\nequipped = ' + str(self.equipped))
        save_file.write('\ndiscovered_areas = ' + str(self.discovered_areas))
        save_file.write('\ncurrent_region = ' + '"' +
                        str(self.current_region) + '"')
        save_file.write('\nlocation = "The Wilderness"')

        save_file.close()

    def rollDie(self):
        return random.randint(1, 6)
