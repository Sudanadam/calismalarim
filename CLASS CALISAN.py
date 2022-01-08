from datetime import date

class Company:
    RaiseRate = 1.1
    NumberOfEmployees = 0
    def __init__(self, name, surname="No Entry", age=0):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = name + surname + "@hotmail.com"
        Company.NumberOfEmployees += 1

    def showInfo(self):
        print(f"Name:{self.name}  Surname: {self.surname}   Age:{self.age} Mail:{self.email} Raise Rate:{Company.RaiseRate}")

    @classmethod
    def shownumberofemployees(cls):
        print(cls.NumberOfEmployees)

    @classmethod
    def CreatwithString(cls, str_):
        name, surname, age = str_.split("-")
        return cls(name, surname, age)

    @classmethod
    def Creatwithbirthyear(cls, name, surname, birthyear):
        return cls(name, surname, date.today().year - birthyear)

    @staticmethod
    def FindBirthYear(Company):
        return date.today().year - Company.age

class Managers(Company):
    NumberOfManagers = 0
    RaiseRate = 3
    def __init__(self, name, surname, age, managerrank, Employees=None):
        super().__init__(name, surname, age)
        #self.name = name
        #self.surname = surname
        #self.age = age
        #self.email = name + surname + "@hotmail.com"
        self.managerrank = managerrank
        if Employees == None:
            self.Employees = []
        else:
            self.Employees = Employees

        Managers.NumberOfManagers += 1

    def addworkers(self, Employe):
        if Employe not in self.Employees:
            self.Employees.append(Employe)

    def deleteworkers(self, Employe):
        if Employe in self.Employees:
            self.Employees.remove(Employe)

    def showEmployee(self):
        for Employe in self.Employees:
            print(Employe.showInfo())

    def showInfo(self):
        print(f"Name:{self.name}  Surname: {self.surname}   "
              f"Age:{self.age} Mail:{self.email} Raise Rate:{Company.RaiseRate} "
              f"Rank:{self.managerrank}")

    def showrank(self):
        print(f"{self.name} 's Rank is {self.managerrank}")

Manager1 = Managers("HamiCan", "Kızılkan", 31, "Ceo")
Manager2 = Managers("AyseSinem", "Kızılkan", 30, "Feo")

Employee1 = Company("Beste", "Kızılkan", 23)
Employee2 = Company("Alper", "Demiralp", 18)
Employee3 = Company("Elif", "Demiralp", 26)
Employee4 = Company("Yıldız", "Sefer")
Employee5 = Company("Kader", age=50)

Employee6 = Company.CreatwithString("İbo-Kızılkan-50")
Employee7 = Company.Creatwithbirthyear("Orhan", "Demiralp", 1970)

print(Manager1.name, Manager1.surname, Manager1.age, Manager1.email, Manager1.managerrank)
print(Manager2.name, Manager2.surname, Manager2.age, Manager2.email, Manager2.managerrank)

print(Employee1.name, Employee1.surname, Employee1.age)
print(Employee2.name, Employee2.surname, Employee2.age)
print(Company.NumberOfEmployees)
Employee2.showInfo()
Employee3.showInfo()
print("----")
Company.showInfo(Employee1)
Company.showInfo(Employee2)
Company.showInfo(Employee3)
Company.showInfo(Employee4)
Company.showInfo(Employee5)
Company.showInfo(Employee6)
Company.showInfo(Employee7)
Company.showInfo(Manager1)
Company.showInfo(Manager2)
print("----")

print(Employee1.__dict__)

print("----")

print(Company.RaiseRate)
print(Employee1.RaiseRate)

print("----")
Employee1.RaiseRate = 2
print(Company.RaiseRate)
print(Employee1.RaiseRate)
print(Employee2.RaiseRate)

print("----")
print(Employee1.__dict__)
print(Employee3.__dict__)
print("----")

Company.shownumberofemployees()
print("----")
print(Company.FindBirthYear(Employee1))

print(Employee1.email)

Managers.showInfo(Manager1)
Managers.showInfo(Manager2)
print("-")
print(Managers.NumberOfManagers)
Managers.showrank(Manager1)
print("----")
Manager1.addworkers(Employee1)
Manager1.addworkers(Employee2)
Manager1.addworkers(Employee3)
Manager2.addworkers(Employee4)
Manager2.addworkers(Employee5)
Manager2.addworkers(Employee6)
print("-------")
Manager1.showEmployee()
Manager2.showEmployee()