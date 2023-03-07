import random,time

class Location:
  map = {}
  isGenerated = False


  # Called whenever a player takes an item from the map
  def takeItem(self,player):
    pass


  # Randomly generates what's nearby
  def generate(self):
    self.isGenerated=True


  # Called whenenver you enter the place
  def enter(self,player):
    if player.current_location != None:
      player.current_location.exit(player)
      
    print('You appear lost.')
    if not self.isGenerated:
      self.generate()
    player.current_location = self
  

  # Called whenever you exit. Returns True if you can exit
  # Look at fiedler_manor.py for example if you can't exit
  def exit(self,player):
    print('You exit the ' + self.name + '.')
    player.current_location = None
    player.location = ''
    player.last_location = self.name
    return True


  # Called in player.explore() when you discover the place
  def discover(self,player):
    
    if self.name[0:1].lower()=='a'or self.name[0:1].lower()=='e'or self.name[0:1].lower()=='i'or self.name[0:1].lower()=='o'or self.name[0:1].lower()=='u':
      print('You discover an ' + self.name + '.')
    
    else:
      print('You discover a ' + self.name + '.')

  # Called whenever you investigate a location
  def investigate(self, player):
    view_list = []
    for thing in self.map:
      view_list.append(thing)
    print('You see ' + str(view_list))


  def __init__(self, name):
    self.name = name
