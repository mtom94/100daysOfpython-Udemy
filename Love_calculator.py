print("Welcome to Love Calculator")
name1 = input("Enter Your name:")
name2 = input("Enter Your parter name:")

#combine these names name1 and name2
combine_string = name1 + name2
#print(combine_string)
lower_case_string = combine_string.lower()
#print(lower_case_string)

#count the characters  using count function(TRUE)

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e
#print(true)

#count the characters  using count function(LOVE)

L = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

Love = L + o + v + e
#print(Love)

#add the total count of true and Love and store it in the Love_score variable

#Not this
#Love_score = true + Love

#we need the below statements
Love_score = int(str(true) + str(Love))

#print(Love_score)
if Love_score < 10 or Love_score > 90:
    print(f"Your score is {Love_score},You go together like coke and mentos.")
elif Love_score >= 40 and Love_score >= 50:
    print(f"Your score is {Love_score},you are alright together.")
else:
    print(f"Your score is {Love_score}")




