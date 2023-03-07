from . import location
class Wilderness(location.Location):
  def exit(self,player):
    self.map = {}
    return True
