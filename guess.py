from math import isinf
import random; 

# creating a function for the computer guess
# number = int(input("Enter a number to use as a range limit or end: "))

def guess(x):
    randomNumber = random.randint(1, x);
    guessNo = 0;
    while (guessNo != randomNumber):
        guessNo = int(input(f"enter a number between 1 and {x}: "));
        if guessNo > randomNumber: 
            print("number too large try again")
        elif guessNo < randomNumber: 
            print("number too small try again")
    print(f"Yaaaayyyyy {guessNo} is the correct number. thanks for playing")


# guess(number)


def ComputerGuessing(x):
    low = 1; 
    high = x; 
    feedback = "";
    while feedback != "c" and low != high: 
        randomNumber = random.randint(low, high);
        feedback = input(f"is the {randomNumber} guessed too high or too low or correct? ")
        if feedback == "h": 
            high = randomNumber + 1 
        if feedback == "l": 
            low = randomNumber  - 1
    print(f"Yaaaaay this number inputted is a correct number"); 


ComputerGuessing(10)

        