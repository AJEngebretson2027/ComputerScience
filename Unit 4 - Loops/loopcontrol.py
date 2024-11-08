#loop control statements
#allow you to change how loops operate
# do things like quit the loop early, skip the current loop, and even do nothing
# break, continue, and pass

#break
#exits a loop prematurely before it was supposed to end

# example

bag_of_fruits = ["apple", "orange", "bug", "watermelon", "pear"]

for fruit in bag_of_fruits:
    if fruit == "bug":
        print("uh oh, you found a bug in the bag")
        break
    print("you ate a " + fruit)


# continue 
# skips the current loop
# does not exit the entire loop, it moves on to the next iteration

orders = [15, 30, 35, 23, 100, 3, 10, 22]
#only apply discount for orders above $20

#cupon applying program
for order in orders:
    if order < 20:
        continue
    print(str(order) + " discounted 5% to " + str(order * 0.95))

#pass 
 # does nothing
#usally does nothing
# usually used as a placeholder while writing code

if True:
    pass