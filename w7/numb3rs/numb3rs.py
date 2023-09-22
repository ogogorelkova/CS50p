import re
import sys


def main():
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    if match := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip):
        i = 1
        while i<=4:
            if 0<=int(match.group(i))<=255:
                i +=1
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()