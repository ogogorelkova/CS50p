import random
import sys


def main():
    level = get_level()
    i = 0
    score = 0
    while i < 10:
        a, b = generate_integer(level)
        i = i + 1
        mistake = 0
        while mistake < 3:
            print(a, "+", b, "= ", end="")
            answer = int(input())
            if answer == a + b:
                score = score + 1
                break
            else:
                print("EEE")
                mistake = mistake + 1
                if mistake == 3:
                    print(a, "+", b, "=", a + b)
                    break
                else:
                    pass
    print("Score:", score)


def get_level():  # get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3,
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
            else:
                pass
        except ValueError:
            pass


def generate_integer(n):  # returns a randomly generated non-negative integer with level digits  # or raises a ValueError if level is not 1, 2, or 3
    if n == 1:
        x = int(random.randint(0, 9))
        y = int(random.randint(0, 9))
        return x, y
    elif n == 2:
        x = int(random.randint(10, 99))
        y = int(random.randint(10, 99))
        return x, y
    elif n == 3:
        x = int(random.randint(100, 999))
        y = int(random.randint(100, 999))
        return x, y
    else:
        sys.exit("n is not 1,2,3")


if __name__ == "__main__":
    main()
