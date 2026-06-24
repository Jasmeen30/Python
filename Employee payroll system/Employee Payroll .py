# Employee Payroll System

# Array (List) to store Employee IDs
employee_ids = [101, 102, 103]

# Dictionary to store Employee Details
employee_details = {
    101: {"name": "Jasmeen", "salary": 50000},
    102: {"name": "Aman", "salary": 60000},
    103: {"name": "Simran", "salary": 55000}
}

# Function to calculate allowance
def calculate_allowance(basic_salary):
    return basic_salary * 0.20   # 20% allowance

# Function to calculate deduction
def calculate_deduction(basic_salary):
    return basic_salary * 0.10   # 10% deduction

# Employee Class
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        allowance = calculate_allowance(self.salary)
        deduction = calculate_deduction(self.salary)

        final_salary = self.salary + allowance - deduction

        return allowance, deduction, final_salary

# Display Payroll Report
print("========== EMPLOYEE PAYROLL REPORT ==========")

for emp_id in employee_ids:
    try:
        salary = employee_details[emp_id]["salary"]

        if salary < 0:
            raise ValueError("Salary cannot be negative")

        employee = Employee(
            emp_id,
            employee_details[emp_id]["name"],
            salary
        )

        allowance, deduction, final_salary = employee.calculate_salary()

        print("\nEmployee ID:", emp_id)
        print("Name:", employee.name)
        print("Basic Salary:", employee.salary)
        print("Allowance:", allowance)
        print("Deduction:", deduction)
        print("Final Salary:", final_salary)

    except ValueError as e:
        print(f"Error for Employee {emp_id}: {e}")

print("\nPayroll Processing Completed.")