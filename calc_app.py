# Creatre the file if it does not exist
# create a name for the calcolator and givre it names 
#if statement to tel it what to do in sertain situations
#calculate input from user 


# create or open a file
file = open('equation.txt', 'w')
#fucntion giving giving num 1 and num 2 instructions if sertain properties aer being used
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def add(num1, num2):
    return num1 + num2

def divide(num1, num2):
    try:
        result = num1 / num2
        #error handelir for devideing with zero
    except ZeroDivisionError:
        #printing error
        print("Error : You can't devide by zero.")
        return None
    else:
        return result
    
try:
    #giving a input fucntion desided on using floaters becaus less margen for errors
    num1 = float(input("Please enter your first number :"))
    operator = input("Please enter one of the following (+, -, *, /): ")
    num2 = float(input("Please enter your second number :"))
except ValueError:
    #error hndelir if the wrong tipe of valuse are entert
    print("Invalid input> please enter a valid number or value")

#telling opperator what to do if plus mines multyply or devide are being used
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    #error handeling for not using the corect symbols
    print("Invalid operator. Please pick one of (+, -, *, /)")
    result = None
    #if everyting is entert correctly the ent result would be pirnted ind the equation.txt file
if result is not None:
    equation = f"{num1} {operator} {num2} = {result}\n"
    file.write(equation)


file.close
