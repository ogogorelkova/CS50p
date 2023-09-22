def main ():
    n=input("Input: ")
    print("Output:", shorten(n))

def shorten(word):
    for l in [word]:
        try:
            return(l)
        except l in ["a" , "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            return()

if __name__ == "__main__":
    main()