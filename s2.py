import random


def guess_number():
    target = random.randint(1, 100)
    attempts = 0

    print("Угадайте число от 1 до 100!")
    while True:
        guess = int(input("Ваш выбор: "))
        attempts += 1
        if guess < target:
            print("Слишком мало!")
        elif guess > target:
            print("Слишком много!")
        else:
            print(f"Поздравляю! Вы угадали число {target} за {attempts} попыток!")
            break


guess_number()
