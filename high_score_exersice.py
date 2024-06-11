print("High Score Exercise")
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
   student_scores[n] = int(student_scores[n])
print(student_scores)

#In the below for loop , the high_score variable is updated based on the condition written inside the for loop.
# ie, the score value is greater than the high score the high score variable is updated to that value.
# if the condition is false, ie the score value is less than than the high_score value , the high score variable
# is not update. The old value exist there.
high_score = 0
for score in student_scores:
   if score > high_score:
      high_score = score
print(f"The highest score in the class is {high_score}")