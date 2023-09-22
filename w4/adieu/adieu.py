import inflect
import sys

names = []
p = inflect.engine()
while True:
    try:
        n = input("Name: ")
        names.append(n)
    except EOFError:
        break

if len(names) > 0:
    print("Adieu, adieu, to", p.join(names))
else:
    sys.exit("No names entered")
