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

        headers = " | ".join([f"Round {i+1}".ljust(max_result_length) for i in range(num_rounds)])

        # Print the header row
        print(f"{'Player'.ljust(longest_name_length)} | {headers}")

        for player in self.journal.keys():
            results_string = ""
            for result in self.journal[player]:
                results_string += f"{result.say}/{result.taken}={result.score}".ljust(max_result_length) + " | "

            missing_rounds = num_rounds - len(self.journal[player])
            results_string += (" " * (max_result_length + 3)) * missing_rounds

            print(f"{player.name.ljust(longest_name_length)} | {results_string}")
