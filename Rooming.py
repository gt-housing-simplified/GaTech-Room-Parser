import wget, json, os

config = {
  'gender': 'Male',
  'capacity': 'Double',
  'rooms': False
}

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

  print("Fitten: ", len(Fitten))
  if config['rooms']:
    for i in Fitten:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Glenn: ", len(Glenn))
  if config['rooms']:
    tempList.clear()
    for i in Glenn:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Towers: ", len(Towers))
  if config['rooms']:
    tempList.clear()
    for i in Towers:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Montag: ", len(Montag))
  if config['rooms']:
    tempList.clear()
    for i in Montag:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Freeman: ", len(Freeman))
  if config['rooms']:
    tempList.clear()
    for i in Freeman:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Harrison: ", len(Harrison))
  if config['rooms']:
    tempList.clear()
    for i in Harrison:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hefner: ", len(Hefner))
  if config['rooms']:
    tempList.clear()
    for i in Hefner:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Armstrong: ", len(Armstrong))
  if config['rooms']:
    tempList.clear()
    for i in Armstrong:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Field: ", len(Field))
  if config['rooms']:
    tempList.clear()
    for i in Field:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hopkins: ", len(Hopkins))
  if config['rooms']:
    tempList.clear()
    for i in Hopkins:
      tempList.append(i['RoomNumber'])
    print(tempList)

  print("Hanson: ", len(Hanson))
  if config['rooms']:
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
  
  printRoomData()





      

