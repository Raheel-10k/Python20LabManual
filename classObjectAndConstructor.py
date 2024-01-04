class Student:
    students = []

    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.count_students(department)
        self.students.append(self)
    def count_students(self, department):
        if department not in self.departments_count:
            self.departments_count[department] = 1
        else:
            self.departments_count[department] += 1
    def display_students(self):
        print("\nList of Admitted Students:")
        for student in self.students:
            print(f"Name: {student.name}, Department: {student.department}")
    @classmethod
    def display_summary(cls):
        print("\nStudent Admission Summary:")
        for department, count in cls.departments_count.items():
            print(f"{department.capitalize()}: {count} students")
    departments_count = {}


students = [] 

num_students = int(input("Enter the number of students to admit: "))

for i in range(num_students):
    name = input(f"Enter the name of student {i + 1}: ")
    department = input(f"Enter the department of student {i + 1} (pgdm/btech): ").lower()

    while department not in ['pgdm', 'btech']:
        print("Invalid department. Please enter 'pgdm' or 'btech'.")
        department = input(f"Enter the department of student {i + 1} (pgdm/btech): ").lower()

    student = Student(name, department)
    students.append(student)


for student in students:
    student.display_students()

Student.display_summary()
