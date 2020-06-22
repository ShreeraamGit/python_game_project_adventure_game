import time
choices = []

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

def main_theme():

    while True:

        print_pause("Enter 1 to knock on the door of the house.\n")
        print_pause("Enter 2 to peer into the cave.\n")

        player_response = input("What would you like to do now? (Please enter 1 or 2.)\n")
        if player_response == '1':
            fight()
            break
        elif player_response == '2':
            cave()
            break
        else:
            print_pause("Sorry, I don't understand.Please Enter number 1 or 2.\n")

def fight():
    print_pause("You approach the door of the house.\n")
    print_pause("You are about to knock when the door opens and out steps a pirate.\n")
    print_pause("Eep! This is the pirate's house!\n")
    print_pause("The pirate attacks you!\n")
    print_pause("You feel a bit under-prepared for this, what with only having a tiny dagger.\n")

    while True:

        fight_response = input("Would you like to (1) fight or (2) run away?\n")

        if fight_response == '1':
            
            if "sword_taken" in choices:
                attack_with_sword()
                break
            elif "sword_taken" not in choices:
                attack_without_sword()
                break
        elif fight_response == '2':
            print_pause("You run back into the field. Luckily, you don't seem to have been followed.\n")
            main_theme()
        else:
            print_pause("Sorry, I don't understand.Please Enter number 1 or 2.\n")

    play_again()

def cave():

    if "sword_taken" in choices:
        print_pause("Oh boy!!!!!!!. We have visited the Cave already and taken the sword of our Choice\n")
        print_pause("We cannot enter the cave again\n")
        main_theme()

    elif "sword_taken" not in choices:
        print_pause("You peer cautiously into the cave.\n")
        print_pause("It turns out to be only a very small cave.\n")
        print_pause("Your eye catches a glint of metal behind a rock.\n")
        print_pause("You have found the magical Sword of Ogoroth and Sword of Zeus\n")
        while True:
            
            sword_response = input("Would you like to take (1) Sword of Ogoroth  or (2) Sword of Zeus?\n")
            if sword_response == '1':
                print_pause("Great Choice...\n")
                print_pause("A ranged attack that silences enemies with bolt of FireBalls.\n")
                choices.append("sword_taken")
                break
            elif sword_response == '2':
                print_pause("Great Choice...\n")
                print_pause("A ranged attack that silences enemies with bolt of electricity.\n")
                choices.append("sword_taken")
                break
            else:
                print_pause("Sorry, I don't understand.Please Enter number 1 or 2.\n")
        print_pause("You discard your silly old dagger and take the sword of your choice with you.\n")
        print_pause("You walk back out to the field.\n")
        main_theme()
           
def attack_with_sword():
        print_pause("As the gorgon moves to attack, you unsheath your new sword.\n")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.\n")
        print_pause("But the gorgon takes one look at your shiny new toy and runs away!\n")
        print_pause("You have rid the town of the gorgon. You are victorious!\n")
        print_pause("YOU WON\n")
        

def attack_without_sword():

        print_pause("You do your best...\n")
        print_pause("but your dagger is no match for the pirate.\n")
        print_pause("You have been defeated!.\n")

def play_again():

    while True:

        play_again_response = input("Would you like to play again? (y/n)\n").lower()

        if play_again_response == 'y':
            print_pause("Excellent! Restarting the game ...\n")
            play_game()
        elif play_again_response == 'n':
            print_pause("Thank you for supporting the Game.See you soon again...\n")

        else:
            print_pause("Sorry, I don't understand.Please Enter number 'y' or 'n'.\n")

def play_game():
    intro()
    choices = []
    main_theme()

play_game()


        

#while True:
    #print_pause("Enter 1 to knock on the door of the house.\n")
    #print_pause("Enter 2 to peer into the cave.\n")
    #response = int(input("What would you like to do?\n"))

    #if response == 1:
        #fight()

#while True:

        #sword_choice = int(input("Press 1 to select Magical Sword of Ogoroth or Press 2 to select Sword of Zeus")  
        #if sword_choice == 1:
            #print_pause("Great choice !")
            ##elif sword_choice == 2:
            #print_pause("A ranged attack that silences enemies with bolt of electricity")
            ##break
        #else:
            #print_pause("Sorry, I don't understand.Please Enter number 1 or 2")