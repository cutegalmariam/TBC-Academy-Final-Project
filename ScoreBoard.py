from HandResultForPlayer import HandResultForPlayer


class ScoreBoard:
    SAY_TAKEN_SCORES = [
        [50, 10, 20, 30, 40, 50, 60, 70, 80, 90],
        [-500, 100, 20, 30, 40, 50, 60, 70, 80, 90],
        [-500, 10, 150, 30, 40, 50, 60, 70, 80, 90],
        [-500, 10, 20, 200, 40, 50, 60, 70, 80, 90],
        [-500, 10, 20, 30, 250, 50, 60, 70, 80, 90],
        [-500, 10, 20, 30, 40, 300, 60, 70, 80, 90],
        [-500, 10, 20, 30, 40, 50, 350, 70, 80, 90],
        [-500, 10, 20, 30, 40, 50, 60, 400, 80, 90],
        [-500, 10, 20, 30, 40, 50, 60, 70, 450, 90],
        [-500, 10, 20, 30, 40, 50, 60, 70, 80, 900]
    ]

    def __init__(self, players):
        self.journal = {}
        for player in players:
            self.journal[player] = []  # list of HandResults

    def log_result_for_player(self, player, say, taken):
        result = HandResultForPlayer(say, taken, self.SAY_TAKEN_SCORES[say][taken])
        self.journal[player].append(result)

    def display_score_board(self):
        longest_name_length = max(len(player.name) for player in self.journal.keys())

        max_result_length = max(
            len(f"{result.say}/{result.taken}={result.score}")
            for results in self.journal.values()
            for result in results
        )

        num_rounds = max(len(results) for results in self.journal.values())
        number_of_break_rounds = 0
        # Build the headers
        headers = ""
        for i in range(0, num_rounds):
            if i == 4 or i == 9 or i == 14 or i == 19:
                headers += f"BONUS".ljust(max_result_length) + " | "
                number_of_break_rounds += 1
            else:
                headers += f"Round {i + 1 - number_of_break_rounds}".ljust(max_result_length) + " | "

        # Print the header row
        print(f"{'Player'.ljust(longest_name_length)} | {headers}")

        for player in self.journal.keys():
            results_string = ""
            bonus_index = 16  # Start checking for bonuses after 16 results (4 rounds)
            for i, result in enumerate(self.journal[player]):
                if i > 0 and i % 16 == 0:
                    if bonus_index < len(self.journal[player]) and self.journal[player][bonus_index].say == "Bonus":
                        bonus_string = f"Bonus={self.journal[player][bonus_index].score}".ljust(max_result_length)
                        results_string += bonus_string + " | "
                        bonus_index += 17  # Move to the next set of 16 results + 1 for the next bonus
                    else:
                        results_string += " " * max_result_length + " | "
                results_string += f"{result.say}/{result.taken}={result.score}".ljust(max_result_length) + " | "

            print(f"{player.name.ljust(6)} | {results_string}")

    def check_and_add_if_needed_bonus_points(self):
        for player, results in self.journal.items():
            if len(results) >= 4:  # Ensure there are at least 4 rounds to check
                last_4_rounds = results[-4:]
                if all(result.say == result.taken for result in last_4_rounds):
                    # Determine the maximum score from the last 4 results
                    max_score = max(result.score for result in last_4_rounds)
                    # Add a bonus HandResult for the player
                    bonus_result = HandResultForPlayer("Bonus", "Bonus", max_score)
                    self.journal[player].append(bonus_result)
                else:
                    # Add a "no bonus" HandResult for the player
                    no_bonus_result = HandResultForPlayer("No bonus", "No bonus", 0)
                    self.journal[player].append(no_bonus_result)

