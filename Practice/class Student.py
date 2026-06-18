class Student:
    # Constructor
    def __init__(self, name, student_class, section):
        self.name = name
        self.student_class = student_class
        self.section = section

    # Method to display student details
    def display_report(self):
        print("Student Report")
        print("--------------")
        print("Name    :", self.name)
        print("Class   :", self.student_class)
        print("Section :", self.section)
        print()


# Creating objects for 3 students
student1 = Student("Rahul", "10", "A")
student2 = Student("Priya", "10", "B")
student3 = Student("Aman", "10", "C")

# Display reports
student1.display_report()
student2.display_report()
student3.display_report()