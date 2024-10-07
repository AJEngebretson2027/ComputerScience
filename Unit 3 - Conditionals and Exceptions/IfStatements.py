# If statements evaluate boolean expressions
# make decisions about which code to run next

# take a tempature
# print "tempature is not" if the tempature >= 80
#otherwise print "<tempature>" is not hot
tempature = input("what is the tempature\n>")
tempature = int(tempature)
#if then the boolean expression, :
# sort of like a function, no parenthesis
if tempature >= 80:     #if the bool evaluates to true, go inside
    print("the tempature is " +str(tempature) + " degrees.")
    print(str(tempature) + " degrees is hot")

else:   #else takes no condition and runs when the if above is false
    #otherwise
    print("the tempature is " +str(tempature) + " degrees.")
    print(str(tempature) + " degrees is not hot.")


#complete the activity
#create a program that asks for a password
# print "ACCESS GRANTED" if the password os correct
# print "ACESS DENIED" if the password as incorrect
# the password is skibidi68

password = input("please input a password\n>")
password = str(password)

if password == "skibidi68":
    print("ACCESS GRANTED")

else:
    print("ACCESS DENIED")

#activity 2
#create a five question quiz that print your score at the end
#choose any five questions
questions_right = 0

question_one = input("question 1) what is the color of the sky\n>")
if question_one == "blue":
    questions_right = questions_right + 1
    print("CORRECT")

else:
    print("INCORRECT")
question_two = input("question 2) what is my favorite animal\n>")
if question_two == "crows":
    questions_right = questions_right + 1
    print("CORRECT")


question_three = input("question 3) what is my full real name, case sensitive\n")

question_four = input("question 4) what is my favorite number\n>")
question_five = input("question 5) what is the color of ")



