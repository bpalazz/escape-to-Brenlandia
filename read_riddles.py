'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: This code reads the riddles.csv file and separates the parameters of the riddle into riddle, answer, and hint to the main function.
'''

import csv # imports the csv file

class RiddleReader: # class the reads the data from the input_file 
    
    def __init__(self, file_path): # initializes the input_file to self
        self.file_path = file_path

    def __call__(self): # allows the call of read_riddles from_csv to happen
        return self.read_riddles_from_csv()

    def AlienInvasion(self): # statement that prints in the PlayRiddle class in brenlandia
        print('\nAh! You must be an Alien!! Abort mission! Game Over.')

    def read_riddles_from_csv(self): # reads the riddle data from the csv file
        data = {'riddle': [], 'answer': [], 'hint': []} # dictionary of all the data

        expected_keys = ['riddle', 'answer', 'hint'] # the expected categories in the csv file

        k = 0 # initializes the first column to go to riddle
        
        with open(self.file_path, 'r') as file: # opens the file as reading
            csv_reader = csv.DictReader(file) # reads the file

            keys = csv_reader.fieldnames # calls the top row the keys

            missing_keys = [key for key in expected_keys if key not in keys] # if the keys are missing in the csv file
            if missing_keys:
                print(f"Missing expected columns in CSV file: {', '.join(missing_keys)}.") # tells you what is missing/wrong
                exit()
            
            num_columns = len(keys) 
            for line in file: # reads each line in the file
                values = line.strip().split(',') # splits the lines up at the commas
                if len(values) == num_columns:
                    for i in range(num_columns):
                        item = values[i]
                        data[keys[k]].append(item) # data is appened if the length of the values matches the number of keys
                        k += 1 # will move to the next column
                        
                k = 0
        
            file.close() # closes the file
        
        return data # returns the data collected

    def __str__(self):
        return str(self.read_weather_data_csv()) # returns the read file as a string