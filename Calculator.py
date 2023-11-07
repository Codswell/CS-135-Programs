#Shelby Stanly
#CS 135 03
#Professor Puckett
#Five Function Calculator
import math

def addition(a,b):
   return a+b

def subtraction(a,b):
   return a-b

def multiplication(a,b):
   return a*b

while True:
   operator = input("Enter operation: +,-,*,sin,cos, q to exit.")
   if operator == 'q':
       break
   elif operator == 'sin':
      x = float(input("Enter a number"))
      value = math.sin(x)
      print(f"{operator}({x}) = {value}")
   elif operator == 'cos':
      x = float(input("Enter a number"))
      value = math.cos(x)
      print(f"{operator}({x}) = {value}")
   else:
      x = float(input("Enter the first number"))
      y = float(input("Enter the second number"))
  
   
      if operator == "+":
         value = addition(x,y)
         print(f"{x} {operator} {y} = {value}") 
      elif operator == "-": 
         value = subtraction(x,y)
         print(f"{x} {operator} {y} = {value}")
      elif operator == "*":
         value = multiplication(x,y)
         print(f"{x} {operator} {y} = {value}")
     
      else: 
         print("Please enter a valid operation")