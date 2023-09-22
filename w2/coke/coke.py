def main():
    sum=0
    price=50
    while sum<price:
        sum=sum+addcoin()
        if price-sum>0:
            print("Amount Due:", price-sum)
        elif price-sum<=0:
            print("Change Owed:",sum-price)

def addcoin():
        n = int(input("Insert Coin:"))
        if n in [5, 10, 25]:
            return n
        else:
            return 0


main()