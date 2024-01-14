name = input ("What is yur name ")
print("Hello", name)

#Ask the user tp input 2 values and store them in variables num1 and num2
num1, num2=input("Enter 2 numbers: ").split() 
#Convert the strings into regular numbers integer
num1=int(num1)
num2=int(num2)
#Add the values entered and store in sum
sum = num1 + num2
#Subtract values and store in difference
difference = num1 - num2
#Multiply the values and store in product
product= num1 * num2
#Divide the values and store in quotient
quotient = num1 / num2
#Use modulus on the values to find the remainder
remainder = num1 % num2
#Print the results
print("{}+{}={}".format(num1, num2,sum))
print("{}-{}={}".format(num1, num2,difference))
print("{}*{}={}".format(num1, num2,product))
print("{}/{}={}".format(num1, num2,quotient))
print("{}%{}={}".format(num1, num2,remainder))
5*1.60934

#Problem: receive miles and convert to kilometres
km_per_mile = 1.60934
miles = float(input("Enter in miles:"))
#kilometres = miles * 1.60934
kilometers = miles * km_per_mile
print(kilometers)
#Enter miles 5
#5 miles equals 8.04 kilometres

#Ask the user to input miles and ssign it to the miles variable
miles = input("Enter miles")
#convert from string to integer
miles = int(miles)
#perform calculations by multiplying 1.60934 times miles
kilometers = miles * 1.60934
#print results using  format()
print("{}miles equals {}kilometers".format(miles, kilometers))



