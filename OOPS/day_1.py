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
#ASS_3
class Employee:
    def __init__(self):
        self.employee_name = None
        self.designation =None

class Customer:
    def __init__(self):
        self.customer_name = None
        self.bill_amount = None

    def purchases(self):
        self.bill_amount=self.bill_amount- self.bill_amount*2/100
        
    def  pays_bill(self,amount):
        print(self.customer_name,"pays bill amount of Rs.",self.bill_amount)
        
class item:
    def __init__(self):
        self.item_id = None
        self.description =None
        self.price_per_unit = None

Ram=Customer()
Ram.purchases()
Ram.pays_bill()


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


#ASS_7
class Instructor:
    def __init__(self,instructor_name,exper,avg_feedback,tech_skill):
        self._instructor_name= instructor_name
        self._exper=exper
        self._avg_feedback= avg_feedback
        self._tech_skill= tech_skill
        
    def set_tech_skill(self, tech_skill):
            self._tech_skill= tech_skill

    def get_tech_skill(self):
        return self._tech_skill
        
    def set_avg_feedback(self, avg_feedback):
            self._avg_feedback= avg_feedback

    def get_avg_feedback(self):
        return self._avg_feedback
        
    def set_exper(self, exper):
            self._exper = exper

    def get_exper(self):
        return self._exper
        
    def set_instructor_name(self, exper):
            self._instructor_name = instructor_name

    def get_instructor_name(self):
        return self._instructor_name   
    
    def check_eligibility(self):
        if(self._exper==3 and self.allocate_course(self._tech_skill)==True and self._avg_feedback>=4.5):
            return True
            
    def allocate_course(self,_tech_skill):
        if(not(_tech_skill==None)):
            return True
        else:
            return False

Krish=Instructor("Krish",3,4.6,"Python")
Krish.allocate_course("Java")
print(Krish.check_eligibility())


#OOPR-Assgn-8
#Start writing your code here
class Student:
    def __init__ (self, student_id,marks,age):
            self._student_id=student_id
            self._age=age
            self._marks=marks
            
    def set_student_id(self, student_id):
            self._student_id = student_id

    def get_student_id(self):
        return self._student_id
    
    def set_age(self, age):
            self.__age = age

    def get_age(self):
        return self._age   
    
    def set_marks(self, marks):
            self._marks =marks

    def get_marks(self):
        return self._marks
        
    def validate_marks(self):
             if(self._marks>=0 and self._marks<=100):
                 print("True")
             else:
                 print("False")
    def validate_age(self):
            if(self._age>20):
                 print("True")
            else:
                 print("False")
    def check_qualification(self):
            if(self._age>20 and self._marks>=65):
                 print("True")
            else:
                 print("False")
    
s1=Student(1,70,21)
s1.validate_marks()
s1.validate_age()
s1.check_qualification()
s2=Student(1,70,19)
s2.validate_marks()
s2.validate_age()
s2.check_qualification()


class Student:
    def __init__ (self, student_id,marks,age):
            self.__student_id=student_id
            self.__age=age
            self.__marks=marks
            self.__course_id=None
            self.__fees=None
            
    def set__student_id(self, student_id):
            self.__student_id = student_id

    def get__student_id(self):
        return self.__student_id
    
    def set__age(self, age):
            self.__age = age

    def get__age(self):
        return self.__age   
    
    def set__marks(self, marks):
            self.__marks =marks

    def get__marks(self):
        return self.__marks
        
    def set__marks(self, course_id):
            self.__course_id =course_id
        
    def get__course_id(self):
        return self.__course_id
        
    def set__fees(self, fees):
        if(course_id==1001):
            self.__fees =25575.0
        else:
            self.__fees =15500.0

    def get__fees(self):
        return self.__fees
        
    def validate_marks(self):
             if(self.__marks>=0 and self.__marks<=100):
                 print("True")
             else:
                 print("False")
    def validate_age(self):
            if(self.__age>20):
                 print("True")
            else:
                 print("False")
    def check_qualification(self):
            if(self.__age>20 and self.__marks>=65):
                 return True
            else:
                 return False
        
    def choose_course(self,course_id):
        if(self.check_qualification()):
            self.course_id=self.get__fees()
            if(self.__marks>80):
                self.__fees=self.__fees-(self.fees*25/100)
                return True
        return False
            
        
    
s1=Student(1,70,21)
s1.set__student_id(1004)
s1.set__age(21)
s1.set__marks(65)
if(s1.check_qualification()):
    print("Student has qualified")
    if(s1.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")
