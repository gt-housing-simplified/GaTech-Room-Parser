import wget, json, os

config = {
  'gender': 'Male', # This is the gender type of the rooms counted
  'capacity': 'Double', # This is the type of rooms counted
  'beds': False # This will toggle the printing of the individual beds
}

# This is the json API url
url = 'https://housing.gatech.edu/rooms/FreeRooms.json?_=1655904358700'
os.remove('FreeRooms.json') 
filename = wget.download(url); print()

Fitten = []
Glenn = []
Towers = []
Montag = []
Freeman = []
Harrison = []
Hefner = []
Armstrong = []
Field = []
Hopkins = []
Hanson = []
WoodruffS = []
WoodruffN = []

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

with open('FreeRooms.json') as json_file:
  data = json.load(json_file)
  length = len(data)

  for i in range(0,length):
    if config['gender'] != data[i]['Gender'] or config['capacity'] != data[i]['Capacity']:
      continue
    checkRoom(data[i])
  
  print("\n" + data[0]['LastUpdated'] + "\n")
  printRoomData()





      

