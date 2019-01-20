from CYOA.Room import Room
from CYOA.Item import Item

dining_room = Room("Dining Room")
family_room = Room("Family Room")
kitchen = Room("Kitchen")

def stay_in_bed():
    print("You stayed in bed and call for your mom to get you breakfast.")
    
def create_kitchen():
    kitchen.north = dining_room
    kitchen.west = family_room
    newspaper = Item("Newspaper", kitchen)
    kitchen.items.append(newspaper)
    
def create_dining_room():
    dining_room.south = kitchen

def create_family_room():
    family_room.east = kitchen

def look(room):
    for item in room.items:
        print (item)
    
def main():
    create_dining_room()
    create_family_room()
    create_kitchen()
    
    print("Welcome to my escape room!")
    
    print(kitchen)
    look(kitchen)
    print("You find yourself in the kitchen. What would you like to do?")
    if (input("You wake up. Do you stay in BED or GET UP?") == "bed"):
        stay_in_bed()
    else:
        print("You got up")

if __name__ == "__main__":
    main()    