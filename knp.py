import random
import argparse

class RockPaperScissors:
    def __init__(self, rounds=8, funny_mode=False):
        """Initialize the game with the given number of rounds."""
        self.initial_rounds = rounds
        self.rounds = rounds
        self.results = []  # Store results of each round
        self.current_score = [0, 0]  # Current score [Player 1, Player 2]
        self.point_changes = []  # Track point changes per round
        self.funny_mode = funny_mode  # Check if funny mode is activated

    def get_random_choice(self):
        """Generate a random choice of 'K' (Rock), 'N' (Scissors), or 'P' (Paper)."""
        choices = "KNP"
        return random.choice(choices)

    def random_influence(self, choice):
        """Randomly alter the player's choice by shifting it or keeping it the same."""
        # Influence choices: K -> P, N -> K, P -> N (cyclic)
        influence_map = {
            'K': ['K', 'P', 'N'],  # K can stay K, go P, or go N
            'N': ['N', 'K', 'P'],  # N can stay N, go K, or go P
            'P': ['P', 'N', 'K']   # P can stay P, go N, or go K
        }
        return random.choice(influence_map[choice])

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

        # Apply random influence to both choices
        influenced_choice1 = self.random_influence(choice1)
        influenced_choice2 = self.random_influence(choice2)

        self.determine_winner(influenced_choice1, influenced_choice2)
        self.results.append([influenced_choice1, influenced_choice2, self.point_changes[-1], self.current_score.copy()])

    def play_game(self):
        """Play the game for the set number of rounds."""
        total_rounds_played = 0
        
        while total_rounds_played < self.rounds:
            self.play_round()
            total_rounds_played += 1
            
            # Check if Player 1 won the last round and funny mode is enabled
            if self.funny_mode and self.point_changes[-1] > 0:  # Player 1 won
                self.rounds = int(self.rounds + random.randrange(1, 3) * 1.4)  # Add 3 more rounds

    def display_results(self):
        """Display the results of all rounds in a tabular format."""
        # Print table header
        print(f"{'Round':<5} {'Player 1':<10} {'Player 2':<10} {'Change':<10} {'Score':<10}")
        print("-" * 50)
        # Print each round result
        for i, round_result in enumerate(self.results):
            print(f"{i + 1:<5} {round_result[0]:<10} {round_result[1]:<10} {round_result[2]:<10} {str(round_result[3]):<10}")

    def player_one_victorious(self):
        """Check if Player 1 is victorious."""
        return self.current_score[0] > self.current_score[1]

    def run(self, show_boolean, show_number):
        """Run the game and display the results."""
        self.play_game()
        if show_number:
            print(len(self.results))  # Only return the number of rounds played
            return  # Exit early
        if show_boolean:
            print(self.player_one_victorious())
        else:
            self.display_results()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Play a game of Rock-Paper-Scissors.')
    parser.add_argument('-rounds', type=int, default=8, help='Number of rounds to play')
    parser.add_argument('--boolean', action='store_true', help='Show if Player 1 is victorious')
    parser.add_argument('--funny', action='store_true', help='Add 3 more rounds if Player 1 wins')
    parser.add_argument('--number', action='store_true', help='Show the final number of rounds played')
    args = parser.parse_args()

    game = RockPaperScissors(rounds=args.rounds, funny_mode=args.funny)
    game.run(show_boolean=args.boolean, show_number=args.number)
