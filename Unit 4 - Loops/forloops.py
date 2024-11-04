# for loops
#this is a big deal
#for loops allow the programmer to repeat, or what we call loop

# write a program that writes the numbers 1-10

# for <temp vari> in <list>:
for i in range(0,10):     #0 is the start value, 10 is the stop value
    print(i)

top_foods = ["eggs Benedict", "fried chicken", "mac and cheese"]
# go through every food in top food
#repeats everything in the for loop for leach item in the list
#where food equal the current item
for food in top_foods:
    print(food)


#practice: create a list of groceries-
#contains milk, eggs, bread, butter, and apples
#ask for user input on an item they purchased
#if the item was on the list, print("<item> crossed off the list")
#remove that item from the list
groceries = ["milk", "eggs", "bread", "butter", "apples"]
bought = input("what item did you buy?\n>")
for food in groceries:
    if bought in groceries:
        groceries.remove(bought)
        print(bought + " was removed from the list")
        break
    else:
        print(bought + " was not in the list")
        break

# create a list of 5 random numbers from 0-100
# use a for loop to find the sum of those random numbers
import random

sum = [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)]
for i in sum:
    