# Designed by Ian Boraks
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH
# THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Needs python version >=3.10.0
# This is because of the use of match statements in the checkRoom() function

from tabulate import tabulate
import wget
import json
import os

config = {
  # This is the gender type of the rooms counted -- [Male, Female, Neutral, All]
  'gender': 'All', 
  # This is the type of rooms counted -- [Double, Triple, Quad, Suite, All]
  'capacity': 'All',
  # This will toggle the printing of the individual beds -- [True, False] 
  'beds': True, 
  # ! WIP -- Keep at False ! This will toggle the export to the csv file -- [True, False] 
  'csv': False, 
  # This will toggle the printing of the room data -- [True, False]
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

dorms = {}

def checkRoom(room):
  buildingName = room['BuildingName']
  if not dorms.get(buildingName):
    dorms[buildingName] = []
  dorms[buildingName].append(room)


def printRoomData(data):
  tableDorms = []
  beds = []
  for name, data in dorms.items():
    tableDorms.append([name, len(data)])
    beds.append(f"Rooms: [{', '.join(i['RoomNumber'] for i in data)}]")
  if config['beds']:   
    for i in range(0,len(tableDorms)):
      print(tabulate([tableDorms[i]], headers = ['Dorm', 'Beds Left']))
      print(beds[i] + '\n')
  else:
    print(tabulate(tableDorms, headers = ['Dorm', 'Beds Left'])) 

def exportRoomData(data):
  try:
    open('BedOverTime.csv', 'x')
  except FileExistsError:
    pass
  with open('BedOverTime.csv','r+t') as f:
    try:
      lastTime = f.readlines()[-1][:19]
      if lastTime == data[0]['LastUpdated']:
        return
    except IndexError:
      f.write('LastUpdated,Fitten,Glenn,Towers,Montag,Freeman,Harrison,Folk,Hefner,Armstrong,Field,Hopkins,Hanson,Woodruff South,Woodruff North,Smith,Brown,Caldwell\n')
      pass

    f.write(data[0]['LastUpdated'] + ',' + str(len(Fitten)) + ',' + str(len(Glenn)) + ',' + str(len(Towers)) + ',' + str(len(Montag)) + ',' + str(len(Freeman)) + ',' + str(len(Harrison)) + ',' + str(len(Folk)) + ',' + str(len(Hefner)) + ',' + str(len(Armstrong)) + ',' + str(len(Field)) + ',' + str(len(Hopkins)) + ',' + str(len(Hanson)) + ',' + str(len(WoodruffS)) + ',' + str(len(WoodruffN)) + ',' + str(len(Smith)) + ',' + str(len(Brown)) + ',' + str(len(Caldwell)) + '\n')

def __main__():
  if config['csv']:
    config['gender'] = 'All'
    config['capacity'] = 'All'

  with open('FreeRooms.json') as json_file:
    data = json.load(json_file)
    length = len(data)

    for i in range(0,length):
      if (config['gender'] != data[i]['Gender'] and config['gender'] != 'All') or (config['capacity'] != data[i]['Capacity'] and config['capacity'] != 'All'):
        continue
      checkRoom(data[i])
    
    if not config['silent']:
      print("\nUpdated on: " + data[0]['LastUpdated'] + "\nUsing Config: ", end = "")
      print(config); print()
      printRoomData(data)
    else:
      print("Updated on: " + data[0]['LastUpdated'])

    if config['csv']:
      exportRoomData(data)
    
    exit()

__main__()