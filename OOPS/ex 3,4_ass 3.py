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


class Employee:
    def __init__(self, employee_name, designation):
        self.employee_name = employee_name
        self.designation = designation

class Customer:
    def __init__(self, customer_name,bill_amount):
        self.customer_name = customer_name
        self.bill_amount = bill_amount

    def purchases(self):
        self.bill_amount=self.bill_amount- self.bill_amount*2/100
        
    def  pays_bill(self,amount):
        print(self.customer_name,"pays bill amount of Rs.",self.bill_amount)
        
class item:
    def __init__(self, item_id,description,price_per_unit):
        self.item_id = item_id
        self.description =description
        self.price_per_unit = price_per_unit

Ram=Customer("Ram",7000)
Ram.purchases()
Ram.pays_bill(7000)
