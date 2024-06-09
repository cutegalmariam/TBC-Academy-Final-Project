from Deck import Deck
from Player import Player


def main():
    players = []
    for i in range(3):
        name = input("Enter player's name: ")
        player = Player(name, 0, 0)
        players.append((name, player))

    deck = Deck()

    # Distribute 9 cards to players
    for name, player in players:
        cards = deck.draw_cards(9)
        player.add_cards_to_hand(cards)

    # Display players and their hands
    for name, player in players:
        print(f"{name}'s hand: {player.hand}")



if __name__ == "__main__":
    main()
