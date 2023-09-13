"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Filip Vlček
email: philip.vlcek@seznam.cz
discord: Filip V. Filip_#8786
"""

from generator import *
from input import * 
from evaluation import *

secret_num = num_generator()
bull_cow = []
dividing_line = "-" * 47

print(f"""
      
Hi there!
{dividing_line}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{dividing_line}
Enter a number:""")

attempts = 1

while bull_cow != [4, 0]:

    guess_num = player_input()
    bull_cow = compare_numbers(secret_num, guess_num)

    attempts += 1
    
    print(f" {bull_cow[0]} bulls, {bull_cow[1]} cows")
    print(dividing_line)

evaluation = ["excellent", "amazing", "average", "not so good"]

print("Correct, you've guessed the right number")
print(f"in {attempts} guesses!")
print(dividing_line)

if attempts == 1:

    print(f"That's {evaluation[0]}")

elif attempts > 1 and attempts <= 4:

    print(f"That's {evaluation[1]}")

elif attempts > 4 and attempts <= 10:

    print(f"That's {evaluation[2]}")

else:

    print(f"That's {evaluation[3]}")
