
class employee:
    def __init__(self,id,name) :
        self.id = id
        self.name = name
    def printEmployeeInfo(self):
        print(f"ID: {self.id} \nName: {self.name}")


employee1 = employee(1,'Bob')
employee2 = employee(2,'Alice')


employee2.printEmployeeInfo()
employee1.printEmployeeInfo()