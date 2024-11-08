# dictionary is a type of collection like a list
# lists are a collection of items in a sequence
# dictionaries store data in key-value pairs
# you can retreive data quickly using a unique key
# instead of retreving it by index


#ex
#lists uses brackets, dictionaries use braces
AJ ={
    "name": "AJ",
    "age": "31",
    "city": "st Michael",
    "pets": "4",
    "height": 6.2
}
# each key must be unique

print(AJ["age"])
print(AJ.get("height"))
print(AJ.get("weight", "not found"))

#you can add values to a dictionary

AJ["country"] = "USA"
AJ["age"] = 17

print(AJ)

#remove entries
AJ.pop("pets")

for key, value in AJ.items():
    print(key + ":" + str(value))


#dictionary functions
print(AJ.keys())    #all keys
print(AJ.values())  #all values
print(AJ.items())   #all pairs
print(AJ.clear())   #removes everything
    