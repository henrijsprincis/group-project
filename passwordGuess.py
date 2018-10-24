import random
import time
import os
import sys
number_of_correct_letters = 0
def randomize_password(password):#takes in password, spits out mixed letters
    output = ""
    while(len(password) != 0):
        random_pos = random.randint(0,len(password)-1)#get rand pos in string
        random_char = password[random_pos] #get random char in string
        output = output + random_char
        password = password[:random_pos] + password[(random_pos+1):]
    return output
def print_correct_position(user_input, password):
    global number_of_correct_letters
    position_in_user_guess = 0
    for position in range(len(user_input)):
        position_in_user_guess = password.find(user_input[position])#gives pos of user guess in password
        if password[position_in_user_guess] == password[position]:
            number_of_correct_letters = number_of_correct_letters + 1
            print("The letter " + user_input[position] + " is at the correct position")
        else:
            print("The letter " + user_input[position] + " is at an incorrect position")
def hangman():
    global number_of_correct_letters
    guesses_remaining = 5
    password = "incorrect"
    print("""You see kirill's computer and using your mad hacking skills you find an exploit in the linux kernel which has allowed
you to take a memory dump. Unfortunately, while transmiting the memory over netcat it has become scrambled. You have worked out the length
and what letters the password contains, but you do not know the right order. You can check the order of the letters by guessing""")
    while guesses_remaining > 0:
        print("You have " + str(guesses_remaining) + " guesses remaining")
        print ("The mixed order password is'" +randomize_password(password) + "'")
        print ("the length of the word is " + str(len(password)))
        user_input = input("> ").lower()
        user_input = user_input[0:len(password)] #shorten the user input if they put too many charachters
        print_correct_position(user_input, password)
        if(number_of_correct_letters == len(password)):
            try:
                os.system('cls')#clear screen
                os.system('color 04')#make the cmd color green
                print("You win! Thank you for playing")
                time.sleep(4)
                os.system('color 07')#switch the color back to white
                sys.exit()
            except:
                sys.exit()
                pass
        else:
            guesses_remaining = guesses_remaining -1
            try:
                os.system('color 04')#make the cmd color red
                print("WRONG!!!")
                time.sleep(1)
                os.system('color 07')#switch the color back to white
                os.system('cls')
            except:
                pass
    print("You enter the password wrong too many times and kirill has caught you... He is so upset with you that he expelled you")
