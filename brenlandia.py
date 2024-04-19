'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: This code takes user input to play a space exploration game that will bring humans to their new planet.
'''

import sys
import os
import random
from read_riddles import RiddleReader
from planets import AdventureMap
from planets import ExitNotFoundError
from planets import Planet

def handle_riddle(current_planet, riddles, num):
    if current_planet.get_name() not in ['Brenlandia', 'Earth']:
        print('You must now answer this riddle so we can keep travelling!')
        attempts = 2
        while num < len(riddles['riddle']):
            print(f'You have {attempts} attempts to answer the riddle')
            print(f"Find the common word to describe these words: {riddles['riddle'][num]}")
            answer = input("Your answer: ").strip().lower()
            
            if answer == riddles['answer'][num]:
                print("Correct!\n")
                num += 1
                break
                
            elif attempts == 1:
                print('\nAh! You must be an Alien!! Abort mission! Game Over.')
                exit(1)

            else:
                print("\nIncorrect. Here's a hint: ", riddles['hint'][num])
                attempts -= 1
        
    return num

def main():
    num = 0

    if len(sys.argv) != 2:
        print('EXIT')
        return

    input_file = sys.argv[1]
    
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist.")
        return

    reader = RiddleReader(input_file)

    riddles = reader()

    adventure_map = AdventureMap()
    adventure_map.add_planet(Planet("Brenlandia", [None], [None]))
    adventure_map.add_planet(Planet("Earth", "I'm sure I don't need to explain what Earth is to you. Anyways get us out of here! And quick!", ["Outer Space"]))
    adventure_map.add_planet(Planet("Jadonia", "This beautiful blue planet puts Neptune and Uranus to shame! Only issue is there is no surface to land on so be careful!", ["Richardian"]))
    adventure_map.add_planet(Planet("Richardian", "This planet has a cool giant storm like Jupiter, but is super hot so stay far away from the surface!", ["Pacotian"]))
    adventure_map.add_planet(Planet("Abbeast", "This planet is the scariest of all. It's gravity is extreme and if you get too close you will get pulled in and die.\nGood luck!", ["Brenlandia"]))
    adventure_map.add_planet(Planet("Mars", "Our President, Brenan Palazzolo, has secretly been bringing a fuel supply to Mars over the years.\nWe must go retrieve that real quick so we can make it to Brenlandia.", ["Jadonia"]))
    adventure_map.add_planet(Planet("Outer Space", "Alright, you have made it into space!\nThe people who built this craft were scared of Aliens and designed the craft to only operate with human words.\nYou must answer questions to get propelled to the next destination.\nGood luck!", ['Mars']))
    adventure_map.add_planet(Planet("Pacotian", "This is by far the cutest planet, it was named after President Brenan's dog, Paco, afterall.\nThe planet has a magic force field that we need to use to get to Abbeast", ["Abbeast"]))

    total_planets = len(adventure_map.map) - 1

    print('\nWelcome to the Game: "Escape to Brenlandia"\n\nHello space explorer! You have been an outstanding explorer for our society, but now our society is running out of time.\nEarth is dying and we need you to navigate our society to the new planet, Brenlandia.\nThank you for taking this opportunity.\nIf the pressure becomes to much for you to handle you can type "exit" (you\'ll just end humanity!).\nLet\'s get started:') 
    current_planet = adventure_map.get_planet("Earth")

    print(current_planet)

    planets_to_go = total_planets

    while True:
        num = handle_riddle(current_planet, riddles, num)
        
        if current_planet.get_name() == "Earth":
            print(f"Please type {current_planet.planet_exit()} to get started: ") 
        else:
            print(f"Please type {current_planet.planet_exit()} to keep going: ") 

        planet_choice = input().strip().lower()

        if planet_choice == "exit":
            print("Exiting the game... thanks for abandoning our chances at a new society! #RIP humanity")
            break

        try:
            if planet_choice.lower() not in [exit_planet.lower() for exit_planet in current_planet.get_exits()]:
                raise ExitNotFoundError(planet_choice)

            current_planet = adventure_map.get_planet(planet_choice)

            planets_to_go -= 1

            if current_planet.get_name() == "Brenlandia":
                print("Congrats you have reached Brenlandia!! Humanity is saved and you get to relax on this beautiful hot pink and green planet.\nThanks for playing! Exiting the game...")
                break

            print(f'\n{current_planet}')

            if planets_to_go == 0:
                print()
            elif planets_to_go == 1:
                print(f"You are {planets_to_go} stop away from Brenlandia\n")

            else:
                print(f"You are {planets_to_go} stops away from Brenlandia\n")

        except ExitNotFoundError as e:
            print(f"{e}")
            print("Invalid planet name. Please choose again.")
            continue


if __name__ == '__main__':
    main()