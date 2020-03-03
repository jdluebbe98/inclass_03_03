'''
Created on Mar 3, 2020
Definitions for class:
Class: Objects in real life
Encapsulation: eh, Python kind of does this
Inheritance:
Polymorphism:
Data Hiding: ugh, again Python kind of does this. Data can be seen outside of the class.
@author: luebbejo
'''
class Vehicle:     
    def __new__(cls):
        if cls is Vehicle:
            raise TypeError("Can't instantiate a Vehicle object")
        
    def __init__(self, type):
        self.type = type
    
    def printType(self):
        print("Type = " + self.type)

#Hmm, what if I don't want to be able to instantiate Vehicle objects in Python?
#Wwhat is the keyword for a non-instantiable class in c#? Static

#v = Vehicle() #This now has one argument, self, even though you don't see it