import time
choices = []

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(.5)

def intro():
    time.sleep(1)
    print_pause("WELCOME TO THE Adventure GAME.\n")
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response

def main():

    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")

    response = valid_input("What would you like to do now? (Please enter 1 or 2.)\n",
                           "Enter 1", "Enter 2")


def fight():

    

