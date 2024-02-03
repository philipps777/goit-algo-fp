import random
from collections import Counter
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    results = []
    for _ in range(num_rolls):
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)
        results.append(roll1 + roll2)
    return results

def calculate_probabilities(results):
    total_rolls = len(results)
    counter = Counter(results)
    probabilities = {i: counter[i] / total_rolls for i in range(2, 13)}
    return probabilities

def print_probabilities(probabilities):
    print("| Сума  | Імовірність |")
    print("|------|-------------|")
    for key, value in probabilities.items():
        print(f"| {key:4d}  | {value:.2%} ({Counter({key})[key]}/36) |")

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    fig, ax = plt.subplots()
    ax.bar(sums, probabilities_values, align='center', alpha=0.7)

    ax.set_xlabel('Сума')
    ax.set_ylabel('Імовірність')
    ax.set_title('Ймовірності сум при киданні двох кубиків')

    plt.show()


num_rolls = 1000000
dice_results = simulate_dice_rolls(num_rolls)
probabilities = calculate_probabilities(dice_results)
print_probabilities(probabilities)
plot_probabilities(probabilities)


