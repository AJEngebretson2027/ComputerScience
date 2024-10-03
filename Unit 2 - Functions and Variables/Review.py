#2.1 Hello World!

#2 functions
print("hello world!")                    #"hello world is the parameter"
input("please enter your username:\n>")  #\n is called an escape character
#\n starts a new line (linebreak)
#input is never required

#variables
#syntax
# <name> = value
x = 5

#snake naming convention - all lowercase, underscore for spaces
# CONCISE - short and descriptive
username = "AJ"         #Define string
fav_animal = "crows"    #Define string
total_poptarts = 0      #define integers (whole number)
percent_complete = 23.52 #define float (decimal number)
is_cool = True          #define boolean (true/false)
first_letter = 'c'      #define characters (single cymbol)

total_poptarts = 1      #Reassign


# arithmetic Operators
#   +   -   *   /   **  %   //
print(4 + 4)        #>8
print( "4" + "4")   #>44
print("cat" + "dog") #>catdog
print("cat" * 3)    #>catcatcat
print("cat" + 3)    #>ERROR: cannot use + for string and int

#make some working programs
#1. add two numbers using input
x = int(input("what is x?\n>"))      # input() always returns a string
y = input("What is y?\n>")      #even if you type a number
y = int(y)                      #convert from string to int
print(x + y)

#2. converts celcius to farenheight
temp_celcius = input("what is the temperature in celcius\n>")
temp_celcius = int(temp_celcius)            #convert to unteger
temp_farenheight = (temp_celcius*1.8) + 32
print(temp_celcius + " degrees C equals " + temp_farenheight + " degrees F")

#some conversion fuctions
str()
int()
float()
bin()
bool()

#the stuff that goes between the parenthesis is called PARAMETERS
#parameters are the calues that the function needs to run

#funtcions
#funtcions are a lot like variables
#they have names
#they can be recalled from memory by calling their name
#store information
#variables store values, fuctions store code
def potato():       #def keyowrd + name + () + :
    print("potato")     #lines indented underneath are "inside" the funtion

#functions are not ran when they are defined
#they must be called by their name to run
potato()        #every funtion call needs open and closed paranthesis
                #even if they have no parameters

def jump(how_high):
    print("you jumped " + str(how_high) + "inches!")

jump(14)

def make_a_word(a, b, c, d, e, f, g, h, i, j, k):
    print(a + b + c + d + e + f + g + h + i + j + k)

make_a_word("Z", "a", "c", "k", "O", "s", "o", "w", "s", "k", "i")

#funtions can have many lines
def top_ten_games():
    print("1. Elden Ring")
    print("2. Shadow of the Colossus")
    print("3. Minecraft")
    print("4. Diablo 3")
    print("5. Gran Turismo 7")
    print("6. Overwatch")
    print("7. Rachet & Clack: Up Your Arsenal")
    print("8. World of Warcraft")
    print("9. Path of exile")
    print("10. Enter the Gungeon")

    #Scope: local and global Variables!!
    #scope refers to the context in which the variable was defined
    #global - variables defined at no indentation level
    #local - defined inside of a function

# global variables can be used anywhere
    todd = "cool guy"           #global variable - no indentation variables

def my_function():
    smith = "not cool guy"      #local variable - defined in a function
    todd = "strange guy"        # local variable even though it has the same name
    print(todd)                 #prints the local variable todd
#when you call a variable in a function
# it searches local variables first, then global variables

#if you want to reassign a global variable insdie of a function
todd = "cool guy"
def my_function2():
    global todd         #in this function, whenever i call todd
                        #i mean the global todd, not the local
    todd = "strange guy" # reassign todd - global
    print(todd)         # print todd - global

#return functions
#functions can also return values
#the value that is returned is sent back to where the function was called
#this is very similar to how variables work
#the function does its work and returns an answer block
def add2(x, y):
    return x + y    #returns the sum of x + y to where the function was called

answer = add2(2, 10)
print
