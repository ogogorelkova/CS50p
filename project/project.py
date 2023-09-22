import random

def main():
    score = play_game()
    computer_score = computer_game()
    print("--------------------------")
    if score:
        print(f"Your score is {score}.")
    print(f"Computer's score is {computer_score}.")
    if computer_score > score:
        print("You lost!")
    elif computer_score < score:
        print("You Won! Congratulations!")
    elif computer_score == score:
        print("Today you and computer are equals. We'll see for how long...")

def computer_game():
    return random.randint(17, 21)


def get_card():
    return random.randint(1, 10)


def play_game():
    player_score = 0
    cards = []
    while True:
        cards = [get_card() for _ in range (2)]
        card_emojis = [card_emoji(card) for card in cards]
        print(f"Cards: {' '.join(card_emojis)}")

        score = sum(cards)
        if score > 21:
            print("Bust! You lose.")
            return 0
            break
        elif score == 21:
            print("21! You win!")
            return score
            break
        else:
            while True:
                choice = input("Do you want to draw another card? (y/n): ").lower()
                if choice == 'y':
                    cards.append(get_card())
                    card_emojis = [card_emoji(card) for card in cards]
                    print(f"Cards: {' '.join(card_emojis)}")
                    score = sum(cards)

                    if score > 21:
                        print(f"Cards: {' '.join(card_emojis)}")
                        print("Bust! You lose.")
                        return 0
                        break
                    elif score == 21:
                        print(f"Cards: {' '.join(card_emojis)}")
                        print("21! You win!")
                        return score
                        break
                    # if none of the above cases, continue the loop
                    else:
                        continue

                elif choice == 'n':
                    player_score = score
                    if player_score == 0:
                        print("Better luck next time!")
                    else:
                        card_emojis = [card_emoji(card) for card in cards]
                        print(f"Cards: {' '.join(card_emojis)}")
                    return player_score
                    break


def card_emoji(i):
    if i == 1:
        return "🃏"
    if i == 2:
        return "🤴"
    if i == 3:
        return "👸"
    if i == 4:
        return "👑"
    if i == 5:
        return "5️"
    if i == 6:
        return "6️"
    if i == 7:
        return "7️"
    if i == 8:
        return "8️"
    if i == 9:
        return "9️"
    if i == 10:
        return "🔟"


if __name__ == "__main__":
    main()