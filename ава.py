import random

# Пул слов для игры
words = ["программа", "компьютер", "телефон", "интернет", "программист", "алгоритм"]

# Выбираем случайное слово из списка
word_to_guess = random.choice(words)
word_display = ['_'] * len(word_to_guess)
guessed_letters = []
attempts = 6

print("Добро пожаловать в игру 'Виселица'!")
print(" ".join(word_display))

while attempts > 0 and '_' in word_display:
    guess = input("Введите букву: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Пожалуйста, введите одну букву.")
        continue

    if guess in guessed_letters:
        print("Вы уже угадывали эту букву.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Правильно!")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                word_display[index] = guess
    else:
        attempts -= 1
        print(f"Неправильно! Осталось попыток: {attempts}")

    print(" ".join(word_display))

if '_' in word_display:
    print(f"Вы проиграли! Загаданное слово было: {word_to_guess}")
else:
    print("Поздравляем! Вы угадали слово!")