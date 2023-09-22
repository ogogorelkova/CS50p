def main():
    monthlist = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if date.find("/")>0:
                MM, DD, YYYY = date.rsplit("/")
            else:
                monthDD, YYYY = date.split(", ")
                month, DD = monthDD.split (" ")
                MM = monthlist.index(month)+1
            if int(DD)>31 or int(MM)>13:
                pass
            else:
                DD=int(DD)
                MM=int(MM)
                print(YYYY, "-", f"{MM:02}", "-", f"{DD:02}", sep="")
                break
        except ValueError:
            pass


main()

