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

import wget, json, os

config = {
  'gender': 'All', # This is the gender type of the rooms counted -- [Male, Female, Neutral, All]
  'capacity': 'All', # This is the type of rooms counted -- [Double, Triple, Quad, Suite, All]
  'beds': False # This will toggle the printing of the individual beds -- [True, False]
}

# This is the json API url
url = 'https://housing.gatech.edu/rooms/FreeRooms.json?_=1655904358700'
try:
  os.remove('FreeRooms.json') 
except:
  pass
filename = wget.download(url); print()

Fitten = []
Glenn = []
Towers = []
Montag = []
Freeman = []
Harrison = []
Folk = []
Hefner = []
Armstrong = []
Field = []
Hopkins = []
Hanson = []
WoodruffS = []
WoodruffN = []
Smith = []
Brown = []
Caldwell = []

def checkRoom(room):
  buildingName = room['BuildingName'] 
  match buildingName.replace(' ', ''):
      case 'Fitten':
        Fitten.append(room)
        return True
      case 'Glenn':
        Glenn.append(room)
        return True
      case 'Towers':
        Towers.append(room)
        return True
      case 'Montag':
        Montag.append(room)
        return True
      case 'Freeman':
        Freeman.append(room)
        return True
      case 'Harrison':
        Harrison.append(room)
        return True
      case 'Folk':
        Folk.append(room)
        return True
      case 'Hefner':
        Hefner.append(room)
        return True
      case 'Armstrong':
        Armstrong.append(room)
        return True
      case 'Field':
        Field.append(room)
        return True
      case 'Hopkins':
        Hopkins.append(room)
        return True
      case 'Hanson':
        Hanson.append(room)
        return True
      case 'WoodruffSouth':
        WoodruffS.append(room)
        return True
      case 'WoodruffNorth':
        WoodruffN.append(room)
        return True
      case 'Smith':
        Smith.append(room)
        return True
      case 'Brown':
        Brown.append(room)
        return True
      case 'Caldwell':
        Caldwell.append(room)
        return True
      case _:
        return False

def printRoomData():
  tempList = []

  print("Fitten:\t\t", len(Fitten)) #, "\t/ 64")
  if config['beds']:
    for i in Fitten:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Glenn:\t\t", len(Glenn)) #, "\t/ 176")
  if config['beds']:
    tempList.clear()
    for i in Glenn:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Towers:\t\t", len(Towers)) #, "\t/ 151")
  if config['beds']:
    tempList.clear()
    for i in Towers:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Montag:\t\t", len(Montag)) #, "\t/ 34")
  if config['beds']:
    tempList.clear()
    for i in Montag:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Freeman:\t", len(Freeman)) #, "\t/ 30")
  if config['beds']:
    tempList.clear()
    for i in Freeman:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Harrison:\t", len(Harrison)) #, "\t/ 102")
  if config['beds']:
    tempList.clear()
    for i in Harrison:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Folk:\t\t", len(Folk)) #, "\t/ 30")
  if config['beds']:
    tempList.clear()
    for i in Folk:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hefner:\t\t", len(Hefner)) #, "\t/ 70")
  if config['beds']:
    tempList.clear()
    for i in Hefner:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Armstrong:\t", len(Armstrong)) #, "\t/ 36")
  if config['beds']:
    tempList.clear()
    for i in Armstrong:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Field:\t\t", len(Field)) #, "\t/ 60")
  if config['beds']:
    tempList.clear()
    for i in Field:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hopkins:\t", len(Hopkins)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in Hopkins:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hanson:\t\t", len(Hanson)) #, "\t/ 84")
  if config['beds']:
    tempList.clear()
    for i in Hanson:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Woodruff South:\t", len(WoodruffS)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in WoodruffS:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Woodruff North:\t", len(WoodruffN)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in WoodruffN:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Smith:\t\t", len(Smith)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in Smith:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Brown:\t\t", len(Brown)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in Brown:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Caldwell:\t", len(Caldwell)) #, "\t/ 64")
  if config['beds']:
    tempList.clear()
    for i in Caldwell:
      tempList.append(i['RoomNumber'])
    print(tempList)

with open('FreeRooms.json') as json_file:
  data = json.load(json_file)
  length = len(data)

  for i in range(0,length):
    if (config['gender'] != data[i]['Gender'] and config['gender'] != 'All') or (config['capacity'] != data[i]['Capacity'] and config['capacity'] != 'All'):
      continue
    checkRoom(data[i])
  
  print("\nUpdated on: " + data[0]['LastUpdated'] + "\nUsing Config: ", end = "")
  print(config); print()
  printRoomData()





      

