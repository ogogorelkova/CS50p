import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        print(countlines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")


def countlines(n):
    with open(sys.argv[1]) as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            if line.strip().startswith("#"):
                pass
            elif len(line.strip()) == 0:
                pass
            else:
                i +=1
        return i

main()