import time,random, Items.items_registry
from . import location
from termcolor import colored

class FiedlerManor(location.Location):

    class SecondFloor(location.Location):

        class ThirdFloor(location.Location):
            
            class Attic(location.Location):

                map = {'Master Bedroom Key':Items.items_registry.items['Master Bedroom Key'],}

                def enter(self,player):

                    if not self.isGenerated:
                        third_floor = player.current_location
                        self.map.update({'Third Floor':third_floor})
                        weak_health_potion = Items.items_registry.items['Weak Health Potion']
                        self.map.update({'Weak Health Potion':weak_health_potion})
                        self.generate()

                    time.sleep(0.5)
                    print('You pull down the hatch to the attic and climb up.')
                    time.sleep(0.5)
                    print('The floor creaks as you step on the old, wooden floorboards.')

                    player.current_location = self
                

                def investigate(self,player):
                    time.sleep(0.5)
                    print('The large attic is illuminated by a single window.')
                    time.sleep(0.5)
                    print('The floor is littered with crates and boxes, mostly filled with junk.')
                    time.sleep(0.5)
                    print(colored('A few items stand out, however.','yellow'))
                    
                    if 'Master Bedroom Key' in self.map:
                        print('On the floor lies a key to the master bedroom.')
                        time.sleep(0.5)
                    
                    list_view = []

                    for thing in self.map:
                        list_view.append(thing)
                    
                    print('You see', list_view)



            attic = Attic('Attic')

            map = {'Attic':attic,}


            def enter(self,player):
                if len(player.command) > 1:
                    if player.command[1]=='upstairs':
                        print('You walk up the windy staircase to the third floor.')

                if not self.isGenerated:
                    downstairs = player.current_location

                    self.generate()
                    self.map.update({'Second Floor':downstairs})
                
                player.current_location = self
            

            def exit(self,player):
                time.sleep(0.5)
                print("You're on the third floor.")
                time.sleep(0.5)
                print('You decide not to jump out the window.')
                return False        


            def investigate(self,player):
                time.sleep(0.5)
                print('Paintings and tapestries line the walls.')
                time.sleep(0.5) 
                print('The hallway contain many doors.')
                time.sleep(0.5)
                print("There's a hatch on the ceiling that leads to the attic.")
                time.sleep(0.5)
                list_view = []
                for thing in self.map:
                    list_view.append(thing)
                print('You see', list_view)





        class MasterBedroom(location.Location):
            
            
            def enter(self,player):
                hasKey = False
                for slot in player.inventory:
                    if player.inventory[slot]=='Master Bedroom Key':
                        hasKey = True
                
                time.sleep(0.5)

                if not hasKey:
                    print('You try the red door.')
                    time.sleep(0.5)
                    print(colored("It's locked.", 'red'))
                    time.sleep(0.5)
                    print('You look through the key hole...')
                    time.sleep(0.5)
                    print('...')
                    time.sleep(0.5)
                    print('Something must be covering it.')
                    time.sleep(0.5)
                    print(colored('You hear quiet breathing from the other side.', 'red'))
                else:
                    print('You unlock the door.')
                    time.sleep(0.5)
                    print('The door flies open!')
                    time.sleep(0.5)
                    print(colored("A vampire! Don't let it bite you!",'red'))
                    time.sleep(0.5)
                    print(colored("You'll make a fine meal!", 'orange'))
                    time.sleep(0.5)
                    
                    # Vampire fight
                    import Enemies.vampire
                    class ManorVampire(Enemies.vampire.Vampire):
                        runDifficulty = 9999999

                        drops = ['']
                    
                    vampire = ManorVampire('Vampire')
                    vampire.ambience()
                    player.fight(vampire)

            def investigate(self,player):
                time.sleep(0.5)
                print('The opulent bedroom is filled with busts and portraits of the vampire.')
                time.sleep(0.5)
                print('It has no windows.')        
                time.sleep(0.5)

                list_view = []

                for thing in self.map:
                    list_view.append(thing)
                
                print('You see', list_view)
            

            def exit(self,player):
                
                print("You can't find an exit in here.")

                return False




        upstairs = ThirdFloor('Third Floor')
        master_bedroom = MasterBedroom('Master Bedroom')

        map = {
            'Third Floor':upstairs,
            'Master Bedroom':master_bedroom,
        }

        isLocked = False


        def exit(self,player):
            time.sleep(0.5)
            print("You're on the second floor.")
            time.sleep(0.5)
            print('You decide not to jump out the window.')
            return False


        def enter(self,player):
            time.sleep(0.5)
            print('You walk up the creaky steps to the second floor.')
            
            if not self.isGenerated:
                downstairs = player.current_location                

                self.map.update({'First Floor':downstairs})
                self.generate()
            
            player.current_location = self


        def investigate(self,player):
            time.sleep(0.5)
            print('Paintings and tapestries line the walls.')
            time.sleep(0.5)
            print('The hallway contain many doors, most of them locked.')
            time.sleep(0.5)
            print('One bright red door stands out in particular.')
            time.sleep(0.5)
            
            list_view = []
            for thing in self.map:
                list_view.append(thing)
            print('You see', list_view)


        def generate(self):
            self.isGenerated = True





    class Basement(location.Location):
        
        map = {}
        isLocked = False


        def enter(self,player):

            if not self.isGenerated:
                upstairs = player.current_location
                fiedler_manor_key = Items.items_registry.items['Fiedler Manor Key']

                self.map.update({'Fiedler Manor Key':fiedler_manor_key})
                self.map.update({'First Floor':upstairs})
                self.generate()
                
                print('You can barely see five feet in front of you as you walk down the dimly lit steps...')
                time.sleep(1.0)
                print('...')
                time.sleep(1.0)
                print(colored('You hear footsteps from upstairs...','red'))

                # Spawns a ghoul upstairs
                from Enemies import ghoul
                ghoul = ghoul.Ghoul('Ghoul')
                self.map['First Floor'].map.update({'Ghoul':ghoul})

            else:
                print('You go downstairs.')
                time.sleep(0.5)
                print('You can barely see anything.')

            player.current_location = self
        

        def exit(self,player):
            print("You can't find an exit from the basement.")
            return False


        def investigate(self,player):
            hasTorch = False
            
            if player.equipped['weapon']=='Torch':
                hasTorch = True
            
            if not hasTorch:
                print('You can barely see anything in this darkness.')
                time.sleep(0.5)
                print('The smell is unbearable down here.')
                time.sleep(0.5)
                print(colored('You feel like something is watching you...','red'))
                time.sleep(0.5)
                print('You wish you had a',colored('torch','yellow')+'...')
                time.sleep(0.5)
                print("You see ['First Floor']")
            
            else:
                print('You pull out your torch and look around...')
                time.sleep(0.5)
                print('...')
                time.sleep(0.5)
                print('You feel nauseous as you shine your torch on the blood-drained corpses that litter the room.')
                time.sleep(0.5)
                print('What kind of maniac would do something like this?')
                time.sleep(0.5)

                if 'Fiedler Manor Key' in self.map:
                    print('You see a',colored('key','yellow')+'!')
                
                list_view = []
                
                for thing in self.map:
                    list_view.append(thing)
                
                print('You see', list_view)





    class Kitchen(location.Location):

        map = {
            'Kitchen Knife':Items.items_registry.items['Kitchen Knife'],
            'Garlic':Items.items_registry.items['Garlic'],
        }


        def exit(self,player):
            print("You can't find an exit from the kitchen.")
            time.sleep(0.5)
            return False


        def enter(self,player):
            print('You enter the kitchen')
            
            if not self.isGenerated:
                entrance = player.current_location
                self.map.update({'Entrance':entrance})
                self.generate()

            player.current_location = self


        def investigate(self,player):
            time.sleep(0.5)
            print('You stomach groans as you look around.')
            time.sleep(0.5)
            print('The large kitchen contains a wide variety of cooking ingredients.')
            time.sleep(0.5)
            print('From artichoke to human flesh, the kitchen contains almost everything.')
            time.sleep(0.5)
            
            list_view = []
            for thing in self.map:
                list_view.append(thing)
            print('You see', list_view)   





    # First Floor

    upstairs = SecondFloor('Second Floor')
    basement = Basement('Basement')
    kitchen = Kitchen('Kitchen')
    isLocked = False
    
    map = {
        'Second Floor':upstairs,
        'Basement':basement,
        'Kitchen':kitchen,
        'Torch':Items.items_registry.items['Torch'],
    }
    

    def discover(self):
        print('You see an ominious house in the distance.')
        time.sleep(0.5)
        print('As you approach, you begin a sense of dread washes over you...')
        time.sleep(0.5)

    
    # First Floor Enter
    def enter(self,player):

        if not self.isGenerated:
            
            time.sleep(0.5)
            print('You walk up to the entrance.')
            time.sleep(0.5)
            print('You take a deep breath and enter through the front door.')
            time.sleep(0.5)
            print(colored('The door slams behind you.', 'red'))

            self.isLocked = True
            self.generate()
        else:
            # Ghoul fight
            if 'Ghoul' in self.map:
                
                ghoul = self.map['Ghoul']
                ghoul.ambience()
                player.fight(ghoul)

            if player.command[1]=='first floor':
                print('You walk to the first floor.')
            
            elif player.command[1]=='entrance':
                print('You walk to the entrance.')
        
        player.current_location = self
    
    
    def exit(self,player):
        
        for slot in player.inventory:
            
            if player.inventory[slot] == 'Fiedler Manor Key':
                self.isLocked = False
                break
                
        if self.isLocked:
            print('You try the door.')
            time.sleep(0.5)
            print(colored("It's locked.",'red'))
            return False
        
        else:
            print('You unlock the door and exit.')
            return True
    

    def investigate(self,player):
        time.sleep(0.5)
        print('The manor is in surpisingly good condition.')
        time.sleep(0.5)
        print('A staircase lies in front of the door.')
        time.sleep(0.5)
        print('Old paintings, tapestries, and torches line the walls.')
        time.sleep(0.5)
        print('You feel uncomfortable being in here.')
        time.sleep(0.5)
        list_view = []
        for thing in self.map:
            list_view.append(thing)
        print('You see', list_view)