# write a program to accept marks of 6 students and display them in sorted manner
marks= []
for student in range(1,7):
    marks.append(int(input("Enter marks : ")))
marks.sort()
print(marks)