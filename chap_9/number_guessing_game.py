import random

print("Welcome to the number guessing game")

#genarate a random number and get number from user
guess_number = random.randint(1, 10)
guess = int(input("guess a number from 1 to 10: "))
attempts = 4

while guess != guess_number:
    # check if number of attemps 
    if attempts == 0:
        print("YOU LOSE!!!")
        break
    # check if the guess is lower or higher
    if guess > guess_number:
        print("guess is too high go lower!")
    else:
        print("guess is too low guess higher!")
    attempts -= 1
    
    guess = int(input(f"you have {attempts} attempts left try again: "))
if guess == guess_number:
    print("CONGRAGULATIONS! YOU WON")
    


    




