'''
Created on Nov 10, 2018

@author: ITAUser

OBJECTIVE:
We want to create a program that makes a rock paper scissors game
ALGORITHM:
First, we will create code that checks who won each round
Second, we will create code that takes the input (choices) from the user
Third, we will create code that takes the 'input'(choices) from the computer
Fourth, we will create code that checks if the user wants to quit, or if the user doesn't enter one of the options(rock,paper,scissors)
Fifth, we will loop each round of the game
Sixth, we will add statements at the end and the beginning that welcome and thank the user playing
Finally, we will loop the whole game, so that the user can keep playing until they choose to quit
'''

'''
1 = rock
2 = scissors
3 = paper
'''

import random

keepPlaying = True
while(keepPlaying):
    print("welcome to Rock, Paper, Scissors!")
    print("Best two out of three. Press 'q' to quit")
    
    humanScore = 0
    cpuScore = 0
    while(humanScore < 2 and cpuScore < 2):
        choice = input ("Please choose(Rock, Paper, Scissors): ")
        choice = choice.strip()
        cpuChoice = random.randint(1,3)
    
        if(choice.lower == 'q'):
            keepPlaying = False
            break
    
        elif ((choice.lower() == 'rock' and cpuChoice == 1) or (choice.lower () == 'scissors' and cpuChoice == 2) or (choice.lower () == 'paper' and cpuChoice == 3)):
            print ("DRAW")
            print ("Human: " + humanScore.__str__() + " CPU: " + cpuScore.__str__())
        elif ((choice.lower() == 'rock' and cpuChoice == 2) or (choice.lower() == 'scissors' and cpuChoice == 3) or (choice.lower() == 'paper'and cpuChoice ==1)):
            humanScore = humanScore + 1
            print("Human: " + humanScore.__str__() + "CPU: " + cpuScore.__str__())
        elif ((choice.lower() == 'rock' and cpuChoice == 3) or (choice.lower() == 'scissors' and cpuChoice == 1) or (choice.lower () == 'paper' and cpuChoice ==2)):
            cpuScore = cpuScore + 1
            print("Human: " + humanScore.__str__() + "CPU: " + cpuScore.__str__())
        
        else:
            print("not an option, try again")
    
    print("Thanks for playing!")
    if(humanScore == 2 ):
        print("You Win!")
    if(cpuScore == 2):
        print("You Lose")
    print("Human: " + humanScore.__str__() + "CPU: " + cpuScore.__str__())
