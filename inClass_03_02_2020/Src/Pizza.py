'''
Created on Mar 3, 2020

@author: luebbejo
'''

#This is another example of classes modeled after the Employee Module

#Create a pizza class
#Fields: set with toppings (string), Crust (string)
#Create a constructor that accepts the toppings and crust and assign to fields in the object
#Write a little code to demo the class like we did in Employee

class Pizza:     
    def __init__(self, toppings, crust):
        self.toppings = toppings
        self.crust = crust
    def toString(self): #A Java/C# convention in all classes
        return "Toppings are " + str(self.toppings) + ". Crust is " + self.crust
        
        
Meatlover = Pizza({"Pepperoni, Sausage, & Bacon"}, "Deep Dish")
Plain = Pizza({"Cheese, Extra Cheese"}, "Thin")
print(Meatlover.toppings) #Blatant violation of OOP Data Hiding
print(Plain.crust)
print(Meatlover.__dict__)
print(Meatlover.toString())