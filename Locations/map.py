import random
from . import rome,abandoned_house,wilderness,suspicious_cave,fiedler_manor

# Minor Locations
abandoned_house = abandoned_house.AbandonedHouse('Abandoned House')
suspicious_cave = suspicious_cave.SuspiciousCave('Suspicious Cave')
ancora_wilderness_places = (abandoned_house, )

# Major Locations
fiedler_manor = fiedler_manor.FiedlerManor('Fiedler Manor')
rome = rome.Rome('Rome')
wilderness = wilderness.Wilderness('The Wilderness')

ancora_minor_locations = {
  'Abandoned House':abandoned_house,
  'Suspicious Cave':suspicious_cave,
}

# The entire world
map = {
  'Ancora':{
    
    'The Wilderness':wilderness,

    'Rome':rome,

    'Minor':ancora_minor_locations,
    
    #'Castle Vantress':{},

    'Fiedler Manor':fiedler_manor,
  },
  'Mordor':{
    'Barad Dur':None,

    "Hell's Portal":None,

    'Mount Doom':None,

    'The Black Gate':None,
  },
  'Hell':{
    'Hell City':None,
    
    'Portal':None,

    "Dante's Inferno":None,

    'Nine Circles':None,
  },
}

def random_location(player):
  die = random.randint(1,6)

  #return (ancora_abandoned_house)
  if die>0:
    places = []
    for place in map[player.current_region]:
      places.append(place)

    
    place = random.choice(places)
    if place == 'Minor' or place == 'The Wilderness':
      location = random.choice(list(map[player.current_region]['Minor'].values()))
      return location
    elif place not in player.discovered_areas:
      player.discovered_areas.append(place)
      return map[player.current_region][place]
    else:
      location = random.choice(list(map[player.current_region]['Minor'].values()))
      return location

  else:
    if player.current_region=='Ancora':
      return (abandoned_house)
