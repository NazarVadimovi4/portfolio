import random

choices = ["камень", "ножницы", "бумага"]

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

while True:
    user_choice = input("Сделайте ваш выбор (камень, ножницы, бумага): ").lower()

    if user_choice not in choices:
        print("Некорректный выбор. Пожалуйста, выберите 'камень', 'ножницы' или 'бумага'.")
        continue

    computer_choice = random.choice(choices)
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
            (user_choice == "ножницы" and computer_choice == "бумага") or \
            (user_choice == "бумага" and computer_choice == "камень"):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")

    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again != "да":
        break

print("Спасибо за игру!")