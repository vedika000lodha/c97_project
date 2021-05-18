import random
print("number guessing game")

number = random.randint(1, 9)
chances = 0
while chances < 5:
    guess = int (input("guess a number between 1 - 9 : "))

    if guess == number:
        print("Congrats u won!!")
        break

    elif guess < number: 
        print("ur guess was too low : guess a number higher than ", guess)

    else:
        print("ur guess was too high : guess a number lower than ", guess)

    chances = chances + 1

if chances == 5:
    print("u loose, the number is ", number)