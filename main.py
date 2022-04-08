# rock,paper and scissors Game......
import ascii_images
from art import *
import random


while True:
    choose = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choose)
    user_input = None

    # font styles for win or loose or draw text....

    win = text2art("you win", font="block", chr_ignore=True)
    loose = text2art("you loose", font="block", chr_ignore=True)
    draw = text2art("draw !", font="block", chr_ignore=True)

    while user_input not in choose:
        user_input = input("Enter the your choice rock or paper or scissors :").lower()
    # user input....
    print(f"Your choice is : {user_input}")

    # user input acsii images....
    if user_input == "rock":
        print(ascii_images.rock)
    elif user_input == "paper":
        print(ascii_images.paper)
    elif user_input == "scissors":
        print(ascii_images.scissors)

    # Computer input...
    print(f"Computer choice is : {computer_choice}")

    # computer input ascii images...
    if computer_choice == "rock":
        print(ascii_images.rock)
    elif computer_choice == "paper":
        print(ascii_images.paper)
    elif computer_choice == "scissors":
        print(ascii_images.scissors)

    if (
        ((computer_choice == "rock") and (user_input == "scissors"))
        or ((computer_choice == "paper") and (user_input == "rock"))
        or ((computer_choice == "scissors") and (user_input == "paper"))
    ):
        tprint("You Loose")
    elif (
        ((computer_choice == "scissors") and (user_input == "rock"))
        or ((computer_choice == "rock") and (user_input == "paper"))
        or ((computer_choice == "paper") and (user_input == "scissors"))
    ):
        print(win)
    elif computer_choice == user_input:
        print(draw)
    paly_again = input("Are you paly want to again? yes/no : ").lower()
    if paly_again != "yes":
        break
tprint("SEE YOU AGAIN... :)")
