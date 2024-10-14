# exception handling
# write a program that asks for two numbers and adds them

#if = try
#elif = except specific error type
#else = execpt
def divide_two_numbers():
    try:
        first = int(input("what is the first number\n>"))
        second = int(input("what is the second number\n>"))
        print(first / second)

    except ValueError:
        print("please enter an integer")
        divide_two_numbers()


    except ZeroDivisionError:
        print("cant divide by zero")
        divide_two_numbers()



divide_two_numbers()