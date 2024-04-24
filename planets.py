'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: The code below creates the planets with their descriptions and next planet. Then the code creates a map of these planets and a message if the player types in an invalid planet.
GitHub Link: https://github.com/bpalazz/escape-to-Brenlandia
'''

class ExitNotFoundError(Exception): # This class calls an error when the user inputted planet is not found in the map.
    def __init__(self, planet_name, message='Planet not found'): # initializes the planet and message
        self.message = message
        self.planet_name = planet_name
    
    def __str__(self): # function that prints out when the class is called
        return f"{self.planet_name} -> {self.message}"

class Planet: # this class accesses all the different parameters of the planet
    def __init__(self, name, description, exits): # this function initializes all those parameters
        self.name = name
        self.description = description
        self.exits = exits

    def get_name(self): # returns the name of the planet
        return self.name

    def get_description(self): # returns the description of the planet
        return self.description
    
    def get_exits(self): # returns the exit of the planet
        return self.exits

    def planet_exit(self): # returns the exit of the planet as a string
        return "\n".join(self.exits)

    def __str__(self): 
        return f'{self.name}: {self.description}\n\nNext Planet:\n{self.planet_exit()}'

class AdventureMap: # Class that creates the map of the planets
    def __init__(self):
        self.map = {} 

    def add_planet(self, planet): # adds the planet to the map
        self.map[planet.name.lower()] = planet

    def get_planet(self, planet_name): # returns the planet name if the planet is on the map
        if planet_name.lower() in self.map:
            return self.map[planet_name.lower()]
        else: # raises the error if planet is not on the map
            raise ExitNotFoundError(planet_name)
