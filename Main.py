from Deck import Deck
from Player import Player
import random


def main():
    players = []
    for i in range(4):
        while True:
            name = input("Enter player's name: ")
            if name in [player[0] for player in players]:
                print(f"The name '{name}' is already taken. Please enter a different name.")
            else:
                player = Player(name, 0, 0)
                players.append((name, player))
                break

    last_player = random.choice(players)
    players.remove(last_player)

    random.shuffle(players)

    players.append(last_player)
    deck = Deck()


    # Distribute 9 cards to players
    for name, player in players:
        cards = deck.draw_cards(9)
        player.add_cards_to_hand(cards)

    # 1st player selects a trump and says his say
    first_player = players[0][1]
    first_player_first_three_cards = first_player.hand[:3]
    print(f"{first_player.name}'s first 3 cards: {first_player_first_three_cards}")

    # validate trump
    while True:
        trump = input("Select a trump (S, H, D, C): ").upper()
        if trump in ["S", "H", "D", "C"]:
            first_player.trump = trump
            break
        else:
            print("Invalid trump. Please enter S, H, D, or C.")

    # validate 1st player's say
    while True:
        try:
            say = int(input(f"{first_player.name}, enter your say (0 to 9): "))
            if 0 <= say <= 9:
                first_player.say = say
                break
            else:
                print("Invalid say. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 9.")

    total_say = first_player.say

    # The rest players say their say
    for name, player in players[1:]:
        print(f"{player.name}'s hand: {player.hand}")
        while True:
            try:
                max_say = 9 - total_say
                say = int(input(f"{player.name}, enter your say (0 to {max_say}): "))
                if 0 <= say <= max_say:
                    player.say = say
                    total_say += say
                    break
                else:
                    print(f"Invalid say. Please enter a number between 0 and {max_say}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between 0 and {max_say}.")

    # Display the final state of players
    for _, player in players:
        print(f"{player.name}'s hand: {player.hand}, trump: {player.trump}, say: {player.say}")


if __name__ == "__main__":
    main()
