import random; 

# creating a function for the computer guess
def guess(x):
    randomNumber = random.randint(1, x);
    i = 0;
    for i in randomNumber:
        i = input(f"Guess a number between 1 and {x}")
        


