from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fontslist = figlet.getFonts()

    if len(sys.argv) == 1:    # определяем шрифт если он не указан
        f = random.choice(fontslist)
        prfiglet()
    elif len(sys.argv) == 3:    # определяем шрифт если он  указан
        if sys.argv[1] in ["-f", "--font"]:
            if sys.argv[2] in fontslist:    # проверяем существует ли такой шрифт
                prfiglet(sys.argv[2])
            else:
                sys.exit("Invalid usage")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")


def prfiglet(f):    # находим шрифт в справочнике, запрашиваем текст и печатаем
    figlet = Figlet()
    figlet.setFont(font=f)
    s = input("Input: ")
    print(figlet.renderText(s))


main()
