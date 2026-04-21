class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def bonus(self):
        self.salary += self.salary * 0.10
        print("New Salary:", self.salary)

e1 = Employee("Ravi", 20000)
e1.bonus()