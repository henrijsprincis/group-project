#!/usr/bin/python3 LOL


from player import *
from items import *
from gameparser import *
from dialogue import *
from test import *
last_action_was_take = False

def test():
    score = 0
    for key in nums:
        print (nums[key]["ques"])
        print (nums[key]["choice"])
        user_input = input("\n- ")
        user_input = user_input.upper()
        if user_input == (nums[key]["ans"]):
            print ("Correct")
            score = score + 1
        else:
            print("Incorrect")
    score = str(score)
    print ("Your Score is " + score + "/15")
    return score

def is_winning():
    global current_narrative
    if (current_narrative == dialogue_exam_start):
        test()
    else:
        return False
def change_dialogue(user_choice):
    global current_narrative
    global dialogue
    global current_narrative
    #print(current_narrative["numbers"][str(user_choice)] + "THIS CODE RAN!!!")
    if(current_narrative["numbers"][str(user_choice)].find("take") != -1):
        user_input = current_narrative["numbers"][str(user_choice)]
        user_input = normalise_input(user_input)
        print(user_input[1])
        execute_take(user_input[1])
        return
    current_narrative = dialogue[current_narrative["numbers"][str(user_choice)]]
def list_of_items(items):
    ret = ""
    if items == []:
        return ret
    for item in items:
        ret = ret + item["name"] + ".\n"
    return ret[0:len(ret)-2]
def print_inventory_items(items):
    print ("You have " + list_of_items(items) + ".\n")

def print_dialogue(room):
    print("")
    # Display dialogue
    print(room["description"])
    print("")
    
def dialogue_option_leads_to(current_dialogue, numbers):
    return dialogue[current_dialogue["numbers"][number]]

def print_menu(dialogue_options, room_items, inv_items):
    print("You can:")
    # Iterate over available exits
    for option in dialogue_options:
        #current narrative numbers (Option = 1)
        if(dialogue_options[option].find("take") == -1):
            print("press " + str(option) + " " + dialogue[dialogue_options[option]]["name"])
        else:#the option contains the word take
            if(room_items != []):
                print("press " + str(option) + " to " + dialogue_options[option])
    for item in room_items:
        print("TAKE " + item["id"] + " to take " + item["name"])
    for item in inv_items:
    	print("DROP " + item["id"] + " to drop " + item["name"])
    print("What do you want to do?")


def is_valid_dialogue(exits, chosen_exit):
    return chosen_exit in exits


def execute_go(direction):
    global last_action_was_take
    last_action_was_take = False
    global current_narrative
    try:
        current_narrative = move(current_narrative["numbers"], direction)
    except:
        print("you cannot move there")


def execute_take(item_id):
    global last_action_was_take
    last_action_was_take = True
    i = 0
    total_sum_of_items = 0
    global current_narrative
    try:
        actual_item = items_all[item_id]
    except:
        print("Invalid item name")
    try:
        for element in current_narrative["items"]:
            if actual_item == element:
                current_narrative["items"].pop(i)
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
            if actual_item == element:
                current_narrative["items"].append(element)
                inventory.pop(i)
            i = i + 1
    except:
        print("You cannot drop that")
    

def execute_command(command):
    user_choice = 0
    if 0 == len(command):
        return
    try:
        user_choice = int(command[0])
        #global current_narrative
        #print(current_narrative["numbers"][str(user_choice)])
        #if (current_narrative["numbers"][str(user_choice)] == "EXAMSTART"):
            #test()
        change_dialogue(user_choice)
        global last_action_was_take
        last_action_was_take = False
    except:
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
        if (last_action_was_take == True):
            print_inventory_items(inventory)
        else:
            print_dialogue(current_narrative)

        # Show the menu with possible actions and ask the player
        command = menu(current_narrative["numbers"], current_narrative["items"], inventory)

        # Execute the player's command
        execute_command(command)#if the command is take, print inv else print dialogue



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

