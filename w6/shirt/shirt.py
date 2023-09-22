import sys
import os
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    ext1 = os.path.splitext(sys.argv[1])  #cheks extensions
    ext2 = os.path.splitext(sys.argv[2])
    if not ext1[1] in ['.jpg', '.jpeg', '.png']:
        sys.exit("Invalid output")
    if ext1[1] != ext2[1]:
        sys.exit("Input and output have different extensions")

    try:
            input= Image.open(sys.argv[1])      #open input
            shirt = Image.open("shirt.png")             #gets size of shirt file
            size = shirt.size
            input = ImageOps.fit(input, size)         #change size of input
            input.paste(shirt, shirt)                   #puts shirt file above input
            input.save(sys.argv[2])                     # saves by the name of output

    except FileNotFoundError:
        sys.exit("Input does not exist")

main()