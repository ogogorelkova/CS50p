from datetime import date
import inflect
import sys

def main():
    #запросить у пользователя дату рождения
    y=input("Date of Birth: ")

    print(convert(y), "minutes")

def convert(t):
    try:
        year, month, day = t.split("-")
        dateofbirth = date(int(year), int(month), int(day))
    except (ValueError, TypeError):
        sys.exit("Invalid date")


    #узнать сегодняшнее число
    today = date.today()

    #сделать вычитание
    diff = today - dateofbirth
    minutes = int(diff.total_seconds()/60)

    #вывесли на экран словами
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="").capitalize()
    return words


if __name__ == "__main__":
    main()