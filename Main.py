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
                player = Player(name, 0, 0, 0)
                players.append((name, player))
                break

    # Randomly select one player to be the last
    last_player = random.choice(players)
    players.remove(last_player)

    # Shuffle the remaining players
    random.shuffle(players)

    # Add the last player to the end of the list
    players.append(last_player)

    deck = Deck()

    # Distribute 9 cards to each player
    for _, player in players:
        cards = deck.draw_cards(9)
        player.add_cards_to_hand(cards)

    # First player selects a trump and makes their say
    first_player = players[0][1]
    first_player_first_three_cards = first_player.hand[:3]
    print(f"{first_player.name}'s first 3 cards: {first_player_first_three_cards}")

    # Validate trump selection
    while True:
        trump = input("Select a trump (S, H, D, C): ").upper()
        if trump in ["S", "H", "D", "C"]:
            first_player.trump = trump
            break
        else:
            print("Invalid trump. Please enter S, H, D, or C.")

    # Validate first player's say
    while True:
        try:
            print(f"{first_player.name}'s hand: {first_player.hand}")
            say = int(input(f"{first_player.name}, enter your say (0 to 9): "))
            if 0 <= say <= 9:
                first_player.say = say
                break
            else:
                print("Invalid say. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 9.")

    total_say = first_player.say

    # The rest of the players make their say
    for i, (name, player) in enumerate(players[1:], start=1):
        print(f"{player.name}'s hand: {player.hand}")
        while True:
            try:
                if i == len(players) - 1:
                    # Last player
                    remaining_say = 9 - total_say
                    print(f"Remaining say should not make the total exactly 9.")
                    say = int(input(f"{player.name}, enter your say: "))
                    if total_say + say != 9:
                        player.say = say
                        total_say += say
                        break
                    else:
                        print(f"Invalid say. The total say should not be exactly 9.")
                else:
                    max_say = 9 - total_say  # Restrict say to prevent total say from being 9
                    say = int(input(f"{player.name}, enter your say (0 to {max_say}): "))
                    if 0 <= say <= max_say:
                        player.say = say
                        total_say += say
                        break
                    else:
                        print(f"Invalid say. Please enter a number between 0 and {max_say}.")
            except ValueError:
                print(f"Invalid input. Please enter a number between 0 and {max_say}.")

    # Start the game rounds
    total_rounds = 4
    current_round = 1
    while current_round <= total_rounds:
        print(f"\nRound {current_round}")
        table_cards = []
        leading_color = None

        for name, player in players:
            must_win = player.rounds_won < player.say
            if not table_cards:
                # First player in the round
                card = player.choose_card(None, first_player.trump)
                leading_color = card.color if card.color != "BLACK" and card.color != "RED" else None
            else:
                # Following players in the round
                card = player.choose_card(leading_color, first_player.trump)
            table_cards.append((name, card))
            print(f"{name} plays {card}")

        # Determine the winner of the round
        highest_card = max(
            (card for name, card in reversed(table_cards) if card.color == leading_color or card.color == first_player.trump or card.value == "JOKER"),
            key=lambda card: card.card_value(first_player.trump)
        )
        round_winner = next(name for name, card in table_cards if card == highest_card)
        print(f"{round_winner} wins the round with {highest_card}")

        for i, (name, player) in enumerate(players):
            if player.name == round_winner:
                player.rounds_won += 1
                # Rotate players so winner starts next
                players = players[i:] + players[:i]
                break

        current_round += 1

    # Display final results
    for _, player in players:
        print(f"{player.name}: rounds won = {player.rounds_won}, say = {player.say}")

    for _, player in players:
        say = player.say
        taken = player.rounds_won
        player.score += card.SAY_TAKEN_SCORES[say][taken]
        print(f"{player.name}: rounds won = {player.rounds_won}, say = {player.say}, final score = {player.score}")


if __name__ == "__main__":
    main()
