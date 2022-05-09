print("Ця гра на виживання. Вам потрібно прожити за студента 365 днів. Так щоб в вас були гроші (мінімум 100) і щоб вас не вигнали!!!")
class Student:
    print("Abobus")
    a = 0
    b = 0
    def __init__(self):
        self.money = 100
        self.study = 100
    #a = int(input("Скільки днів працювати студенту:"))
    def work(self):
        for a in range(int(input())):
            Sania.money = Sania.money + 1
            Sania.money = Sania.study - 1
        print(Sania.money,Sania.study)
    #b = int(input("Скільки днів Вчитися студенту:"))
    def study(self):
        for b in range(int(input())):
            Sania.money = Sania.money - 1
            Sania.money = Sania.study + 1
        print(Sania.money, Sania.study)
        if Sania.study < 1:
            print("ти програв")
        if Sania.money < 1:
            print("ти програв")
Sania = Student()
Sania.work()
Sania.study()
print(Sania.money, Sania.study)
