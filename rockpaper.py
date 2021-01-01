# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:04:57 2020

@author: yogith
"""


import random
#To count your Total score
score = []
tie = "nothing"

print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
stop = False
# Below in range(n): n denotes how many times you wanna play
for i in range(11):
    print(" ")
    print("your choice 1.rock 2.paper 3.scissor")
    choice = int(input("enter your choice: "))
    
    
    # changing your choice number into string form
    if choice == 1:
        you = "rock"
        print("your choice is rock")
    elif choice == 2:
        you = "paper"
        print("your choice is paper")
    elif choice == 3:
        you = "scissor"
        print("your choice is scissor")
        
        
        
    # changing computer choice number into string form
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_name = "rock"
        print("computer choice is rock")
        print(" ")
    elif comp_choice == 2:
        comp_name = "paper"
        print("computer choice is paper")
        print(" ")

    elif comp_choice == 3:
        comp_name = "scissor"
        print("computer choice is scissor")
        print(" ")

    
    # Here the game takesplace
    # we'll get results
    if choice == comp_choice:
       result = "nothing"
    elif(choice == 1 and comp_choice == 3 or choice == 1 and comp_choice == 3 ):
        result = "rock"
    elif(choice == 2 and comp_choice == 3 or choice == 3 and comp_choice == 2):
        result = "scissor"
    else:
        result = "paper"
    
    print(you,"vs",comp_name)
    print(result,"wins")
    

    if(you ==  result):
        print("you've got 1 points")
        score.append(1)# appends 1 to score list
    elif(result == tie):
        print("tie")
    else:
        print("you lose")
    
# we'll count the number of ones in score list and calulate total score   
total_score = score.count(1)
print(" ")
print("your total score is",total_score)