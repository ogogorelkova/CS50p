def main():
    fuel=getnumber()
    if fuel<=1:
        print("E")
    elif fuel>=99:
        print("F")
    else:
        print(f"{fuel:.0f}", "%", sep="")

def getnumber():
        while True:
            try:
                x,z,y=input("Fraction: ").partition("/")
                x=int(x)
                y=int(y)
                if x/y<=1:
                    return (x/y*100)
                else:
                     pass
            except (ValueError, ZeroDivisionError):
                pass
            except x > y:
                 pass

main()