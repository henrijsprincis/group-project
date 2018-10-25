#The following code is adapted from Professo Kirill's game template 2
#https://learningcentral.cf.ac.uk/bbcswebdav/pid-4830871-dt-content-rid-11885046_2/xid-11885046_2
from player import *
from items import *
from gameparser import *
from dialogue import *
from test import *
from passwordGuess import *
import sys
last_action_was_take = False
user_choices= open("player_choices.txt","a")
def check_inventory_for_cheats():
    global inventory
    cheats_in_inventory = False
    for item in inventory:
        if item == item_cheat_notes:
            cheats_in_inventory = True
    return cheats_in_inventory
def check_inventory_for_study_notes():
    global inventory
    cheats_in_inventory = False
    for item in inventory:
        if item == item_notes:
            cheats_in_inventory = True
    return cheats_in_inventory
def check_valid_user_input_test(user_input):
    possible_answers = ["A","B","C","D"]
    if user_input in possible_answers:
        return True
    else:
        return False
def test(cheat_notes_present):
    score = 0
    valid_execution_times = 0
    while(len(nums)>0):
        if(cheat_notes_present):
            print("You look at the cheat notes and see that the correct answer is " + nums[str(valid_execution_times+1)]["ans"])
        if(check_inventory_for_study_notes()):
            print("You remember your notes and see that the hint is '" + nums[str(valid_execution_times+1)]["hint"] + "'")
        print (nums[str(valid_execution_times+1)]["ques"])
        print (nums[str(valid_execution_times+1)]["choice"])
        user_input = input("\n- ").upper()
        user_input_valid = check_valid_user_input_test(user_input)
        if user_input_valid == True:
            if user_input == (nums[str(valid_execution_times+1)]["ans"]):
                print ("Correct")
                score = score + 1
            else:
                print("Incorrect")
            valid_execution_times = valid_execution_times + 1
            nums.pop(str(valid_execution_times))
        else:
            print("please select A,B,C or D")
    score = str(score)
    print ("Your Score is " + score + "/15")
    return int(score)

def is_winning():
    global current_narrative
    global dialogue
    if (current_narrative == dialogue_exam_start):
        if check_inventory_for_cheats():
            print("You are lucky that you have a cheat sheet with you :). Without it who knows what the right answer would be")
            score = test(True)
            #sys.exit()
        else:
            score = test(False)
        if score > 10:
            if check_inventory_for_cheats():
                print("You cheated to win. You beat the system, but did you really. The only reason why you were able to cheat was because you were smart enough to hack into kirill's computer. Cheating may be frowned upon in our modern society, but to a rational human being the social norms are nothing, but guidelines. Cheating will always remain a strategy to gain an edge, but the only question is? Was it worth the risk? Unfortunately, this game has come to an end, but you can check out other ending by playing me again without cheating :) !!!")
                user_choices.write("The user chose to cheat and won the game because of it\n")
                user_choices.close()
                sys.exit()
            print("YOU WIN!!! CONGRATS! Your indepth knowledge of python is very well appreciated and you are an excellent student. There comes a time in our lives where we must part ways. I am afraid that this is it for the game, unless you want to check out the other ending to the game (go to kirills room and hack his computer)")
            user_choices.write("The user won the game without cheating\n")
            user_choices.close()
            sys.exit()
        else:
            print("Poor you. You failed the test and got kicked out of school. Depressed and sad, you turned to alcohol to wash away your problems. This ended your already short lifespan. The moral of the story is that in order to survive, you must either cheat or be intelligent. Don't worry though! You can play me again and see what happens if you cheat/answer correctly. Just make sure that no one is looking because that would be embarrassing!")
            user_choices.write("The user lost the game\n")
            user_choices.close()
            sys.exit()
    elif current_narrative == dialogue_puzzle:
        global inventory
        hangman()
        inventory.append(item_cheat_notes)
        current_narrative = dialogue_stairwell
        dialogue_stairwell["numbers"].pop("4")
    elif current_narrative == dialogue_wait:
        dialogue["dialogue_jason"]["numbers"].pop("2", None)
    elif current_narrative == dialogue_coffee:
        dialogue["dialogue_breakfast"]["numbers"].pop("3", None)
        dialogue["dialogue_kitchen"]["numbers"].pop("2", None)
    else:
        return False
def change_dialogue(user_choice):
    global current_narrative
    global dialogue
    global current_narrative
    global last_action_was_take
    if(current_narrative["numbers"][str(user_choice)].find("take") != -1):
        user_input = current_narrative["numbers"][str(user_choice)]
        user_input = normalise_input(user_input)
        execute_take(user_input[1])
        return
    current_narrative = dialogue[current_narrative["numbers"][str(user_choice)]]
    last_action_was_take = False
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
    #for item in room_items:
        #print("TAKE " + item["id"] + " to take " + item["name"])
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

def execute_command(command):
    user_choice = 0
    if 0 == len(command):
        return
    try:
        global last_action_was_take
        user_choice = int(command[0])
        change_dialogue(user_choice)
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

