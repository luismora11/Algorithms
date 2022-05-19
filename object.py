#This is a demonstration of a Class and an object in Python
from tkinter import N


class Person:
    
    def __init__(self, name, weight, age):
        self.n = name
        self.w = weight
        self.a = age

    def sayHi(self):
            print("My name is " + self.n)

p1 = Person("Luis", 149, 29)
p1.sayHi() 
        