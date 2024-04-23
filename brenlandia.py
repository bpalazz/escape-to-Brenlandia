'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002 - Escape to Brenlandia
Course: CPSC 1050 
Section: 001
Description: This code takes user input to play a space exploration game that will bring humans to their new planet.
'''

import sys # allows us to access other modules functions
import os # imports the operating system
from read_riddles import RiddleReader # imports the RiddleReader class from the read_riddles module
from planets import AdventureMap # imports the AdventureMap class from planets
from planets import ExitNotFoundError # imports the ExitNotFoundError class from planets
from planets import Planet # imports the Planet class from planets
from alien import Aliens # imports the Alien function from alien

class PlayRiddle(RiddleReader): # adds the riddle to the game and inherits from the RiddleReader class in the read_riddles module

    def __init__(self, current_planet, file_path): # initializes the parameters of the class
        self.reader = RiddleReader(file_path)
        self.current_planet = current_planet
        self.riddle = self.reader.read_riddles_from_csv() # inherited part of the function

    def handle_riddle(self, num):  # function that handles the riddles from the RiddleReader class

        if self.current_planet.get_name() not in ['Brenlandia', 'Earth']:  # if the current planet is not the starting planet or last planet
            print('You must now answer this riddle so we can keep traveling!')
            attempts = 2  # attempts per riddle

            while num < len(self.riddle['riddle']):  # runs until the number of riddles is equal to the length of riddles available
                
                print(f'You have {attempts} attempts to answer the riddle.')
                
                # Print the riddle
                print(f"Find the common word to describe these words: {self.riddle['riddle'][num]}")
                
                # Get user's answer
                answer = input("Your answer: ").strip().lower()

                # Check if the answer is correct
                if answer == self.riddle['answer'][num]:  # if they get the riddle correct
                    print("Correct!\n")
                    num += 1  # move to the next riddle
                    break
                elif attempts == 1:  # if they used their attempts, this will print
                    self.AlienInvasion()
                    exit(1)
                else:  # if they get it wrong the first time, the hint will print out
                    print("\nIncorrect. Here's a hint: ", self.riddle['hint'][num])
                    attempts -= 1  # lose an attempt

        return num  # returns the current riddle index


def main():
    num = 0 # starts the riddle function on the first riddle

    if len(sys.argv) != 2: # check that the riddles.csv is correct
        print('EXIT')
        return

    input_file = sys.argv[1] # calls the riddles.csv the input function for the read_riddles module
    
    if not os.path.exists(input_file): # makes sure the input file exists on the operating system in use
        print(f"File {input_file} does not exist.")
        return

    reader = RiddleReader(input_file) # assings reader as the input_file in the RiddleReader class

    riddles = reader.read_riddles_from_csv() # calls riddles the reader function

    adventure_map = AdventureMap() # lines 71 - 79 creates the map of the planets
    adventure_map.add_planet(Planet("Brenlandia", [None], [None]))
    adventure_map.add_planet(Planet("Earth", "I'm sure I don't need to explain what Earth is to you. Anyways get us out of here! And quick!", ["Outer Space"]))
    adventure_map.add_planet(Planet("Jadonia", "This beautiful blue planet puts Neptune and Uranus to shame! Only issue is there is no surface to land on so be careful!", ["Richardian"]))
    adventure_map.add_planet(Planet("Richardian", "This planet has a cool giant storm like Jupiter, but is super hot so stay far away from the surface!", ["Pacotian"]))
    adventure_map.add_planet(Planet("Abbeast", "This planet is the scariest of all. It's gravity is extreme and if you get too close you will get pulled in and die.\nGood luck!", ["Brenlandia"]))
    adventure_map.add_planet(Planet("Mars", "Our President, Brenan Palazzolo, has secretly been bringing a fuel supply to Mars over the years.\nWe must go retrieve that real quick so we can make it to Brenlandia.", ["Jadonia"]))
    adventure_map.add_planet(Planet("Outer Space", "Alright, you have made it into space!\nThe people who built this craft were scared of Aliens and designed the craft to only operate with human words.\nYou must answer questions to get propelled to the next destination.\nGood luck!", ['Mars']))
    adventure_map.add_planet(Planet("Pacotian", "This is by far the cutest planet, it was named after President Brenan's dog, Paco, afterall.\nThe planet has a magic force field that we need to use to get to Abbeast", ["Abbeast"]))

    planets_to_go = len(adventure_map.map) - 1 # starts the counter of planets to go.

    print('\nWelcome to the Game: "Escape to Brenlandia"\n\nHello space explorer! You have been an outstanding explorer for our society, but now our society is running out of time.\nEarth is dying and we need you to navigate our society to the new planet, Brenlandia.\nThank you for taking this opportunity.\nIf the pressure becomes to much for you to handle you can type "exit" (you\'ll just end humanity!).\nLet\'s get started:') 
    
    current_planet = adventure_map.get_planet("Earth") # initializes the game to start on Earth

    play_riddle = PlayRiddle(current_planet, input_file)

    print(current_planet) # prints all the information about Earth
    
    while True: # loops until "break" is called

        if current_planet.get_name() == "Earth": # starts the game with correct grammar
            print(f"Please type {current_planet.planet_exit()} to get started: ") 
        else: # keeps the game going with correct grammar 
            print(f"Please type {current_planet.planet_exit()} to keep going: ") 

        planet_choice = input().strip().lower()

        if planet_choice == "exit": # if the player wants to exit the game
            print("Exiting the game... thanks for abandoning our chances at a new society! #RIP humanity")
            break

        try: 
            if planet_choice.lower() not in [exit_planet.lower() for exit_planet in current_planet.get_exits()]:
                raise ExitNotFoundError(planet_choice) # if the planet is not on the map the ExitNotFoundError class will be called from the planets module

            current_planet = adventure_map.get_planet(planet_choice) # updates the current_planet to the inputted planet

            play_riddle = PlayRiddle(current_planet, input_file)

            planets_to_go -= 1 # subtracts 1 from the planets left to go

            if current_planet.get_name() == "Brenlandia": # this prints if the user gets to the final planet
                print("Congrats you have reached Brenlandia!! Humanity is saved and you get to relax on this beautiful hot pink and green planet.\nThanks for playing! Exiting the game...")
                break

            print(f'\n{current_planet}') # prints the description of the planet

            if planets_to_go == 0: # prints nothing at Brenlandia
                print()

            elif planets_to_go == 1: # prints 1 stop away with correct grammar
                print(f"You are {planets_to_go} planets away from Brenlandia\n")

            else: # prints multiple stops away with correct grammar
                print(f"You are {planets_to_go} planets away from Brenlandia\n")

            num = play_riddle.handle_riddle(num) # raises the riddle for the user to play
            
        except ExitNotFoundError as e: # the error statement that will restart the while loop if not actual planet name
            print(f"{e}")
            print("Invalid planet name. Please choose again.")
            continue

    while current_planet.get_name() == 'Brenlandia': # this only prints when the user is at the final planet
        
        kills = 0 # starts the alien body at 0

        print("\nWAIT! What's that in the sky?\nOMG it's Aliens!!\nQuick! Someone get the Alien translator.")
        print('Aliens: Greetings humans, our planet has been taken over. Can we reside here?')

        while True:

            residence = input('Respond: yes or no: ').lower().strip()

            if residence == 'yes': # if the user wants the Aliens to reside with them
            
                print(Aliens(2)) # prints the alien from the alien module
                print('Great... they just ate humanity.')
                print('You saved everyone just to get eaten. GAME OVER')
                exit(1)

            elif residence == 'no': # if the user does not want the Aliens to reside with them
        
                print(Aliens(0)) # prints the alien from the alien module
                print('Oh no! They are trying to eat you! You need to kill them.')
                killer = input('Type kill to kill the Aliens: ').lower().strip()
                kills += 1
                print(Aliens(kills)) # prints the second alien from the alien module
                print("Good job! You may now relax peacefully. GAME OVER")
                exit(1)

            else:
                print("Invalid input. Please enter yes or no.") # restarts the loop
                continue

if __name__ == '__main__':
    main()