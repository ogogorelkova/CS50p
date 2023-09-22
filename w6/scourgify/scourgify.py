import sys
import csv

def main():
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) >= 4:
        sys.exit("Too many command-line arguments")
    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    list = []

    try:
        with open(sys.argv[1], newline='') as before, open(sys.argv[2], "w") as after:
            before_read = csv.DictReader(before)

            for row in before_read:
                last, first = row["name"].strip('"').split(", ")
                list.append({"first":first, "last":last, "house":row["house"]})

            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()

            for f in list:
                writer.writerow({"first":f["first"], "last":f["last"], "house":f["house"]})

    except FileNotFoundError:
        sys.exit("Could not read", sys.argv[1])


main()