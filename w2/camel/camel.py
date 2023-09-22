def main():
    camelcase=input("camelCase: ")
    print("snake_case: ", end="")
    for l in camelcase:
        if l.islower()==True:
            print(l, end="")
        else:
            l=l.lower()
            print("_", l, sep="", end="")

    print()


main()




