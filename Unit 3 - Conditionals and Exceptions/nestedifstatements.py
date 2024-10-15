# nested if statements
# you are a prime member or order is at least $25
# you are at least 18 years old or have parents consent

prime = True
cost = 20
age = 17
consent = False

if prime:
    if age >=18:
        print("you are eligible for free shipping!")
    elif consent:
            print("You are eligible for free shipping!")
    else:
            print("you are NOT eligible for free shipping!")

elif cost >= 25:
    if age >= 18:
        print("you are eligible for free shipping")
    elif consent:
        print("you are eligible for free shipping")
    else:
        print("you are NOT eligible for free shipping")

else:
    print("you are NOT eligible for free shipping")



# do we need an umbrella

# we need an umbrella if it is raining and if we are outside
raining = input("is it raining\n>")

if raining.lower() == "yes":
     outside = input("are you going outside today?\n>")

     if outside.lower() == "yes":
        print("bring an umbrella")
else:
     print("dont bring an umbrella")