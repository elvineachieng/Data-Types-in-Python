#Enter calculation:5*6
#5 * 6 = 30
num1, num2, operator =input("Enter calculation").split()
#store the user input of 2 numbers and the operator
#convert the strings into integers
num1 = int(num1)
num2 = int(num2)
#if + then we need to provide output based on addition
if operator =="+":
    print("{} + {} = {}".format(num1, num2, num1 + num2))
elif operator =="-": 
    print("{} - {} = {}".format(num1, num2, num1 - num2)) 
elif operator =="*":
    print("{} * {} = {}".format(num1, num2, num1 * num2))
elif operator =="/":
    print("{} / {} = {}".format(num1, num2, num1 / num2))
else:
    print("use either + - * or / next time")    
#print the resul
age=eval(input("Enter age:"))
#and : if both are true it returns true
#or : if either conditions is true then true
#not : Convert a true conditions into  a false
#if age is both greater than or eqaul to 1 and less than or equal to 18 important
if (age>=1) and (age<= 18):
    print("Imprtant Birthday")
#we'll provide different outputs based on age
#1 - 18 -> importatnt
#if age is either 21 or 50 important
elif(age == 21) or (age == 50):
  print("Imprtant Birthday")
elif not(age < 65):
    print("Important Birthday")
esle:print("Sorry Not Important Birthday")
#we check if age is less than 65 and then convert true to false and vice versa
#else not important
#21, 50, >65 -> important 
#All others -> nt important
#Receive age and store in age 