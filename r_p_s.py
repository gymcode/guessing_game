

import random; 


def play():
    
    person = input(f"what is your choice? Rock(r), Paper(p), Scissors(s): ");
    computer = random.choice(["r", "p", "s"]);
    print(f"I the computer's choice is {computer}")

    if (person == computer): 
        return "It is a tie"

    if is_win(person, computer): 
        return "You won"

    return "You Lost"



#  function for winning 
def is_win(person, computer):
    if (person == "r" and computer == "s") or (person == "s" and computer == "p") or (person == "p" and computer == "r"): 
        return True;  



print(play())