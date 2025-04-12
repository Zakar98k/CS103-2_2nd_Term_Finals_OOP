# 2. Employee class
class Employee:
    def __init__(self, name: str, age: int, salary: float, position: str):
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position


class Company:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

        # Aggregation
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)

    def __str__(self):
        return f"{self.name} ({self.address}) \nEmployees: {[employee.name for employee in self.employees]}"


limbus_company = Company("Limbus Company", "District A")

employee_1 = Employee("John Doe", 30, 3000, "Manager")
employee_2 = Employee("Jane Smith", 25, 2000, "Developer")
employee_3 = Employee("Elon Musk", 53, 100000, "CEO")

limbus_company.add_employee(employee_1)
limbus_company.add_employee(employee_2)
limbus_company.add_employee(employee_3)

print(limbus_company)
