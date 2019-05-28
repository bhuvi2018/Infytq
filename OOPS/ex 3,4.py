class Employee:
    def __init__(self):
        self.name = name
        self.age = age
        self.salary=sal
        

Jack=Employee("Jack",24,30000)
Jill=Employee("Jill",27,40000)


#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self._name=name
        self._gender=gender

    def running(self):
        if(self._gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")

Maria=Athlete("Maria","girl")
Maria.running()
