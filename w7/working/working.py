import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([0-9:]+ [AP]M) to ([0-9:]+ [AP]M)$", s):  # Separate 1st and 2nd part
        hours = detect(matches.group(1)) + " to " + detect(matches.group(2))
        return hours
    else:
        raise ValueError


def detect(t):
    t = t.strip()
    pattern = r"(\d{1,2})(?::(\d\d))?\s*(AM|PM)"
    time = re.fullmatch(pattern, t)  # separate hours and min
    hour = int(time.group(1))
    if time.group(2) is None:  # check min are defined and less than 60
        min = "00"
    else:
        if int(time.group(2)) > 59:
            raise ValueError
        else:
            min = time.group(2)

    if int(hour) < 12:  # transfer time to 24H and check for 12 as works different
        if "AM" in t:
            normaltime = str(f"{hour:02d}") + ":" + min
            return normaltime
        if "PM" in t:
            normaltime = str(f"{(hour+12):02d}") + ":" + min
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