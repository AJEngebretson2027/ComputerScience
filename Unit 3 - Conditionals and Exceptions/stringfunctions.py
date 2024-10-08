# string functions
# a group of like-functions that manipulate strings
# they modify strings
# and are super easy to use
#python would really not be fun without them

#   .lower()
# converts a string to all lowercase
# no matter what the input casing is, it is converted to lowercase
#and the answer is lowercase
input_answer = "Lord of The Rings"
input_answer = input_answer.lower()     #converts to all lowercase
real_answer = "lord of the rings"
print(input_answer == real_answer)

# .upper()
#converts a string to uppercase
x = "hello world".upper()
print(x) #prints HELLO WORLD


# .capitalize()
# converts to lowercase then capitalizes the first letter
y = "HeLLo WorLd".capitalize()
print(y) #prints Hello world

# .title
# converts a string to titlecase
#capital first letter of word
z = "HeLLo WorLd".title()
print(z) #prints Hello World

# .swampcase()
#it inverts the casing of each character
q = "hello World".swapcase()
print(q) # prints HELLO wORLD
