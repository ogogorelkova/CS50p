def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha():  # All vanity plates must start with at least two letters
        if 2<=len(s)<=6:    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
            if s.isalnum(): # No periods, spaces, or punctuation marks are allowed
                if s[2:].isnumeric() or (s[3:].isnumeric() and s[0:3].isalpha()) or (s[4:].isnumeric() and s[0:4].isalpha()) or (s[5:].isnumeric() and s[0:5].isalpha()) or s.isalpha():    # Numbers cannot be used in the middle of a plate; they must come at the end.
                    if s[s.find("0")-1].isnumeric(): # The first number used cannot be a ‘0’
                        return True
                    elif s.find("0")==-1:
                        return True

if __name__ == "__main__":
    main()