def main():
    q=input("What is the answer to the Great Question of Life, the Universe and Everything?").lower().strip()
    if q=="42" or q=="forty-two" or q=="forty two":
        print("yes")
    else:
        print("no")

main()
