from . import npc
from termcolor import colored
import time


class Blacksmith(npc.ShopKeeper):
    sells = {
        'Short Sword': 20,
        'Weak Health Potion': 5,
        'Bronze Helmet': 20,
        'Bronze Breastplate': 80,
        'Bronze Leggings': 80,
        'Bronze Boots': 40,
        'Bronze Gauntlets': 40,
    }

    buys = {
        'Short Sword': 10,
        'Weak Health Potion': 2,
        'Bronze Helmet': 10,
        'Bronze Breastplate': 20,
        'Bronze Leggings': 20,
        'Bronze Boots': 10,
        'Bronze Gauntlets': 10,
    }


class VampireQuestNPC(npc.QuestNPC):
    def talk(self, player):

        if 'Fiedler Manor' in player.active_quests:
            hasFang = False
            for slot in player.inventory:
                if player.inventory[slot] == 'Vampire Fang':
                    hasFang = True
            
            if hasFang:
                print('Oh my.')
                time.sleep(0.5)
                print('...')
                time.sleep(0.5)
                print('I underestimated you.')
                time.sleep(0.5)
                time.sleep(0.5)
                print('Here, as a token of my gratitude.')
            else:
                print('Bring me its',colored('Vampire Fang','yellow'),'as proof of its death.')

        elif 'Fiedler Manor' in player.completed_quests:
            pass

        else:
            if player.level > 4:
                print('Help, traveler!')
                time.sleep(0.5)
                print(
                    'Fell creatures dwell inside the forsaken Fiedler Manor.')
                time.sleep(0.5)
                print(
                    'It is rumored that a vampire lives inside that mansion.')
                time.sleep(0.5)
                print(
                    'Many brave or foolish adventurers like you have entered the manor and never left.'
                )
                time.sleep(0.5)
                print('My father was one of the brave ones.')
                time.sleep(0.5)
                print('Will you avenge my loss, oh brave one? [yes/no]')
                while True:
                    ask = input('> ')
                    if ask == 'no':
                        break
                    elif ask == 'yes':
                        import Items
                        self.quest_started = True
                        time.sleep(0.5)
                        print('Excellent!')
                        time.sleep(0.5)
                        print(
                            'Be warned. If the vampire is still alive, you will need this.')
                        stake = Items.stake
                        player.getItem(stake)
                        time.sleep(0.5)
                        print('Bring me its',colored('Vampire Fang','yellow'),'as proof of its death.')
                        break
            else:
                print(
                    'You must be at least level 5 to start the Fiedler Manor Quest.'
                )

