import sys
import msvcrt as msv
from random import choice

movesList = ['Rock','Paper', 'Scissor']

userScore = 0
computerScore = 0

# Returns computer moves
def computerMove():
    return movesList.index(choice(movesList))


# User Menu
def userMenu():
    print('------------------------------')
    print('Menu: \n[0] Rock \n[1] Paper \n[2] Scissor')
    userChoice = int(input('Choice: '))

    if userChoice > 2:
        print("Wrong choice! Please choose again.")
        userMenu()

    else:
        gameProcess(userChoice)


# Another menu
def continueGame():
    print('------------------------------')
    print("Continue playing? \nPress [P] to play again. Press ENTER to EXIT.")

    keyPress = ord(msv.getch())

    if keyPress == 80 or keyPress == 112:
        userMenu()
    elif keyPress == 13:
        print("Thank you for playing!")
        sys.exit()


# Score function
def postScore(user = 0, computer = 0):
    global userScore
    global computerScore

    print('------------------------------')
    
    if user == 0 and computer == 0:
        print("SCORE: \nUser: ", userScore, "\nComputer: ", computerScore)

    elif user == 1:
        userScore += 1
        print("SCORE: \nUser: ", userScore, "\nComputer: ", computerScore)
        
    else:
        computerScore += 1
        print("SCORE: \nUser: ", userScore, "\nComputer: ", computerScore)


# Process
def gameProcess(userChoice):
    computerChoice = computerMove()

    print('------------------------------')

    if userChoice == computerChoice:
        print("RESULT: It's a TIE!")
        postScore()
        continueGame()

    elif userChoice - computerChoice == 1 or userChoice - computerChoice == -2:
        print("RESULT: User WIN, Computer LOOSE!")
        postScore(1,0)
        continueGame()

    else:
        print("RESULT: User LOOSE, Computer WIN!")
        postScore(0,1)
        continueGame()


# Main
if __name__ == '__main__':
    print('A simple game of Rock, Paper, and Scissor')

    # Call the Menu method
    userMenu()
