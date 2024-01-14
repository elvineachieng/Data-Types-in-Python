#data_types
#string data type
#literal assignment of values
first = "Elvine"
last = " Achie"

print(type(first))
print(type(first) == str)
print(isinstance(first, str))
#constructor function
# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

#concatenatin
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
#type casting is the process of cinverting value of one data type to another 
decade = str(1980)
print(type(decade))
print(decade)
#Explicit
name = "Elvine"
age = 23
gpa = 8.2
student = True
print(type(name))
print(type(age))
print(type(gpa))
print(type(student))
age = float(age)
print(age)
gpa = int(gpa)
print(gpa)
student = str(student)
print(type(student))
age = bool(age)
print(age)
#Implicit type casting
x = 2
y = 2.0
x = x/y
print(x)



statement = "I like rock music from the " + decade + "s."
print(statement)

#multiple lines
multiline = '''
Hey, how are you?

I was just checking in.   
                        All good?


'''
print(multiline)


#Escaping special characters
sentences = 'I\'m back at work!\tHey!\n\nwhere\'s at\\located?'
print(sentences)
#String Methods
print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("good", "okay"))
print(multiline)
print(len(multiline))
multiline += '                        '
multiline = '        '+ multiline
print(len(multiline))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
#Build a menu
title = "upper".upper()
print(title.center(20, '='))
print("coffee".ljust(16, ".")+"$1".rjust(4))
print("muffin".ljust(16, ".")+"$2".rjust(4))
print("cheesecake".ljust(16, ".")+"$4".rjust(4))

#string index values
print(first[1])
print(first[-1])
print(first[0:])
#some methods returm boolean data
print(first.startswith('E'))
print(first.endswith("A"))

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print( isinstance(myvalue, bool))


#numeric data types
#integers
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
#float type
gpa = 3.28
y = float(1.14)
print(type(gpa))
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)


#Built in function for numbers
print(abs(gpa))
print(round(gpa + -1))
print(round(gpa))
print(round(gpa, 1))


#Cating a string to a number
zipcode = "10001"
zip_value = (int(zipcode))
print(type(zip_value))



