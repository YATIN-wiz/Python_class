class Car:
    def __init__(self, brand,model,year):
        self.brand = brand
        self.model = model
        self.year = int(year)

    def display(self):
        print("Car brand:", self.brand)
        print("Model:", self.model)
        print("Year it was made:", self.year)

    def age(self):
        age = (2024 - self.year)
        print("Age:", age)


car = Car(input("Enter car brand"), input("Enter model"), input("Enter year"))

car.display()
car.age()
