#defining a function
def well_wishes():
 print("hello")
 print("how are you?")
# calling the function
well_wishes()

#activity 2

#defining a function
def weather_condition():
 print("The weather is pleasant in",spring)
 print("The weather is pleasant in",autumn)

spring="spring.It is a season of new beginnings."
autumn="autumn.It is a season of harvest."
# calling the function
weather_condition()

#activity 3

def add(p,q):
 return p+q
def subtract(p,q):
 return p-q 
def multiply(p,q):
 return p*q
def divide(p,q):
    return p/q

print("Please select an operation:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice=input("Enter your choice(1/2/3/4): ")

num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

if choice=="1":
  print(num1,"+",num2,"=",add(num1,num2))
elif choice=="2":
  print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=="3":
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=="4":
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid input")