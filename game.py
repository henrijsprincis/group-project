#!/usr/bin/python3 LOL

from dialogue import *
from player import *
from items import *
from gameparser import *

def is_winning():
    return False

def print_inventory_items(items):
    print ("You have " + list_of_items(items) + ".\n")

def print_dialogue(room):
    print("")
    # Display dialogue
    print(room["description"])
    print("")
    
def dialogue_option_leads_to(current_dialogue, numbers):
    return rooms[exits[direction]]["name"]


def print_menu(exits, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))
    for item in room_items:
    	print("TAKE " + item["id"] + " to take " + item["name"])
    for item in inv_items:
    	print("DROP " + item["id"] + " to drop " + item["name"])
    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    #print (current_room)
    global current_narrative
    try:
        current_narrative = move(current_narrative["numbers"], direction)
    except:
        print("you cannot move there")


def execute_take(item_id):
    #Try to loop through the items in the current room
    #try:
    i = 0
    total_sum_of_items = 0
    try:
        actual_item = items_all[item_id]
    except:
        print("Invalid item name")
    try:
        for element in current_room["items"]:
            if actual_item == element:
                for myinvitem in inventory:
                    total_sum_of_items = total_sum_of_items + myinvitem["mass"]
                if (total_sum_of_items + element["mass"] > 3.0):
                    print ("You cannot take that")
                    print ("It is too heavy :/")
                    return
                current_room["items"].pop(i)
                inventory.append(element)
                print("you picked up "+ element["name"])
                return
            i = i + 1
    except:
        print("")
    print ("You cannot take that")
    return

def execute_drop(item_id):
    i = 0
    try:
        actual_item = items_all[item_id]
        for element in inventory:
            #print (element)
            #print (item_id)
            if actual_item == element:
                current_room["items"].append(element)
                inventory.pop(i)
            i = i + 1
    except:
        print("You cannot drop that")
    

def execute_command(command):
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    return rooms[exits[direction]]


# This is the entry point of our program
def main():

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        if is_winning() == True:
            print ("you win!!!")
            exit()
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

