class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    def display(self):
        print(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, empid, salary):
        super().__init__(name,age)
        self.empid = empid
        self.salary = int(salary)

    def display(self):
        print(self.name, self.age, self.empid, self.salary)

    def salary_incrementation(self):
        inc = int(input("Enter the amount to be incrementated:"))
        self.salary += inc


if __name__ == "__main__":
    p1 = Person("P1",20)
    p2 = Employee("P2", 35, "id345", 100000)
    p1.display()
    p2.display()
    p2.salary_incrementation()
    p2.display()

    
