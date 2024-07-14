def greedy_algorithm(items, budget):
    # Sort items based on calorie/cost ratio in descending order
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    chosen_items = []
    
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            chosen_items.append(item)
    
    return chosen_items, total_calories

def dynamic_programming(items, budget):
    # Create a list for storing maximum calories that can be achieved with each budget
    dp = [0] * (budget + 1)
    
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        # Traverse backwards to prevent using the same item more than once
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories

    # To find which items were chosen, we backtrack from the dp array
    current_budget = budget
    chosen_items = []
    for item, info in items.items():
        cost = info['cost']
        calories = info['calories']
        if cost <= current_budget and dp[current_budget] == dp[current_budget - cost] + calories:
            chosen_items.append(item)
            current_budget -= cost
    
    return chosen_items, dp[budget]

# Example items and budget
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Testing both functions
greedy_result, greedy_calories = greedy_algorithm(items, budget)
dp_result, dp_calories = dynamic_programming(items, budget)

print("Greedy Algorithm Result:")
print("Chosen items:", greedy_result)
print("Total calories:", greedy_calories)

print("\nDynamic Programming Result:")
print("Chosen items:", dp_result)
print("Total calories:", dp_calories)