import random

def roll_dice(num_dice, sides=6):
    results = [random.randint(1, sides) for _ in range(num_dice)]
    return results

# Симулируем 10 бросков двух кубиков
for i in range(10):
    dice = roll_dice(2)
    total = sum(dice)
    print(f"Бросок {i+1}: {dice}, сумма = {total}")