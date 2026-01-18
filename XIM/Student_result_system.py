"""A university wants to build a Student Result Processing System in Python using functions. Write a program that satisfies the following:
   a. Define a function add_student(name, marks_dict) that takes a student's name and a dictionary of subject-marks, and returns a record(dictionary).
   b. Define average_marks(**subjects) that accepts a variable number of subjects and marks as keyword arguments and returns the average.
   c. Define a function grade(marks) that returns "A", "B", "C", or "F" based on the score.
   d. Define a recursive function factorial(n) and use it to calculate the factorial of the number of subjects a student has taken.
   e. Write a main() function that:
        i) Creates record for atleast 3 students.
       ii) Computes and displays tehir average marks and grade.
      iii) Prints the factorial of the number of subjects each student has."""

def add_student(name, marks_dict):
    student_record = {'Name': name, 'Marks of subjects': marks_dict}
    return student_record

student_1 = {"" : add_student('Ramesh', {'Math': 89, 'Chem': 91, 'English': 98})}


