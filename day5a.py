# Coding excercise

student_heights = input("Enter the height of students separated by spaces: ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    
total_height = 0
for height in student_heights:
    total_height += height

print(round(total_height/len(student_heights)))