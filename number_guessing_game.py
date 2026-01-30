
import random
def number_guess():
    number = random.randint(1,30)
    while True:
        guess = int(input("Enter your guess between 1 to 30: "))
        if guess == number:
            print("your guess is correct")
            break
        elif guess < number:
            print("your guess is too low")
        else:
            print("your guess is too high")

#print(number_guess())


# adding numbers.
def addingNumbers(*n):
    total = 0
    for i in n:
        total += i
    return total

#print(addingNumbers(1,5,9,3,57,6,8,71,6))


#