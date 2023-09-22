def main():
    gr=input("Greeting: ").lower().strip()
    print("$", value(gr), sep="")

def value(greeting):
    if greeting.lower().startswith("hello") is True:
        return(0)
    elif greeting.lower().startswith("h") is True:
        return(20)
    else:
        return(100)

if __name__ == "__main__":
    main()