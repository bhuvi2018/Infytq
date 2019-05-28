#EX_3
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


#ASS_3
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


#ASS_5
class Vehicle:
    def __init__(self,vehicle_id, vehicle_cost,vehicle_type):
        self._vehicle_id = vehicle_id
        self._vehicle_cost=vehicle_cost
        self._vehicle_type= vehicle_type
        
    def set_vehicle_id(self, vehicle_id):
            self._vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self._vehicle_id
        
    def set_vehicle_cost(self, vehicle_cost):
            self._vehicle_cost = vehicle_cost

    def get_vehicle_cost(self):
        return self._vehicle_cost
        
    def set_vehicle_type(self, vehicle_type):
            self._vehicle_type = vehicle_type

    def get_vehicle_type(self):
        return self._vehicle_type
    
    def calculate_premium(self):
        if(self._vehicle_type=="TwoWheeler"):
            self._premium_amount=self._vehicle_cost*2/100
        elif(self._vehicle_type=="FourWheeler"):
            self._premium_amount=self._vehicle_cost*6/100
        else:
            print("vehicle type is invalid")
    
    def display_vehicle_details(self):
        print("Vehicle ID:",self._vehicle_id)
        print("Vehicle Cost:",self._vehicle_cost)
        print("Vehicle Type:",self._vehicle_type)
        print("Premium Amount:",self._premium_amount)
    

Car=Vehicle("BM2009",450000,"FouWheeler")
Car.set_vehicle_type("FourWheeler")
Car.calculate_premium()
Car.display_vehicle_details()
