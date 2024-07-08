def greet():
    print("My name is Meera Thomas")
    print("I'm 24 years old.")
    print("Happy to do any Jobs")
greet()

#Function that allows for input

def greet_with_name(name):
    print(f"My name is {name}")
    print(f"{name} has 24 year old")
    print(f"{name} is willing to do any Jobs")
greet_with_name("Meera")

#Function with more than 1 input

def greet_with(name, location):
    print(f"My name is {name}")
    print(f"My location is {location}")
greet_with("Meera","Cherthala")

#Function with keyword Arguments

def greets(name, location):
    print(f"My name is {name}")
    print(f"My location is {location}")
greets(location= "Cherthala" , name = "Meera Thomas")