'''
Created on Mar 3, 2020

@author: luebbejo
'''

class Employee:
#    pass
#    def __init__(self, last_name):
#        self.last_name = last_name #Be sure to differentiate. One is at the Object scope, and the other is in the Method scope
        
    def __init__(self, last_name, first_name): #'self' is the current object 
        self.last_name = last_name
        self.first_name = first_name
'''
woz = Employee() #This invokes the default constructor for the Employee class
woz.last_name = "Wozniak"   #Adds a field to the object

jobs = Employee()
jobs.lastName = "Jobs" #Yikes, wrong way. This creates two different field names for semantically the same thing

print(woz.last_name)
print(jobs.lastName)
print(woz.__dict__) #This prints the dictionary associated with this object in Name/Value pairs since it's a dictionary 
'''
        
woz = Employee("Wozniak", "Steve") #Invokes the explicit constructor for Employee
jobs = Employee("Jobs", "Steve")
print(woz.last_name)
print(jobs.last_name)
print(woz.__dict__)


timCook = Employee("Cook", "Tim") #Uses the constructor with three arguments 