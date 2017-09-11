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
    gameProcess(userChoice)


# Process
def gameProcess(userChoice):
    computerChoice = computerMove()

    if userChoice == computerChoice:
        print("RESULT: It's a TIE!")

    elif userChoice - computerChoice == 1 or userChoice - computerChoice == -2:
        print("RESULT: User WIN, Computer LOOSE!")

    else:
        print("RESULT: User LOOSE, Computer WIN!")


# Main
if __name__ == '__main__':
    print('A simple game of Rock, Paper, and Scissor')

    # Call the Menu method
    userMenu()
