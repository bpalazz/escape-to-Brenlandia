'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: The code below creates the planets with their descriptions and next planet. Then the code creates a map of these planets and a message if the player types in an invalid planet.
'''

class ExitNotFoundError(Exception): 
    def __init__(self, planet_name, message='Planet not found'):
        self.message = message
        self.planet_name = planet_name
    
    def __str__(self):
        return f"{self.planet_name} -> {self.message}"

class Planet:
    def __init__(self, name, description, exits): 
        self.name = name
        self.description = description
        self.exits = exits

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
    
    def get_exits(self):
        return self.exits

    def planet_exit(self):
        return "\n".join(self.exits)

    def __str__(self):
        return f'{self.name}: {self.description}\n\nNext Planet:\n{self.planet_exit()}'

class AdventureMap:
    def __init__(self):
        self.map = {} 

    def add_planet(self, planet): 
        self.map[planet.name.lower()] = planet

    def get_planet(self, planet_name):
        if planet_name.lower() in self.map:
            return self.map[planet_name.lower()]
        else:
            raise ExitNotFoundError(planet_name)
