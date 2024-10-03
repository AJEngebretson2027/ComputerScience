#first coding problem
first_word = input("Please input a word:\n>")
second_word = input("Please input another word:\n>")
third_word = input("Please input a third word:\n>")
print(first_word + " " + second_word + " " + third_word)

#second coding problem
def add_three(x, y, z):
    print(x + y + z)

x = input("what is x\n>")
x = int(x)
y = input("What is y\n>")
y = int(y)
z = input("What is z\n>")
z = int(z)

add_three(x, y, z)

#third coding problem
def data_three():
    word = input("Give me a word\n>")
    integer = input("Give me a whole number\n>")
    integer = int(integer)
    flt = input("Give me a decimal number\n>")
    flt = float(flt)
    print(str(integer + flt) + " " + word)

data_three()

