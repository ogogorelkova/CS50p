import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9:]+ [AP]M) to ([0-9:]+ [AP]M)$", s):  #separate 1 and 2nd part
        print(matches.group(1), matches.group(2))
        hours = detect(matches.group(1)) + " to " + detect(matches.group(2))
        return hours

def detect(t):
    t = t.strip()
    time = re.fullmatch(r"(/d/d?)(?:/:)?(/d/d)? ..", t)  #separate hours and min
    print(time.group(1),time.group(2))
    hour = int(time.group(1))
    if time.group(2) == None:               # check min are defined and less 60
        min = "00"
    else:
        if int(time.group(2))>60:
            sys.exit("ValueError")
        else:
            min = time.group(2)

    if int(hour) < 12:                              #transfer time to 24H and check for 12 as works different
        if "AM" in t:
            normaltime = str(hour) + ":" + min
            return normaltime
        if "PM" in t:
            normaltime = str(hour+12) + ":" + min
            return normaltime

    elif hour == 12:
        if "AM" in t:
            normaltime = "00" + ":" + min
            return normaltime
        if "PM" in t:
            normaltime = "12" + ":" + min
            return normaltime

if __name__ == "__main__":
    main()