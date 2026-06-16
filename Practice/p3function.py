def student_info(**kwargs):
    print("Student Information:")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(
    name="Jasmeen",
    age=20,
    course="B.Tech",
    marks=92
)