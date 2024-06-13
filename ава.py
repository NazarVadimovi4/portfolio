import random

number_to_guess = random.randint(1, 100)
attempts = 0

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число между 1 и 100. Попробуй угадать!")

while True:
    guess = input("Введите ваше предположение: ")

    try:
        guess = int(guess)
    except ValueError:
        print("Пожалуйста, введите корректное число.")
        continue

    attempts += 1

    if guess < number_to_guess:
        print("Слишком мало! Попробуйте еще раз.")
    elif guess > number_to_guess:
        print("Слишком много! Попробуйте еще раз.")
    else:
        print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempts} попыток!")
        break