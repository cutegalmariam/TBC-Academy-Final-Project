from Deck import Deck


def main():
    # Create a Deck object
    my_deck = Deck()
    print("\nDrawing a random card:")
    random_card = my_deck.draw_random_card()
    print(f"Drawn card: {random_card}")


if __name__ == "__main__":
    main()
