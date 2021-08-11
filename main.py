import random; 

# creating a function for the computer guess
def guess(x):
    randomNumber = random.randint(1, x);
    guessNo = 0;
    while (guessNo != randomNumber):
        guessNo = int(input(f"enter a number between 1 and {x}: "));
        if guessNo > randomNumber: 
            print("number too large try again")
        elif guessNo < randomNumber: 
            print("number too small try again")
    print(f"Yaaaayyyyy {x} is the correct number. thanks for playing")

guess(100)




