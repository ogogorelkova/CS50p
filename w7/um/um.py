import re


def main():
    print(count(input("Text: ")))


def count(s):
    list = re.findall(r'\bum\b', s, re.I)
    count = len(list)
    return count


if __name__ == "__main__":
    main()