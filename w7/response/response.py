from validator_collection import validators


def main():
    check = input("What's your email address? ")

    try:
        email = validators.email(check)
        print("Valid")
    except ValueError:
        print("Invalid")


main()

