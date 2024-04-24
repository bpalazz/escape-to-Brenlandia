'''
Author: Brenan Palazzolo
Date: 4 - 16 - 24
Assignment: RPG Project 002
Course: CPSC 1050 
Section: 001
Description: This code holds all the bodies of the aliens.
GitHub Link: https://github.com/bpalazz/escape-to-Brenlandia
'''

def Aliens(kills): # function that holds the three bodies of the aliens used
  Bodies = (
      ''' 
        (._.)
        \ | /   
         \|/     
          |     
          |    
         / \   
      ''',
      '''      
       _____(x_x)        
      //    \\\\
      ''',
      '''         
        (.( ____o).)        
          |// \\\\      
        \ | /   
         \|/     
          |        o
          |       \|/
         / \      / \\

      '''
    )
  return Bodies[kills] # returns the body at the value of kill in the main function
