class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee(20000)
e.set_salary(-5000)   # invalid, ignore
print(e.get_salary()) # 20000