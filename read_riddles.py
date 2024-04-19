'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: This code reads the riddles.csv file and separates the parameters of the riddle into riddle, answer, and hint to the main function.
'''

import csv
import random
import json

class RiddleReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def __call__(self):
        return self.read_riddles_from_csv()

    def read_riddles_from_csv(self):
        data = {'riddle': [], 'answer': [], 'hint': []}

        expected_keys = ['riddle', 'answer', 'hint']

        k = 0
        
        with open(self.file_path, 'r') as file:
            csv_reader = csv.DictReader(file)

            keys = csv_reader.fieldnames

            missing_keys = [key for key in expected_keys if key not in keys]
            if missing_keys:
                print(f"Missing expected columns in CSV file: {', '.join(missing_keys)}.")
                exit()
            
            num_columns = len(keys)
            for line in file:
                values = line.strip().split(',')
                if len(values) == num_columns:
                    for i in range(num_columns):
                        item = values[i]
                        data[keys[k]].append(item)
                        k += 1
                        
                k = 0
        
            file.close()
        
        return data

    def __str__(self):
        return str(self.read_weather_data_csv())