#Shelby Stanly
#CS 135 03
#Professor Puckett
#Exam 2 Question 2 
import math

#Title
print("Monthly Payment Calculator")
print(" ") 
print(" ")

#For the loan count later
loans = 0

Y = True 

while Y == True:
   #Principal amount
   P = float(input("How much is the loan?"))
   
   #(Monthly rate)/100 - Converting it to a decimal
   interest_rate = float(input("What is the annual interest rate (i.e., 6.5)?"))
   r = float((interest_rate/12)/100)
   
   years = float(input("How many years?"))
   n = float(years*12)
   
   payment = float(P*(r*(1+r)**n)/(((1+r)**n)-1))
   y = "{:.2f}".format(payment)
   
   print(f"Your monthly payment is ${y}.")
   print(" ")
   more = input("Any more calculations? (Y/N)")
   if more == "Y" or more == "y":
      print (" ")
      print (" ")
      loans = int(loans + 1)
      continue
   else:
      loans = int(loans + 1)
      print (" ")
      print (" ")
      break
print (f"Loans processed today: {loans}")
print("Have a lovely day!")