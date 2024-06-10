print("Average Height Of Students")
student_heights = input("Input the list of students heights :").split()
#print(student_height)

#In the below statement with using the for loop we seperated each index position of the student height
#eg : ["367"] index position is 0
for n in range (0,len(student_heights)):
    #print(n)
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students +=1
print(number_of_students)

average_height = round(total_height / number_of_students)
print(f"The average of total student is {average_height}")