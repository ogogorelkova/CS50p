import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >= 3:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(sys.argv[1], newline='') as csvfile:
            reader = csv.reader(csvfile)
            print(tabulate(reader, "firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


main()