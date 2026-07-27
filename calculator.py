#python program to create calculator
#3 steps to build calculator
# 1.functions for operations 
# 2.input user
#3.print result
#step1:create function:
#function to add two numbers
def add(num1,num2):
    return num1+num2

#function to substract two numbers
def sub(num1,num2):
    return num1-num2
#function to multiply two numbers
def multiply(num1,num2):
    return num1*num2
#function to divide two numbers
def divide (num1,num2):
    return num1/num2
#step2:user input
print("please select an operation:\n" \
      "1.Addition\n " \
      "2.Subtraction\n"\
      "3.multiplication\n"\
      "4.divide\n")
select=int(input("select an operation from 1 to 4:"))
number1=int(input ("select the first number:"))
number2=int(input("select the second number:"))
#step3:print the result
if select==1:
    print("Addition of two numbers are:" ,\
          add(number1,number2))
elif select==2:
    print("subtraction of two numbers is:" ,\
          sub(number1,number2))
elif select==3:
    print("multiply of two numbers is:",\
          multiply(number1,number2))
elif select==4:
    print("division of two numbers is:",\
          divide(number1,number2))
else:
    print("invalid operation!please select again")