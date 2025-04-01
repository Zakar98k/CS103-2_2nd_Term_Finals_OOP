class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary


class Company:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
