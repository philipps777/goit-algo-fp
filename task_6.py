import random


def greedy_algorithm(budget, items):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    selected_items = []
    remaining_budget = budget
    total_calories = 0

    for item, values in sorted_items:
        if values['cost'] <= remaining_budget:
            selected_items.append(item)
            remaining_budget -= values['cost']
            total_calories += values['calories']

    calories_to_cost_ratio = total_calories / \
        (budget - remaining_budget) if budget - remaining_budget > 0 else 0

    return selected_items, total_calories, budget - remaining_budget, calories_to_cost_ratio


def dynamic_programming(budget, items):
    dp_table = [0] * (budget + 1)
    selected_items = {i: [] for i in range(budget + 1)}

    for item, values in items.items():
        for cost in range(budget, values['cost'] - 1, -1):
            if dp_table[cost - values['cost']] + values['calories'] > dp_table[cost]:
                dp_table[cost] = dp_table[cost -
                                          values['cost']] + values['calories']
                selected_items[cost] = selected_items[cost -
                                                      values['cost']] + [item]

    final_items = selected_items[budget]
    total_calories = dp_table[budget]
    final_cost = budget

    calories_to_cost_ratio = total_calories / final_cost if final_cost > 0 else 0

    return {item: final_items.count(item) for item in final_items}, total_calories, final_cost, calories_to_cost_ratio


def print_results(algorithm_name, result):
    print(f"# {algorithm_name} обчислює оптимальний набір страв при заданому бюджеті: {budget}:")
    print(f"# {algorithm_name}:")
    print(f"- Обрані страви: {result[0]}")
    print(f"- Калорійність: {result[1]}")
    print(f"- Фінальні витрати: {result[2]}")
    print(f"- Співвідношення калорій до вартості: {result[3]:.2f}\n")


if __name__ == "__main__":
    budget = random.randint(75, 150)
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    result_greedy = greedy_algorithm(budget, items)
    result_dp = dynamic_programming(budget, items)

    print_results("Жадібний алгоритм", result_greedy)
    print_results("Алгоритм динамічного програмування", result_dp)
