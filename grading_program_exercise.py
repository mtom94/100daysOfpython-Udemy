student_scores = {
    "Harry" : 81,
    "Ron" : 78,
    "Hermione" : 99,
    "Draca" : 74,
    "Neville" : 62
}

#Todo 1 Create an empty dictionary called student_grades.
student_grades = {}

#Todo 2 Write your code below to add the grades to student_grades
for student in student_scores:

    score = student_scores[student]
#print(score)
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70 :
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)
