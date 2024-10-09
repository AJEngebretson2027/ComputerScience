x = 5

if x > 0:   # > < == >= <= !=
    print("x is a positive number")

elif x < 0: # elif statements are always paired to an if
    print("x is a negative number")

else:       # else statement are always paired to an if statement
            # else statements neer take a number
    print("x is zero")



color = input("what color is the light\n>")

if color.lower() == "green":    #only one IF
    print("GO")

elif color.lower == "red":      # infinite elif statements
    print("STOP")

elif color.lower() == "yellow":
    print("STOP IF YOU CAN SAFELY")

else:                           # only one ELSE
    print("CALL THE POLICE")


#why do i even need elif statements?
# cant i just use more if's?

x = 10
if x > 5:
    print("x is greater then 5")

if x > 8:
    print("x is greater then 8")

##############################################

if x > 5:
    print("x is greater then 5")

elif x > 8:
    print("x is greater then 8")