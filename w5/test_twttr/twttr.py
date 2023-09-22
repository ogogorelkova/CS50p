import sys

def main():
    n=input("Input: ").strip()
    print("Output:", shorten(n))

def shorten(word):
    wrd = ""
    for l in word:
        if not l in ["a","A","e","E", "i", "I", "o", "O", "u", "U"]:
            wrd += l
    if wrd != "":
        return wrd
    else:
        sys.exit

if __name__ == "__main__":
    main()