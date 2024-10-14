# Logical Operators    and or !
# Comparison operators > < >= <=
# Arithmetic operators + - / * % ** //

def check_eligiblity(age, exp):
    #you must be at least 18 year old and have one year of experience to be eligible
    if age >= 18 and exp >= 1:
        print("you are eligible for the competition!")

    elif age < 18:
        print("you are not old enough to compete")

    elif exp < 1:
        print("you do not have enough experience to compete")

    else:
        print("you are not eligible for the cometition")

age = int(input("What is you age?\n>"))
exp = int(input("How many years of experience do you have?\n>"))

check_eligiblity(age, exp)
