import time


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro():
    time.sleep(1)
    print_pause("WELCOME TO THE GAME.\n")
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.\n")
    print_pause("To your right is a dark cave.\n")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

def fight():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and out steps a pirate.\n")
    print_pause("Eep! This is the pirate's house!\n")
    print_pause("The pirate attacks you!\n")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.\n")

    while True:

        fight_response = int(input(("Would you like to (1) fight or (2) run away?/n")))
        if fight_response == 1:
            print_pause("You do your best...")
            print_pause("but your dagger is no match for the pirate.")
            print_pause("You have been defeated!")

        


while True:
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    response = int(input("What would you like to do?\n"))

    if response == 1:

