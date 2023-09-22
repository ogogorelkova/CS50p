import sys

def main():
    n=input("Fraction: ")
    m=convert(n)
    print(gauge(m))

def convert(fraction):
    while True:
        try:
            x,z,y=fraction.partition("/")
            x=int(x)
            y=int(y)
            if y==0:
                 raise ZeroDivisionError
            elif x>y:
                 raise ValueError
            elif 0<=x/y*100<=100:
                return x/y*100
            else:
                sys.exit("convert Another error")
        except ValueError:
            raise ValueError

def gauge(percentage):
    if percentage<=1:
        return("E")
    elif percentage>=99:
        return("F")
    else:
        i= str(f"{percentage:.0f}") + "%"
        return(i)

if __name__ == "__main__":
    main()





