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

import wget
import json
import os

config = {
    # This is the gender type of the rooms counted -- [Male, Female, Neutral, All]
    'gender': 'All',
    # This is the type of rooms counted -- [Double, Triple, Quad, Suite, All]
    'capacity': 'All',
    # This will toggle the printing of the individual beds -- [True, False]
    'beds': True
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


def printRoomData():
    for name, data in dorms.items():
        print(f"{name}\t{len(data)}")
        if config['beds']:
            print(f"Rooms: [{', '.join(i['RoomNumber'] for i in data)}]\n")


with open('FreeRooms.json') as json_file:
    data = json.load(json_file)

    for entry in data:
        if (config['gender'] == entry['Gender'] or config['gender'] == 'All') or (config['capacity'] == entry['Capacity'] or config['capacity'] == 'All'):
            checkRoom(entry)

    print(f"\nUpdated on: {data[0]['LastUpdated']}\nUsing config: {config}\n")
    printRoomData()