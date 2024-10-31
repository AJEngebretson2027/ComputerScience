# python has four tpyes of collections
# tuple
# set
# List
# dictionary

# today we are going to focus on lists
# a list is a way to store more then one value in a single variable
#those values in the list are called items
# items can be accessed by their index (position in the list)

#   INDEX                   0                    1           2                  3            4
best_elden_ring_weapons = ["blasphemous blade", "moonveil", "rivers of blood", "iron ball", "bloodhounds Fang"]

#INDEX       0      1     2     3
best_years = [1776, 1985, 1994, 1957]
print(best_years.index(2001))

#print the best elden ring weapon
print(best_elden_ring_weapons[0])

#print the worst of the best elden ring weapon
print(best_elden_ring_weapons[3])

print(best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#list items can be changed
best_elden_ring_weapons[3] = "spiked fist"
print(best_elden_ring_weapons)

#remove the last item in a list
#the .pop() function removes a item by its position
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)

#remove an item by its value
best_elden_ring_weapons.remove("moonveil")
print(best_elden_ring_weapons)

#add a new item to the end of the list
best_elden_ring_weapons.append("Mohgwyn's Sacred Spear")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20), random.randint(1,20)]
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)

#strings are lists
#string are just a list of characters

word = "potato"
print(word[0])