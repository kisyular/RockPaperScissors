
###################################################################################
#Algorithm
#   import the math functions,random
#   print the instructions of the game so the user knows the guidelines
#   initialize computer choice to an empty string
#   initiate a Boolean condition (while True)
#   prompt the user to enter a command which is either r, p, s or q
#   print what happens if the user chooses 'q'
#   print what happens if the user chooses r, p, s
#   define what happens after computer chooses any random number either 1, 2 or 3
#   set a condition which shows who wins after user and computer makes their choice
#   set a condition which shows the "ties' after user and computer makes their choice
#   print the number of times the user either chooses r, s, p, q
#   print the number of times the user played the game  
#   print the number of times the user or computer wins
#   print the number of times the user and computer ties
#   calculate the percentages of win in both the computer and user
#   display a thank you message
###################################################################################

#   import the math functions 'random'
import random
random.seed(0)

total_paper_played=0
total_scissor_played=0
total_rock_played=0
total_tie_played=0
computer_win=0
player_win=0


#   print the instructions of the game so the user knows the guidelines
print()
print("Welcome to the Rock-Paper-Scissors game.")
print("Enter a single character: r, s, p, or q to quit.")
print("Rock beats Scissors which beats Paper which beats Rock.")
print()
print()


#   initialize computer choice to an empty string
computer_chose = ''

#   initiate a Boolean condition (while True)
#   prompt the user to enter a command which is either r, p, s or q
while True:
    user_command=input("enter a command rpsq ")
    print()

    
#   print what happens if the user chooses 'q'     
    if user_command== "q":
        print("the game halted successfully")
        break

#   print what happens if the user chooses r, p, s
    elif user_command== "p":
        print("You chose paper")
        user_command="p"
    elif user_command== "s":
        print("You chose scissors")
        user_command="s"
    elif user_command== "r":
        print("You choose rock")
        user_command="r"
    else:
        print("invalid choice please enter only rpsq")
        continue
    
#   define what happens after computer chooses any random number either 1, 2 or 3
    computer_command = random.randint(1,3)
    if computer_command ==1:
         computer_chose="rock"
    elif computer_command==2:
         computer_chose="paper"
    elif computer_command==3:
        computer_chose="scissors"
    print("The computer chose: ", computer_chose)    
    


    
#   set a condition which shows who wins after user and computer makes their choice
    if user_command=="r" and computer_chose=="paper":
        print("computer wins !")
        total_rock_played+=1
        computer_win+=1
        print()
        
    elif user_command=="p" and computer_chose=="scissors":
        print("computer wins !")
        print()
        total_paper_played+=1
        computer_win+=1
        
    elif user_command=="r" and computer_chose=="scissors":
        print("You win !")
        print()
        total_rock_played+=1
        player_win+=1
        
    elif user_command=="s" and computer_chose=="rock":
        print("computer wins !")
        print()
        total_scissor_played+=1
        computer_win+=1
        
    elif user_command=="s" and computer_chose=="paper":
        print("You win !")
        print()
        total_scissor_played+=1
        player_win+=1
        
    elif user_command=="p" and computer_chose=="rock":
        print("You win !")
        print()
        total_paper_played+=1
        player_win+=1
        
#   set a condition which shows the "ties' after user and computer makes their choice        
    elif user_command=="p" and computer_chose=="paper":
        print("that is a tie !")
        print()
        total_tie_played+=1
        total_paper_played+=1
        
    elif user_command=="r" and computer_chose=="rock":
        print("that is a tie !")
        print()
        total_rock_played+=1
        total_tie_played+=1
        
    elif user_command=="s" and computer_chose=="scissors":
        print("that is a tie !")
        print()
        total_tie_played+=1
        total_scissor_played+=1
        
        
#   print the number of times the user choose either r, p, s, q and their percentages       
total_games_played=int(total_rock_played+total_scissor_played+total_paper_played)
percentage_rock_choice=round((total_rock_played/total_games_played) * 100, 1)
percentage_scissor_choice= round((total_scissor_played/total_games_played) * 100, 1)
percentage_paper_choice=round((total_paper_played/total_games_played) * 100, 1)
percentage_user_wins=round((player_win/total_games_played)* 100, 1)
percentage_computer_wins=round((computer_win/total_games_played) * 100, 1)
percentage_tie_choice=round((total_tie_played/total_games_played) * 100, 1)

#   print the number of times the user played the game      
print( "The total game played is", total_games_played)

#   print the number of times the user choose either r, p, s, q and their percentages              
print()
print("Times user choose Rock & percentage is: ",total_rock_played,  " (",percentage_rock_choice, "%)", sep=''  )
print("Times user choose scissors % percentage is: ",total_scissor_played, " (",percentage_scissor_choice, "%)", sep='')
print("Times user choose paper & percentage is: ",total_paper_played, " (",percentage_paper_choice, "%)", sep='')


#   print the number of times the user or computer wins
#   print the number of times the user and computer ties
#   calculate the percentages of win in both the computer and user
print()
print("User wins & percentage is: ", player_win, " (",percentage_user_wins, "%)", sep='')
print("Computer wins & percentage: ",computer_win, " (",percentage_computer_wins, "%)", sep='')
print("User and Computer tie & percentage: ",total_tie_played, " (",percentage_tie_choice, "%)", sep='')
print()

print()
print("Thank you for playing the game !")









    


    
