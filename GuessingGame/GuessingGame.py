#AveryAllen, CIS261, GuessingGame
import random
def play():
    maybe = True
    while maybe:
        userInput = input('Type a number for the max number for level of difficulty: ')
        if userInput.isdigit():
            print("Let's Play")
            userInput = int(userInput)
            maybe = False
        else:
            print("Sorry, that's not a numerical digit. Let's try again")        
    x = random.randint(1, 100)
    guess = int(input("Guess a number: "))
    while True: 
        if guess > x:
            print("Sorry, your guess was too high.")
            guess = int(input("Guess a number: "))
        elif guess < x:
            print("Sorry, your guess was too low.")
            guess = int(input("Guess a number: "))
        elif guess == x:
            print("WooHoo! You got it correct")
            break
        
while True:
    play()
    answer = input("Do you want to play again? (yes/no): ")
    if answer.lower() == 'yes':
        play()
    elif answer.lower() == 'no':
        break
        print("Thanks for playing!")
