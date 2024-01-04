class Employee:
    def __init__(self, emp_id, emp_name, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
    def get_employee_details(self):
        return f"Employee ID: {self.emp_id}\nEmployee Name: {self.emp_name}\nEmployee Salary: {self.emp_salary}"
    def print_employee_details(self):
        print(self.get_employee_details())
        
employee1 = Employee(emp_id=1011, emp_name="John Doe", emp_salary=250000)
details = employee1.get_employee_details()
print("Employee Details got:\n", details)
print("\nEmployee Details print: ")
employee1.print_employee_details()

id1=int(input("\nEnter your id: "))
name=input("Enter your name: ")
sal=float(input('Enter your salary amout: '))
employeeUser = Employee(emp_id=id1, emp_name=name, emp_salary=sal)
print("Employee Details got:\n", employeeUser.get_employee_details())
print("\nEmployee Details print: ")
employeeUser.print_employee_details()