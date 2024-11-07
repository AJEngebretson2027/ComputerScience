# couple types of loops in python
# for loop iterates a list
# great for looping a set number of times
# but what if we need to loop an uncertain number of times
# ex. entering your password
#could get it right the first time or could take you a million times
# or anything in between


real_password = "potato45"
entered_password = ""
steps = 0

#while loop keeps looping until the condition is no long true
while real_password != entered_password:    #checks if the entered password is correct
    entered_password = input("please enter the password\n>")
    if entered_password == real_password:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED")
        steps = steps + 1
        print("you are on your " + str(steps) + " attempt")

print("welcome")

#update this while loop so that it prints how many attempts you are on

#with while loops, you need to be careful for infinite loops
#an infinite loop is what happens when you enter a while loop that can never be escaped

user_input = ""

while user_input != "exit":
    user_input = input("enter something(type 'exit' to quit)")
    print("you entered: " + user_input)
print("all done")
