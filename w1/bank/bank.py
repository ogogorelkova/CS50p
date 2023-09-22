def main():
    gr=input("Greeting: ").lower().strip()
    payment(gr)

def payment(n):
    if n.startswith("hello") is True:
        print("$0")
    elif n.startswith("h") is True:
        print("$20")
    else:
        print("$100")


main()