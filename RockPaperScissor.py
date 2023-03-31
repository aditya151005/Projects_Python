#Importing random module
import random
#printing welcome message of game
print("~~~~~~Welcome to Rock, Paper and Scissors Game~~~~~~")
#Initial score of user
user_score=0
#Initial score of computer
comp_user=0
#Initial Tie score 
ties=0
#input the user name
name=input("Enter your name:")
#Printing Winning rules of game
print("""Winning Rules:
      1. Paper vs Rock --> Paper
      2. Rock vs Scissors --> Rock
      3. Scissors vs Paper --> Scissors
      """)
while True:
    print("""Choices are:
        1.Rock
        2.Paper
        3.Scissors
        """)
    print()
#Choices are made by user
    choice=int(input("Enter your choice from 1-3:"))
    print()
#checking the validity of user choice
    while choice>3 or choice<1:
        choice=int(input("Enter valid choice"))
    if choice==1:
        user_choice='Rock'
    elif choice==2:
        user_choice='Paper'
    else:
        user_choice='Scissors'  
    print("The user's choice is",user_choice)
    print("Now it is Computer's turn")
#choices made by computer
    computer=random.randint(1,3)
    if computer==1:
        comp_choice="Rock"
    elif computer==2:
        comp_choice="Paper"
    else:
        comp_choice="Scissors"
    print("The computer's choice is",comp_choice)
#Checking the game rules
    if((user_choice=='Rock' and comp_choice=='Paper') or (user_choice=='Paper' and comp_choice=='Rock')):
        print("Paper wins")
        result="Paper"
    elif((user_choice=='Rock' and comp_choice=='Scissors') or (user_choice=='Scissors' and comp_choice=='Rock')):
        print("Rock wins")
        result="Rock"
    elif(user_choice==comp_choice) :
        print("It's a tie in a particular game")
        result="Tie"  
    else:
        print("Scissors wins")
        result="Scissors"
#updating the scores of user and computer
    if result=="Tie":
        ties+=1
    elif result==user_choice:
        print("User Wins in this particular game")
        user_score+=1
    else:
        print("Computer Wins in this particular game")
        comp_user+=1
    print("Scores are")
#printing user score
    print(name,"'s score is",user_score)
#printing computer score
    print("computer's score is",comp_user)
#printing score when scores are at tie position
    print("ties score is",ties)
#checking the final results of game
    if user_score>comp_user:
        print("User wins in overall game")
    elif user_score<comp_user:
        print("Computer wins in overall game")
    else:
        print("It's a tie in overall game")
    repeat=input("Do you want to play again? ")
    if repeat == "no" or repeat == "No":
        break
print("Game Over!")
print("Thanks for playing!!!!")