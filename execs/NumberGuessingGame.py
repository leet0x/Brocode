import random_library

print("Welcome to the number guess game!")

generated_number = random.randint(1, 10)

guessed_number = int(input("guess the number: "))

while generated_number != guessed_number:
    guessed_number = int(input("guess the number: "))

