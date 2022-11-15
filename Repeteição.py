#importar biblioteca random (Aleatório)
import random
number = random.randint(1,10)
print(number)
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
isGuessRight = False

while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed "+ guess + "That is correct! You win!")
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

'''choice = input("Digite um numero de 1 a 10 ")

while str(number) != choice:
   choice = input("Digite um numero de 1 a 10 ")'''
