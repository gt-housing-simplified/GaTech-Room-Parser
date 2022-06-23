# Designed by Ian Boraks
# https://github.com/Ian-Boraks/GaTech-Room-Parser
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# To set up the config, use the following command line arguments:
# Gender:
#   -g <Male, Female, Neutral, All>
#
# Capacity (Room Type):
#   -c <Double, Triple, Quad, Suite, 2 person, 4 person, 6 person, All>
#
# List Empty Rooms:
#   1. -e   (will list just the empty room count)
#   2. -er  (will list both the count and the room names)
#
# List Bed Names:
#   -b
#
# Output to a CSV File: ! WIP -- DO NOT USE !
#   -csv
#
# Run Silently (Use w/ -csv):
#   -s

from tabulate import tabulate
import wget
import json
import os
import sys

# This config is only for defaults.
config = {
  'gender': 'All',
  'capacity': 'All',
  'empty': False,
  'rooms': False,
  'beds': False,
  'csv': False,
  'silent': False
}

# This is the json API url
url = 'https://housing.gatech.edu/rooms/FreeRooms.json?_=1655904358700'
try:
  os.remove('FreeRooms.json')
except:
  pass
filename = wget.download(url)
print()

dorms, empty = {}, {}


def checkRoom(room):
  buildingName = room['BuildingName']
  if not dorms.get(buildingName):
    dorms[buildingName] = []
  dorms[buildingName].append(room)


def getRoom(room_type, room, truncate=1):
  empty[room_type][0].append(room)
  empty[room_type][1].add(room[:-truncate])


def getEmpty(rooms, bed_letters):
  empty_list = []
  for room in rooms[1]:
    if all(bed in rooms[0] for bed in (room + bed_i for bed_i in bed_letters)):
        empty_list.append(room)
  return empty_list


def printRoomData(data):
  tableDorms, beds, empty_counts, rooms = [], [], [], []

  for name, data in dorms.items():
    tableDorms.append([name, len(data)])

    if config['empty'] or config['rooms']:
        global empty  # need to change

        empty = {k: ([], set()) for k in ['Double', 'Triple', 'Quad', 'Suite Room', 'Suite', '2 person', '4 person', '6 person']}

        for room in data:
          if room['Capacity'] == 'Suite':
              getRoom('Suite Room', room['RoomNumber'])
              getRoom('Suite', room['RoomNumber'], truncate=2)
          else:
              getRoom(room['Capacity'], room['RoomNumber'])

        empty['Double'] = getEmpty(empty['Double'], ['a', 'b'])
        empty['Triple'] = getEmpty(empty['Triple'], ['a', 'b', 'c'])
        empty['Quad'] = getEmpty(empty['Quad'], ['a', 'b', 'c', 'd'])
        empty['Suite Room'] = getEmpty(empty['Suite Room'], ['a', 'b'])
        empty['Suite'] = getEmpty(empty['Suite'], ['Aa', 'Ab', 'Ba', 'Bb'])
        empty['2 person'] = getEmpty(empty['2 person'], ['A', 'B'])
        empty['4 person'] = getEmpty(empty['4 person'], ['A', 'B', 'C', 'D'])
        empty['6 person'] = getEmpty(empty['6 person'], ['A', 'B', 'C', 'D', 'E', 'F'])

        empty = {room_type: rooms for room_type, rooms in empty.items() if rooms}
        empty_count = {room_type: len(rooms) for room_type, rooms in empty.items()}

        empty_counts.append(empty_count)
        rooms.append(empty)
        # need to make more readable

    if config['beds']:
        beds.append(f"Available Beds: [{', '.join(i['RoomNumber'] for i in data)}]")

  if config['beds'] or config['empty']:
    for i in range(len(tableDorms)):
        print(tabulate([tableDorms[i]], headers=['Dorm', 'Beds Left']))
        if config['empty']:
          print(f"Empty Room Count: {empty_counts[i]}")
        if config['rooms']:
          print(f"Empty Rooms: {rooms[i]}")
        if config['beds']:
          print(beds[i])
        print()
  else:
    print(tabulate(tableDorms, headers=['Dorm', 'Beds Left']))


# def exportRoomData(data):
#   try:
#     open('BedOverTime.csv', 'x')
#   except FileExistsError:
#     pass
#   with open('BedOverTime.csv', 'r+t') as f:
#     try:
#         lastTime = f.readlines()[-1][:19]
#         if lastTime == data[0]['LastUpdated']:
#           return
#     except IndexError:
#         f.write(
#           'LastUpdated,Fitten,Glenn,Towers,Montag,Freeman,Harrison,Folk,Hefner,Armstrong,Field,Hopkins,Hanson,Woodruff South,Woodruff North,Smith,Brown,Caldwell\n')
#         pass

#     f.write(data[0]['LastUpdated'] + ',' + str(len(Fitten)) + ',' + str(len(Glenn)) + ',' + str(
#         len(Towers)) + ',' + str(len(Montag)) + ',' + str(len(Freeman)) + ',' + str(len(Harrison)) + ',' + str(
#         len(Folk)) + ',' + str(len(Hefner)) + ',' + str(len(Armstrong)) + ',' + str(len(Field)) + ',' + str(
#         len(Hopkins)) + ',' + str(len(Hanson)) + ',' + str(len(WoodruffS)) + ',' + str(len(WoodruffN)) + ',' + str(
#         len(Smith)) + ',' + str(len(Brown)) + ',' + str(len(Caldwell)) + '\n')

def main():
  if config['csv']:
    config['gender'] = 'All'
    config['capacity'] = 'All'

  with open('FreeRooms.json') as json_file:
    data = json.load(json_file)
    length = len(data)

    for i in range(0, length):
      if (config['gender'] != data[i]['Gender'] and config['gender'] != 'All') or (
          config['capacity'] != data[i]['Capacity'] and config['capacity'] != 'All'):
        continue
      checkRoom(data[i])

    if not config['silent']:
      print("\nUpdated on: " + data[0]['LastUpdated'] + "\nUsing Config: ", end="")
      print(config);
      print()
      printRoomData(data)
    else:
      print("Updated on: " + data[0]['LastUpdated'])

    # if config['csv']:
    #   exportRoomData(data)


if __name__ == "__main__":
  try:
    if ('-g' in sys.argv):
      config['gender'] = sys.argv[sys.argv.index('-g') + 1]
    if ('-c' in sys.argv):
      config['capacity'] = sys.argv[sys.argv.index('-c') + 1]
    if ('-e' in sys.argv):
      config['empty'] = True
    if ('-er' in sys.argv):
      config['empty'] = True
      config['rooms'] = True
    if ('-b' in sys.argv):
      config['beds'] = True
    if ('-csv' in sys.argv):
      config['csv'] = True
    if ('-s' in sys.argv):
      config['silent'] = True
  except IndexError:
    raise Exception('Invalid Command Line Arguments')

main()
