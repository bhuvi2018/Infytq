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
    def __init__(self):
        self.__name=""
        self.__gender=""
    
    def set_name(self,name):
        self.__name=name
    
    def get_name(self):
        return self.__name
        
    def set_gender(self,gender):
        self.__gender=gender
    
    def get_gender(self):
        return self.__gender
        
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
k=Athlete()
k.set_gender("girl")
k.set_name("Maria")
k.running()
   
    #OR
    
#OOPR-Exer-4
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender

    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
k=Athlete("Maria","girl")
k.running()


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

#ASS 5
class Vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_cost=None
        self.__vehicle_type= None
        self.__premium_amount=None
        
    def set_vehicle_id(self, vehicle_id):
            self.__vehicle_id = vehicle_id

    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def set_vehicle_cost(self, vehicle_cost):
            self.__vehicle_cost = vehicle_cost

    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def set_vehicle_type(self, vehicle_type):
            self.__vehicle_type = vehicle_type
            
    def get_premium_amount(self):
        return self.__premium_amount
            
    def set_premium_amount(self,premium_amount):
            self.__premium_amount = premium_amount

    def get_vehicle_type(self):
        return self.__vehicle_type
    
    def calculate_premium(self):
        if(self.__vehicle_type=="TwoWheeler"):
            self.__premium_amount=self.__vehicle_cost*2/100
            print(self.__premium_amount)
        elif(self.__vehicle_type=="FourWheeler"):
            self.__premium_amount=self.__vehicle_cost*6/100
            print(self.__premium_amount)
        else:
            print("vehicle type is invalid")
    
    def display_vehicle_details(self):
        print("Vehicle ID:",self.__vehicle_id)
        print("Vehicle Cost:",self.__vehicle_cost)
        print("Vehicle Type:",self.__vehicle_type)
        print("Premium Amount:",self.__premium_amount)
    

Car=Vehicle()
Car.set_vehicle_type("TwoWheeler")
Car.set_premium_amount(1000)
Car.set_vehicle_cost(100000)
Car.calculate_premium()
Car.set_vehicle_id(111)
Car.display_vehicle_details()


#ASS_7
class Instructor:
    def __init__(self):
        self.__instructor_name= "Krish"
        self.__experience=2
        self.__avg_feedback=4.6
        self.__technology_skill="Java"
            
    def set_technology_skill(self, technology_skill):
            self.__technology_skill= technology_skill

    def get_technology_skill(self):
        return self.__technology_skill
        
    def set_avg_feedback(self, avg_feedback):
            self.__avg_feedback= avg_feedback

    def get_avg_feedback(self):
        return self._avg_feedback
        
    def set_experience(self, experience):
            self.__experience = experience

    def get_experience(self):
        return self._experience
        
    def set_instructor_name(self, instructor_name):
            self.__instructor_name = instructor_name

    def get_instructor_name(self):
        return self.__instructor_name  
        
    def allocate_course(self,technology):
        if((technology==self.__technology_skill) or (technology=="C++")):
            return True
        else:
            return False
    
    def check_eligibility(self):
        if(self.__experience>3 and self.__avg_feedback>=4.5):
            return True
        elif(self.__experience<=3 and self.__avg_feedback>=4):
            return True
        else:
            return False

Krish=Instructor()
print(Krish.allocate_course("Java"))
print(Krish.check_eligibility())


#OOPR-Assgn-8
#Start writing your code here
class Student:
    def __init__ (self):
            self._student_id=None
            self._age=None
            self._marks=None
            
    def set_student_id(self, student_id):
            self._student_id = student_id

    def get_student_id(self):
        return self._student_id
    
    def set_age(self, age):
            self._age = age

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
    
s1=Student()
s1.set_marks(90)
s1.set_age(21)
s1.set_student_id("BB")
s1.validate_marks()
s1.validate_age()
s1.check_qualification()


#ASS 9
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
