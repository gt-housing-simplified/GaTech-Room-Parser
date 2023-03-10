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
#   -g <Male, Female, Neutral, All, Dynamic>
#
# Capacity (Room Type):
#   -c <Double, Triple, Quad, Suite, 2 person, 4 person, 6 person, All>
#
# bed_empty (Beds in room for -e and -er to be true):
#   -C <int>
#
# List Empty Rooms:
#   1. -e   (will list just the empty room count)
#   2. -er  (will list both the count and the room names)
#
# List Bed Names:
#   -b
#
# Output to a File: ! WIP -- DO NOT USE !
#   -fo
#
# Run Silently (Use w/ -fo):
#   -s

from tabulate import tabulate
import wget
import json
import os
import sys
import time

# This config is only for defaults.
config = {
    "gender": "All",
    "capacity": "All",
    "bed_empty": 0,
    "empty": False,
    "rooms": False,
    "beds": False,
    "file_output": False,
    "silent": False,
}

# This is the json API url
url = f"https://housing.gatech.edu/available-rooms-dir/FreeRooms.json?_={round(time.time()*1000)}"
try:
    os.remove("FreeRooms.json")
except:
    pass
filename = wget.download(url)
print()

dorms, empty = {}, {}

final_file_table = []


def checkRoom(room):
    buildingName = room["BuildingName"]
    if not dorms.get(buildingName):
        dorms[buildingName] = []
    dorms[buildingName].append(room)


def getRoom(room_type, room, truncate=1):
    empty[room_type][0].append(room)
    empty[room_type][1].add(room[:-truncate])


def getEmpty(rooms, bed_letters):
    empty_list = []
    for room in rooms[1]:
        if (
            sum(bed in rooms[0] for bed in (room + bed_i for bed_i in bed_letters))
            >= config["bed_empty"]
        ):
            empty_list.append(room)

    return empty_list


def printRoomData(data):
    global final_file_table

    tableDorms, beds, empty_counts, rooms = [], [], [], []

    for name, data in dorms.items():
        tableDorms.append([name, len(data)])

        if config["empty"] or config["rooms"]:
            global empty  # need to change

            empty = {
                k: ([], set())
                for k in [
                    "Double",
                    "Triple",
                    "Quad",
                    "Suite Room",
                    "Suite",
                    "2 person",
                    "3 person",
                    "4 person",
                    "4 person short",
                    "5 person",
                    "6 person",
                    "7 person",
                ]
            }

            for room in data:
                if room["Capacity"] == "Suite":
                    getRoom("Suite Room", room["RoomNumber"])
                    getRoom("Suite", room["RoomNumber"], truncate=2)
                else:
                    getRoom(room["Capacity"], room["RoomNumber"])

            empty["Double"] = getEmpty(empty["Double"], ["a", "b"])
            empty["Triple"] = getEmpty(empty["Triple"], ["a", "b", "c"])
            empty["Quad"] = getEmpty(empty["Quad"], ["a", "b", "c", "d"])
            empty["Suite Room"] = getEmpty(empty["Suite Room"], ["a", "b"])
            empty["Suite"] = getEmpty(empty["Suite"], ["Aa", "Ab", "Ba", "Bb"])
            empty["2 person"] = getEmpty(empty["2 person"], ["A", "B"])
            empty["3 person"] = getEmpty(empty["3 person"], ["A", "B", "C"])
            empty["4 person"] = getEmpty(empty["4 person"], ["A", "B", "C", "D"])
            empty["4 person short"] = getEmpty(
                empty["4 person short"], ["A", "B", "C", "D"]
            )
            empty["5 person"] = getEmpty(empty["5 person"], ["A", "B", "C", "D", "E"])
            empty["6 person"] = getEmpty(
                empty["6 person"], ["A", "B", "C", "D", "E", "F"]
            )
            empty["7 person"] = getEmpty(
                empty["7 person"], ["A", "B", "C", "D", "E", "F", "G"]
            )

            empty = {room_type: rooms for room_type, rooms in empty.items() if rooms}
            empty_count = {room_type: len(rooms) for room_type, rooms in empty.items()}

            empty_counts.append(empty_count)
            rooms.append(empty)

        if config["beds"]:
            beds.append([i["RoomNumber"] for i in data])

    if config["empty"] or config["rooms"] or config["beds"]:
        for i in range(len(tableDorms)):
            print(tableDorms[i][0])
            table = [["Beds Left", tableDorms[i][1]]]
            if config["beds"]:
                table.append(["", ", ".join(beds[i])])
            if config["empty"]:
                table.append(
                    [
                        "Empty Rooms",
                        ", ".join(
                            [
                                f"{count} {room_type}s"
                                for room_type, count in empty_counts[i].items()
                            ]
                        ),
                    ]
                )
            if config["rooms"]:
                for rooms_per_type in [
                    f"{room_type}s: {', '.join(rms)}"
                    for room_type, rms in rooms[i].items()
                ]:
                    table.append(["", rooms_per_type])

            if config["file_output"]:
                # final_file_table.append([tableDorms[i][0]])
                final_file_table.extend(table)
            else:
                print(tabulate(table, maxcolwidths=[None, 150]))
                print()
    else:
        if config["file_output"]:
            final_file_table.extend(tableDorms)
        else:
            print(tabulate(tableDorms, headers=["Dorm", "Beds Left"]))


def main():
    global final_file_table

    if config["file_output"]:
        tabulate.PRESERVE_WHITESPACE = True
        with open("output.html", "w") as f:
            f.write("")
            f.close()

    with open("FreeRooms.json") as json_file:
        data = json.load(json_file)
        length = len(data)

        for i in range(0, length):
            if (
                config["gender"] != data[i]["Gender"]
                and config["gender"] != "All"
                and data[i]["Gender"] != "Dynamic"
            ) or (
                config["capacity"] != data[i]["Capacity"]
                and config["capacity"] != "All"
            ):
                continue
            checkRoom(data[i])

        if not config["silent"]:
            print(
                "\nUpdated on: " + data[0]["LastUpdated"] + "\nUsing Config: ", end=""
            )
            print(config)
            print()
            printRoomData(final_file_table)
        else:
            print("Updated on: " + data[0]["LastUpdated"])

    if config["file_output"]:
        with open("output.html", "a") as f:
            if config["empty"] or config["rooms"] or config["beds"]:
                f.write(
                    tabulate(
                        final_file_table, maxcolwidths=[None, 150], tablefmt="html"
                    )
                )
            else:
                f.write(
                    tabulate(
                        final_file_table, headers=["Dorm", "Beds Left"], tablefmt="html"
                    )
                )
            f.close()


if __name__ == "__main__":
    try:
        if "-g" in sys.argv:
            config["gender"] = sys.argv[sys.argv.index("-g") + 1]
        if "-c" in sys.argv:
            config["capacity"] = sys.argv[sys.argv.index("-c") + 1]
        if "-C" in sys.argv:
            config["bed_empty"] = int(sys.argv[sys.argv.index("-C") + 1])
        if "-e" in sys.argv:
            config["empty"] = True
        if "-er" in sys.argv:
            config["empty"] = True
            config["rooms"] = True
        if "-b" in sys.argv:
            config["beds"] = True
        if "-fo" in sys.argv:
            config["file_output"] = True
        if "-s" in sys.argv:
            config["silent"] = True
    except IndexError:
        raise Exception("Invalid Command Line Arguments")

main()
