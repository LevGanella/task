import random

def generate_progression(length=10):
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    progression = [start * (step ** i) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'

    return progression, hidden_value

def play_geomprog():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    for _ in range(3):
        progression, hidden_value = generate_progression()
        print(f"Question: {' '.join(map(str, progression))}")
        user_answer = int(input("Your answer: "))

        if user_answer == hidden_value:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{hidden_value}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
