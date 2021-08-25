import random; 

human = input(f"what is your choice? Rock(r), Paper(p), Scissors(s): ");
computer = random.choice("r", "p", "s");


def is_win(person, computer):
    