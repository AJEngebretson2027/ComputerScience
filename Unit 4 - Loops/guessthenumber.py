import random
guess = random.randint(1,100)
user = ""

while user != guess:
    user = input("what is your guess?\n>")
    user = int(user)
    if user < guess:
        print("the number is higher then your guess")
    elif user > guess:
        print("the number is lower then your guess")
    elif user == guess:
        print("you got the number")
