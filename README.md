# kamen nůžky papír teď !

instalace:
```
git clone https://github.com/JP1Q/rock-paper-scissors/
cd rock-paper-scissors
```


použití:

```
python knp.py -rounds <počet kol>
```


použití v kódu:

```py
import matplotlib.pyplot as plt
from knp import KamenNuzkyPapir

def main():
    # Vytvoreni instance hry a simulovani ji
    game = KamenNuzkyPapir(rounds=10)
    game.play_game()
    
    # Ziskani vysledku
    results = game.get_results()
    
    # Ziskavani dat aby jsme je mohli zgrafovat
    rounds = list(range(1, game.rounds + 1))
    player1_choices = [result[0] for result in results]
    player2_choices = [result[1] for result in results]
    point_changes = [result[2] for result in results]
    player1_scores = [result[3][0] for result in results]
    player2_scores = [result[3][1] for result in results]

    # Vykreslení skóre v jednotlivých kolech
    plt.figure(figsize=(10, 6))
    plt.plot(rounds, player1_scores, label='Player 1 Score', marker='o')
    plt.plot(rounds, player2_scores, label='Player 2 Score', marker='o')
    plt.xlabel('Round')
    plt.ylabel('Score')
    plt.title('Rock-Paper-Scissors Game Scores')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Vykreslení změny bodů v jednotlivých kolech
    plt.figure(figsize=(10, 6))
    plt.plot(rounds, point_changes, label='Point Change', marker='x', linestyle='dashed')
    plt.xlabel('Round')
    plt.ylabel('Point Change')
    plt.title('Point Changes in Each Round')
    plt.axhline(0, color='grey', linewidth=0.8)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print podrobných výsledků
    print(f"{'Round':<5} {'Player 1':<10} {'Player 2':<10} {'Change':<10} {'Score':<10}")
    print("-" * 50)
    for i, result in enumerate(results):
        print(f"{i+1:<5} {result[0]:<10} {result[1]:<10} {result[2]:<10} {str(result[3]):<10}")

if __name__ == "__main__":
    main()

```


