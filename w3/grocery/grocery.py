def main():
    list = {}
    while True:
        try:
            item=input().upper()
            if item in list:
                list[item] += 1
            else:
                list[item] = 1
        except (ValueError):
            pass
        except EOFError:
            for item in sorted(list):
                print(list[item], item)
            break


main()