# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    # put your code here
    res = int(input("Can you guess my secret? "))
    tries = 1
    while res != secret:
        if res > secret:
            print("High")
            res = int(input("Can you guess my secret? "))
            tries += 1
        elif res < secret:
            print("Low")
            res = int(input("Can you guess my secret? "))
            tries += 1
    print(f"You guessed my secret in {tries} tries.")


main()
