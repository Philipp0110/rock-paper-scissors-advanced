# Write your code here
import random


def greeting(name):
    print("Hello, {name}".format(name=name))
    # set_name(name)


def get_rating(name):
    with open("rating.txt", "r")as f:
        rating_ = 0
        for line in f:
            if name in line:
                temp, rating_ = line.split()
                return int(rating_)
    if rating_ == 0:
        return rating_


def classic_game(user_input):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    global rating
    if user_input == "rock":
        if computer_choice == "scissors":
            rating += 100
            print("Well done. The computer chose scissors and failed")
        elif computer_choice == "paper":
            print("Sorry, but the computer chose paper")
        else:
            rating += 50
            print("There is a draw (rock)")
    elif user_input == "paper":
        if computer_choice == "scissors":
            print("Sorry, but the computer chose scissors")
        elif computer_choice == "paper":
            rating += 50
            print("There is a draw (paper)")
        else:
            rating += 100
            print("Well done. The computer chose rock and failed")
    elif user_input == "scissors":
        if computer_choice == "scissors":
            rating += 50
            print("There is a draw (scissors)")
        elif computer_choice == "paper":
            rating += 100
            print("Well done. The computer chose paper and failed")
        else:
            print("Sorry, but the computer chose rock")
    else:
         print("Invalid input")


def not_classic_game(game_list, user_input):
    global rating
    computer_choice = random.choice(game_list)
    length = len(game_list)
    if user_input in game_list:
        user_index = game_list.index(user_input)
        computer_index = game_list.index(computer_choice)
        if user_input == computer_choice:
            print("There is a draw ({option})".format(option=user_input))
            rating += 50
        else:
            new_list = game_list[game_list.index(user_input):]
            for i in range(game_list.index(user_input)):
                new_list.append(game_list[i])
            new_list.remove(user_input)
            winner = new_list[0:(length//2)]
            loser = new_list[length//2:]
            if computer_choice in loser:
                rating += 100
                print("Well done. The computer chose {option} and failed".format(option=computer_choice))
            else:
                print("Sorry, but the computer chose", computer_choice)

    else:
        print("Invalid input")


game_run = True
user_name = input("Enter your name: ")
greeting(user_name)
rating = get_rating(user_name)
game_list = input().split(',')
print("Okay, Let's start")

while game_run:
    user_input = input()
    if user_input == "!exit":
        print("Bye!")
        game_run = False
    elif user_input == "!rating":
        print("Your rating: " + str(rating))
    elif game_list[0] == '':
        classic_game(user_input)
    else:
        not_classic_game(game_list, user_input)

