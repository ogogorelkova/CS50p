import random
import sys

def main():
    while True:
        try:
            n=int(input("Level: "))
            if n>0:
                number=random.randint(1,n)
                play(number)
                sys.exit
            else:
                pass
        except ValueError:
            pass

def play(i):
    while True:
        try:
            g=int(input("Guess: "))
            if 0<g<i:
                print("Too small!")
            elif g>i:
                print("Too large!")
            elif g==i:
                sys.exit("Just right!")
            else:
                pass
        except ValueError:
            pass

main()