import time
import random
choices = []
random_enemy = ['Pirate', 'Phantom', 'Medusa', 'Giant Spider']
enemy = random.choice(random_enemy)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    time.sleep(1)
    print_pause("WELCOME TO THE Adventure GAME.\n")
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.\n")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                "and has been terrifying the nearby village.\n")
    print_pause("In Front of you there is house and "
                "to your right there is a dark cave.\n")
    print_pause("In your hand you hold your simple, "
                "yet trusty (but not very effective) dagger.\n")


def main_msg():
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")


def pirate_attack_msg():
    time.sleep(1)
    print_pause("You approach the door of the house.\n")
    print_pause(f"You are about to knock when the door opens,"
                f"and out steps a dangerous {enemy}.\n")
    print_pause(f"Eep! This is the {enemy}'s house!\n")
    print_pause(f"The {enemy} attacks you!\n")


def cave_msg():
    time.sleep(1)
    print_pause("You peer cautiously into the cave.\n")
    print_pause("It turns out to be only a very small cave.\n")
    print_pause("Your eye catches a glint of metal behind a rock.\n")
    print_pause("You have found the magical Sword of Ogoroth.\n")


def sword_msg():
    print_pause("Do you want to pick the Sword of Ogoroth\n")


def sword_pick_msg():
    print_pause("Great Choice...\n")
    print_pause("A ranged attack that silences enemies with,"
                "bolt of electricity is in your possesion.\n")


def sword_not_picked_msg():
    print_pause("Be sure you didnt pick the Sword.\n")


def cave_repeat_msg():
    time.sleep(1)
    print_pause("Oh boy!!!!!!!. We have visited the Cave,"
                "already and taken the sword of our Choice\n")
    print_pause("It is useless to come back to the cave,"
                "and searching the empty place.\n")


def attack_without_sword_msg():
    time.sleep(1)
    print_pause("You do your best...\n")
    print_pause(f"but your dagger is no match for the {enemy}.\n")
    print_pause("You have been defeated!.\n")


def attack_with_sword():
    time.sleep(1)
    print_pause(f"As the {enemy} moves to attack,"
                "you unleash your new sword.\n")
    print_pause("The Sword of Ogoroth shines brightly in your hand,"
                "as you brace yourself for the attack.\n")
    print_pause(f"But the {enemy} takes one look at your shiny, "
                "new toy and runs away!\n")
    print_pause(f"You have rid the {enemy}. You are victorious!\n")
    print_pause("YOU WON\n")


def field():

    while True:
        main_msg()
        player_response = input("What would you like to do now?"
                                "(Please enter 1 or 2.)\n")
        if player_response == "1":
            pirate_attack_msg()
            if "player_has_sword" in choices:
                print_pause("You feel ready for this,"
                            "what with having your new sword.\n")
            else:
                print_pause("You feel a bit under-prepared for this,"
                            "what with only having a tiny dagger.\n")
            fight_run()
            break
        elif player_response == "2":
            if "player_has_sword" in choices:
                cave_repeat_msg()
            else:
                cave_msg()
                sword_pick()
        else:
            print_pause("Sorry, I don't understand."
                        "Please Enter number 1 or 2.\n")


def fight_run():
    while True:
        fight_run_response = input("Would you like to,"
                                   "(1) fight or (2) run away?\n")

        if fight_run_response == "1":
            if "player_has_sword" in choices:
                attack_with_sword()
            else:
                attack_without_sword_msg()
            break
        elif fight_run_response == "2":
            print_pause("You run back into the field."
                        "Luckily, you don't seem to have been followed.\n")
            field()
            break
        else:
            print_pause("Sorry, I don't understand."
                        "Please Enter number 1 or 2.\n")


def sword_pick():
    while True:
        sword_msg()

        sword_plr_response = input("If YES 'Press 1' or 'Press 2' for NO.\n")

        if sword_plr_response == "1":
            print_pause("Great Choice...\n")
            print_pause("A ranged attack that silences enemies,"
                        "with bolt of electricity is in your possesion.\n")
            choices.append("player_has_sword")
            break
        elif sword_plr_response == "2":
            sword_not_picked_msg()
            choices.append('')
            break
        else:
            print_pause("Sorry, I don't understand."
                        "Please Enter number 1 or 2.\n")


def play_again():
    while True:
        play_again_response = input("Do you wish to play again?"
                                    "1) Restart or (2) Quit?\n")

        if play_again_response == "1":
            print_pause("Excellent....Restarting....!")
            play_game()
        elif play_again_response == "2":
            print_pause("Thank you for playing the game."
                        "See you soon again.\n")
            break
        else:
            print_pause("Sorry, I don't understand."
                        "Please Enter number 1 or 2.\n")
        break


def play_game():
    intro()
    field()
    play_again()


play_game()
