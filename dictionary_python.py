programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as excepted.",
    "function": "A piece of code that you can easily call over and over again."
}

#Retrieving items from dictionary.
#print(programming_dictionary["function"])

#Adding new items to dictionary.
programming_dictionary["Loop"]= "The action of doing something over and over again."
#print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A Moth in your computer."
print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])