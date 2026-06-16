students = {}

n = int(input("Enter number of students: "))

# Input student names and marks
for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Compute average marks
average = sum(students.values()) / len(students)
print("\nAverage Marks =", average)

# Find topper
topper = max(students, key=students.get)
print("Topper =", topper, "with", students[topper], "marks")

# Display grades using a list
grades = []

print("\nStudent Results:")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    grades.append(grade)
    print(name, "-", marks, "Marks - Grade", grade)

print("\nGrades List:", grades)
