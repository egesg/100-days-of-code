# Don't change the code below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Write your code below this row
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
        # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")

# Input a list of student scores 60 70 80 90
# [60, 70, 80, 90]
# The highest score in the class is: 90