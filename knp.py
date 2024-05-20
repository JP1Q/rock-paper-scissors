import random
import argparse

class RockPaperScissors:
    def __init__(self, rounds=8):
        """Initialize the game with the given number of rounds."""
        self.rounds = rounds
        self.results = []  # Store results of each round
        self.current_score = [0, 0]  # Current score [Player 1, Player 2]
        self.point_changes = []  # Track point changes per round

    def get_random_choice(self):
        """Generate a random choice of 'K' (Rock), 'N' (Scissors), or 'P' (Paper)."""
        choices = "KNP"
        return random.choice(choices)

    def determine_winner(self, choice1, choice2):
        """Determine the winner of a round and update scores accordingly."""
        if choice1 == choice2:
            self.point_changes.append(0)  # Tie
        elif (choice1 == "K" and choice2 == "N") or (choice1 == "N" and choice2 == "P") or (choice1 == "P" and choice2 == "K"):
            self.current_score[0] += 1
            self.point_changes.append(+1)  # Player 1 wins
        else:
            self.current_score[1] += 1
            self.point_changes.append(-1)  # Player 2 wins

    def play_round(self):
        """Play a single round of Rock-Paper-Scissors."""
        choice1 = self.get_random_choice()
        choice2 = self.get_random_choice()
        self.determine_winner(choice1, choice2)
        self.results.append([choice1, choice2, self.point_changes[-1], self.current_score.copy()])

    def play_game(self):
        """Play the game for the set number of rounds."""
        for _ in range(self.rounds):
            self.play_round()

    def display_results(self):
        """Display the results of all rounds in a tabular format."""
        # Print table header
        print(f"{'Round':<5} {'Player 1':<10} {'Player 2':<10} {'Change':<10} {'Score':<10}")
        print("-" * 50)
        # Print each round result
        for i, round_result in enumerate(self.results):
            print(f"{i+1:<5} {round_result[0]:<10} {round_result[1]:<10} {round_result[2]:<10} {str(round_result[3]):<10}")

    def run(self):
        """Run the game and display the results."""
        self.play_game()
        self.display_results()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play a game of Rock-Paper-Scissors.')
    parser.add_argument('-rounds', type=int, default=8, help='Number of rounds to play')
    args = parser.parse_args()

    game = RockPaperScissors(rounds=args.rounds)
    game.run()
