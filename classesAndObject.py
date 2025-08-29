## Classes and Object

class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("i am getting called because u create object")

    def work(myself):
        print("Happy Working as an employee", myself.age)

e1 = Employee("Megha",34)
e2 = Employee("Deepak",30)
print(e1.name)
print(e2.name)
e1.work()
e2.work()