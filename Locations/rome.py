from . import location
import time


class Rome(location.Location):
    class BlackSmith(location.Location):
        from NPC import rome_npc
        blacksmith = rome_npc.Blacksmith
        map = {
            'David': blacksmith,
        }

        def enter(self, player):
            print('You enter the blacksmith.')
            player.current_location = self

    blacksmith = BlackSmith('Blacksmith')
    pub = None
    job_board = None

    # This is what the player sees when they investigate

    map = {
        "The Prancing Pony": pub,
        "Job Board": job_board,
        'Blacksmith': blacksmith,
    }

    # when you go in Rome
    def enter(self, player):
        print('You wander into the great city of Rome.')

        if player.current_location != None:
            player.current_location.exit(player)
        if not self.isGenerated:
            self.generate()

        player.current_location = self

    # whenever player.investigate is called
    def investigate(self, player):
        print('Around you, you find that the bustling city of Rome,')
        time.sleep(0.5)
        print('with her bustling architecture and beautiful atmosphere,')
        time.sleep(0.5)
        print('is ideal for glory seeking.')
        time.sleep(0.5)

        view_list = []
        for place in self.map:
            view_list.append(place)
        print('You see ' + str(view_list))
  
    def discover(self,player):
        time.sleep(0.5)
        print('You discover the great city of Rome.')
        time.sleep(0.5)
        print('The city is surrounded by thick marble walls')
        time.sleep(0.5)
        print('They are adorned with statues of various Gods and Goddesses.')
        time.sleep(0.5)
        print('[Rome has been added to your map]')
        player.discovered_areas.append('Rome')
