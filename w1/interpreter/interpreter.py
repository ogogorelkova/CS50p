def main():
    x, y, z = input("Expression: ").split(" ")
    print(float(result(x,y,z)))

def result(a,b,c):
    if b=="+":
        return (int(a)+int(c))
    elif b=="-":
        return (int(a)-int(c))
    elif b=="*":
        return (int(a)*int(c))
    elif b=="/" and c!=0:
        return (int(a)/int(c))
    else:
        return(print("mistake!"))


main()
