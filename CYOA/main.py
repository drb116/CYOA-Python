from CYOA.Room import Room
from CYOA.Item import Item
from _operator import inv


dining_room = Room("Dining Room")
family_room = Room("Family Room")
kitchen = Room("Kitchen")
inventory = {}
solved=False

def stay_in_bed():
    print("You stayed in bed and call for your mom to get you breakfast.")
    
def create_kitchen():
    kitchen.north = dining_room
    kitchen.west = family_room
    
    newspaper = Item("Newspaper", kitchen)
    newspaper.lookat = "It is part of today's newspaper. There is an article " \
    "about Martin Luther King. It says that\nhis birthday is always celebrated on " \
    "the the 3rd Monday of the 1st Month."
    newspaper.use = "You read the news. Trump is still president. Oh well."
    newspaper.lookunder = "Nothing under the paper exceptt he table it is on."
    kitchen.items["newspaper"] = newspaper
    
    faucet = Item("Faucet", kitchen)
    faucet.lookat = "There is a faucet over the sink."
    faucet.use = "You turn the faucet on and water comes out."
    faucet.lookunder = "I'm not exactly sure how to look under the faucet."
    kitchen.items["faucet"] = faucet
    
    table = Item("Table", kitchen)
    table.lookat = "There is a glass table with a newspaper on top of it."
    table.use = "The table is doing a good job holding up the paper. I am not sure there "\
    "is anything else to do with it."
    table.lookunder = "There are a few old pieces of food on the table. Maybe they should get a dog."
    kitchen.items["table"] = table
    
def create_dining_room():
    dining_room.south = kitchen
    
    table = Item("Table", dining_room)
    table.lookat = "There is a wood table. Something appears to be carved in it."
    table.use = "When you look closer at the table, you see a heart and with three letters carved in it:\n"\
    "   xxx   xxx   \n xx   x x   xx \nx      x      x\n x   P.D.M   x \n  x         x  \n"\
    "    x     x    \n      x x      \n       x       \n"
    table.lookunder = "There are a few dust bunnies under the table. Where Roomba when you need it!"
    dining_room.items["table"] = table
    
    rug = Item("Rug", dining_room)
    rug.lookat = "There is a rug under the dining room table. There appears to be a "\
    "bulge under the corner."
    rug.use = "The rug feels nice on your feet, but doesn't do much else."
    rug.lookunder = "You look under the rug and find a dirty piece of plastic. It looks like "\
    "there is something written on it, but you can't read\nit through all the dirt. You pick "\
    "it up and take it with you."
    dining_room.items["rug"] = rug
    
    dirty_plastic = Item("Dirty Piece of plastic", dining_room)
    dirty_plastic.visible=False
    dirty_plastic.lookat = "It is a dirty piece of plastic. "
    dirty_plastic.use = "You can't use the plastic because it is too dirty"
    dirty_plastic.lookunder = "Yep, it is thin piece of plastic. Nothing but air under there."
    dining_room.items["dirtyplastic"] = dirty_plastic
    
    clean_plastic = Item("Clean Piece of plastic", dining_room)
    clean_plastic.visible=False
    clean_plastic.lookat = "It is a clean piece of plastic. There is some writing on it."
    clean_plastic.use = "You look closely and see the a capital V written on it."
    clean_plastic.lookunder = "Yep, it is thin piece of plastic. Nothing but air under there."
    dining_room.items["cleanplastic"] = clean_plastic
    

def create_family_room():
    family_room.east = kitchen
    door = Item("Door", family_room)
    door.lookat = "The door is locked from the inside, this appears to be your exit out."
    door.lookunder = "Its a door. You can't look under it."
    door.use = "The door is locked. You need a key to use it."
    family_room.items["door"] = door
    
    picture = Item("Picture", family_room)
    picture.lookat = "It is a nice picture of some dogs playing poker."
    picture.lookunder = "You look under the picture and find a hidden vault. There is a combo lock on it. To try the lock,\n"\
    "use the command enter combo.\n"
    picture.use = "Its a picture. Just look at it."
    family_room.items["picture"] = picture
    
    key = Item("Key", family_room)
    key.visible=False
    key.lookat = "It looks like a standard key to the door."
    key.use = "You use the key on the door. It opens! Congratulations you have escaped the room!"
    key.lookunder = "You look on the back of the key and see two letters written on a piece of masking tape: F.R."
    family_room.items["key"] = key

def look(room):
    for key,value in room.items.items():
        if (value.visible):
            print (value)
    for key,value in inventory.items():
        print ("You have a " + value.name)

def try_combo():
    first = input("Enter the first number: ")
    second = input("Enter the second number: ")
    third = input("Enter the third number: ")
    #PDM
    if (first == "5" and second=="3" and third=="1"):
        print("The combo worked! The safe opens and inside you find a key. You pick up the key and put it in your inventory.")
        inventory["key"] = family_room.items.get("key")
    else:
        print("Wrong combo. Try again.")
    
def action(room, item, command):
    if (item in room.items):
        if (command=="lookat"):
            print(room.items.get(item).lookat)
        elif (command=="use"):
            print(room.items.get(item).use)
        elif (command=="lookunder"):
            print(room.items.get(item).lookunder)
        else:
            print("I am not sure what you want me to do with the " + item + ".")
        
        #Special cases
        if (item=="key" and command=="use"):
            solved=True
        if (item=="rug" and command=="lookunder"):
            inventory["dirtyplastic"] = dining_room.items.get("dirtyplastic")
        if (item=="faucet" and command=="use" and ("dirtyplastic" in inventory)):
            del inventory["dirtyplastic"]
            inventory["cleanplastic"] = dining_room.items.get("cleanplastic")
            print("The faucet cleans the plastic off. You now have a clean plastic in your inventory.")
    elif (item in inventory):
        if (command=="lookat"):
            print(inventory.get(item).lookat)
        elif (command=="use"):
            print(inventory.get(item).use)
        elif (command=="lookunder"):
            print(inventory.get(item).lookunder)
        else:
             print("I am not sure what you want me to do with the " + item + ".")
    else:
        print("I don't see a " + item + ".")
        
def main():
    create_dining_room()
    create_family_room()
    create_kitchen()
    location = kitchen
    
    print("Welcome to my escape room!\n")
    
    while solved ==False:
        print(location)
        choice = input("What would you like to do?")
        if (" " in choice):
            choices = choice.strip().lower().split(" ")
            command = choices[0]
            qualifier = choices[1]
        else:
            command = choice
        
        if (command=="exit"):
            break
        elif (command=="help"):
            print("Options: look, lookat, lookunder, go, use, exit, help")
        elif (command=="enter" and qualifier=="combo" and location==family_room):
            try_combo()
        elif (command == "look"):
            look(location)
        elif (command=="lookat" or command=="lookunder" or command == "use"):
            action(location, qualifier, command)
        elif (command=="go"):
            if (qualifier=="north" and location.north!=None):
                location = location.north
            elif (qualifier=="south" and location.south!=None):
                location = location.south
            elif (qualifier=="west" and location.west!=None):
                location = location.west
            elif (qualifier=="east" and location.east!=None):
                location = location.east
            else:
                print("There is no room in that direction")
        print("")
    print("Thanks for playing the Escape Room!")
    
if __name__ == "__main__":
    main()    