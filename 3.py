class Human:
    def __init__(self, name = "human"):
        self.name = name
class Auto():
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self, human):
        self.passengers.append(human)
    def add_passenger(self, human,a):
        self.passengers.append(human)
    def print_passengers_names(self):
        if self.passengers != []:
            print(f"Names of {self.brand} passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are no passengers in {self.brand}")
nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")
car.add_passenger(nick)
car.add_passenger(kate)
car.print_passengers_names()





















# class Student:
#     studentsCounter = 0
#     def __init__(self,name,progress,db,school = 1):
#         self.name = name
#         self.progress = progress
#         self.dateofBirthday = db
#         self.school = school
#         Student.studentsCounter += 1
#     def __str__(self):
#         return f"№{self.studentsCounter}\nname: {self.name}\nprogress: {self.progress} \ndate of Birthday: {self.dateofBirthday}"
#     def addProgress(self, a):
#         self.progress += a
#         print("Student mark:",self.progress)
#     def method(self):
#         print("method")

# object = Student("object",11, "04.05.2007")
# print(object)
# James = Student("James",8, "02.06.2009")
# Robert = Student("Robert",5, "02.06.2009")
# Robert.addProgress(5)
# Robert.addProgress(-10)

