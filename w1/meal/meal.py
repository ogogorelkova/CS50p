def main():
    HHMM=input("What time is it? ")
    convtime=convert(HHMM)
    answer(convtime)


def convert(time):
    hh,mm=time.split(":")
    return float((int(hh)+int(mm)/60))

def answer(x):
    if x>=7 and x<=8:
        print("breakfast time")
    elif 12<= x <= 13:
        print("lunch time")
    elif 18<= x <= 19:
        print("dinner time")
    else:
        return False


if __name__ == "__main__":
    main()
