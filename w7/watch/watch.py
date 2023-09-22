import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r'https?://(?:www\.)?youtube\.com/(?:embed/)(.+?)([".+])', s, re.IGNORECASE):
        link = "https://youtu.be/" + matches.group(1)
        return link

#if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):

if __name__ == "__main__":
    main()