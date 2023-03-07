import time


class NPC():
    def talk(self, player):
        print('[Insert dialogue]')

    def __init__(self, name):
        self.name = name


class ShopKeeper(NPC):
    # What the player can sell
    buys = {}

    # What the player can buy
    sells = {}

    def buying(self, player):
        print('Buying: ' + str(self.sells))

    def selling(self, player):
        print('Selling: ' + str(self.buys))

    def talk(self, player):
        print('Hello, welcome to my store.')
        time.sleep(0.5)
        asking = True
        buying = False
        selling = False
        while asking:
            ask = input('Would you like to buy or sell items? [buy/sell/q]\n> '
                        ).lower()

            if ask == 'sell':
                selling = True
                player.printInventory()
                while selling:
                    print('Selling: ' + str(self.buys))
                    time.sleep(0.5)
                    ask = input(
                        'What would you like to sell to me? [item/q]\n> '
                    ).lower()
                    if ask == 'q':
                        selling = False
                        break
                    if ask != '':
                        for item in self.buys:
                            if ask == item.lower():
                                for slot in player.inventory:
                                    if item == player.inventory[slot]:
                                        player.inventory[slot] = ''
                                        player.gold += self.buys[item]
                                        time.sleep(0.5)
                                        print(' - ' + item)
                                        time.sleep(0.5)
                                        print(' + ' + str(self.buys[item]))

                                        continue
                    time.sleep(0.5)

            elif ask == 'buy':
                buying = True
                asking = False
                while buying:
                    print('Buying: ' + str(self.sells))
                    time.sleep(0.5)
                    ask = input(
                        'What would you like to buy from me? [item/q]\n> '
                    ).lower()
                    if ask == 'q':
                        buying = False
                        break
                    if ask != '':
                        for item in self.sells:
                            if ask == item.lower():
                                if player.gold >= self.sells[item]:
                                    isFound = False
                                    for slot in player.inventory:

                                        if player.inventory[slot] == '':
                                            isFound = True
                                            player.gold -= self.sells[item]
                                            print(' - ' +
                                                  str(self.sells[item]) +
                                                  ' gold')
                                            print(' + ' + item)
                                            player.inventory[slot] = item
                                            break

                                    if not isFound:
                                        time.sleep(0.5)
                                        print('Your inventory is full!')

                                elif player.gold < self.sells[item]:
                                    time.sleep(0.5)
                                    print('Oy vey. You tryna scam me?')
                                    time.sleep(0.2)
                                    print('Gold: ' + str(player.gold))
                                    time.sleep(0.2)
                                    print('Cost: ' + str(self.sells[item]))

                    time.sleep(0.5)
            elif ask == 'q':
                asking = False
                break
            time.sleep(0.5)
        '''if buying:
      self.buying(player)
    elif not buying:
      self.selling(player)'''


class QuestNPC(NPC):

    quest_started = False
    quest_completed = False

    quest_reward = {
        'xp': 0,
        'gold': 0,
        'items': [],
    }

    def questComplete(self, player):

        self.quest_completed = True
