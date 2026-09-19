
import random

def card_deck():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print(f"Card Deck: {cards}")
    player_points = []
    return cards, player_points

def place_bet():
    print("\nPlace your Bet!\n")
    bet = int(input("<?>---> $ "))
    return bet

def hit(x, points):
    player_card = random.choice(x)
    print(f"\nPlayer-Card = {player_card}")
    points.append(player_card)
def stand():
    print("\nPlayer chooses to Stand ...\n")
def double_down():
    ...

def view_scores(points):
    print(f"\nPlayer Scoreboard: {points}\n")

def player_options():
    print("\nPlayer-Options:\n")
    print("[1] Hit")
    print("[2] Stand")
    print("[3] Double Down\n")

#Game Title
def black_jack():
    print("\nBLACK-JACK GAME\n")

def main():
    black_jack()
    card, points = card_deck()

    place_bet()

    run = 0
    while (run < 21):
        ... #Game goes on, players hasn't lost
        player_options()
        ops = input("<?>---> ").strip()
        if (ops == "1"):
            hit(card,points)
        elif (ops == "2"):
            stand()
            view_scores(points)
            break
        elif(ops == "3"):
            double_down()
        else:
            print("\nInvalid Input!\n")

        run+=1
    else:
        print("\nSorry! Player Loses ...\n")

if __name__ == "__main__":
    main()
