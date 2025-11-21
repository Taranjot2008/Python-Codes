import sympy as sp
from sympy import N

#welcome message
print("Welcome to the Scientific Calculator!")

def take_input():
    #taking input
    a = input("Enter first expression or a number(a): ")
    b = input("Enter second expression or a number(b): ")
    return a, b, x


#categorizing different operations of different classes
op_class = input("Select an operation class (Arithmetic, Exponential, Calculus, Trignometric, Hyperbolic): ").lower()

if op_class == 'arithmetic' or op_class == 'a':
    x = sp.symbols('x')
    a, b = take_input()
    #operations dictionary for basic arithmetic operations
    operations_dict = {
        '+': sp.Add(a, b),
        '-': sp.Add(a, (-b)),
        '*': sp.Mul(a, b),
        '/': sp.Mul(a, (1/b))
    }

    #operation input
    operation = input("Enter an operation (+, -, *, /): ").lower()

    try:
        #calculating error
        if operation not in operations_dict:
            raise ValueError("Invalid operation")
        #calculating result
        result = operations_dict[operation]
        #printing the result
        print(f"The result is: {result}")       

    except ValueError as ve:
        print(ve)


elif op_class == 'exponential' or op_class == 'e':

    a, b = take_input()

    #operations dictionary for exponential operations
    operations_dict = {
        'sqrt': sp.sqrt(a),
        'pow': sp.Pow(a, b),
        'log': round(N(sp.log(a, b)), 4)
    }

    #operation input
    operation = input("Enter an operation (sqrt(a), pow(a^b), log_b(a)): ").lower()

    try:
        #calculating error
        if operation not in operations_dict:
            raise ValueError("Invalid operation")
        #calculating result
        result = operations_dict[operation]
        #printing the result
        print(f"The result is: {result}")

    except ValueError as ve:
        print(ve)

elif op_class == 'calculus' or op_class == 'c':

    func_input = input("Enter a function in terms of x (e.g., x**2 + 3*x + 2): ")
    x = sp.symbols('x')

    #integration operation
    def integration(func):
        return sp.integrate(func, x)
    
    #differentiation operation
    def differentiation(func):
        return sp.diff(func, x)
    
    #limits operation
    def limits(func, point):
        return sp.simplify(sp.limit(func, x, point))
    
    #operation input
    operation = input("Enter an operation (integrate, differentiate, limit): ").lower()

    if operation == 'integrate' or operation == 'int':
        calc_integral = integration(func_input)
        print(f"The integral of the function is: {calc_integral} + C")
    
    elif operation == 'differentiate' or operation == 'diff':
        calc_derivative = differentiation(func_input)
        print(f"The derivative of the function is: {calc_derivative}")
    
    else:
        point = int(input("Enter the point to evaluate the limit: "))
        calc_limit = limits(func_input, point)
        print(f"The limit of the function as x approaches {point} is: {calc_limit}")

elif op_class == 'hyperbolic' or op_class == 'h':

    #take inout in radians
    a = input("Enter the input: ")

    #operations dictionary for exponential operations
    operations_dict = {
        'sinh': round(sp.sinh(a), 4),
        'cosh': round(sp.cosh(a), 4),
        'tanh': round(sp.tanh(a), 4),
        'sech': round(sp.sech(a), 4),
        'cosech': round(sp.csch(a), 4),
        'coth': round(sp.coth(a), 4),
        'asinh': round(sp.asinh(a), 4),
        'acosh': round(sp.acosh(a), 4),
        'atanh': round(sp.atanh(a), 4),
        'asech': round(sp.asech(a), 4),
        'acosech': round(sp.acsch(a), 4),
        'acoth': round(sp.acoth(a), 4)
    }

    #operation input
    operation = input(f"Enter an operation {list(operations_dict.keys())}: ").lower()

    try:
        #calculating error
        if operation not in operations_dict:
            raise ValueError("Invalid operation")
        #calculating result
        result = operations_dict[operation]
        #printing the result
        print(f"The result is: {result}")

    except ValueError as ve:
        print(ve)

elif op_class == 'trignometric' or op_class == 't':

    #take inout in radians
    a = input("Enter the degree (in rad) or value if inverse trig functions: ")

    #operations dictionary for exponential operations
    operations_dict = {
        'sin': round(sp.sin(a), 4),
        'cos': round(sp.cos(a), 4),
        'tan': round(sp.tan(a), 4),
        'sec': round(sp.sec(a), 4),
        'cosec': round(sp.csc(a), 4),
        'cot': round(sp.cot(a), 4),
        'asin': round(sp.asin(a), 4),
        'acos': round(sp.acos(a), 4),
        'atan': round(sp.atan(a), 4),
        'asec': round(sp.asec(a), 4),
        'acosec': round(sp.acsc(a), 4),
        'acot': round(sp.acot(a), 4)
    }

    #operation input
    operation = input(f"Enter an operation {list(operations_dict.keys())}: ").lower()

    try:
        #calculating error
        if operation not in operations_dict:
            raise ValueError("Invalid operation")
        #calculating result
        result = operations_dict[operation]
        #printing the result
        print(f"The result is: {result}")

    except ValueError as ve:
        print(ve)

'''#running infinite loop
while True:
    #asking if user wants to run calculation again
    repeat = input("Do you want to perform another operation? (y/n): ")

    #running calculation again
    def run_again():
            
        operation = input("Enter an operation (+, -, *, /, sqrt(a), pow(a^b), log_b(a)): ")
        result = operations_dict[operation]
        
        #error
        if operation not in operations_dict:
            print("Invalid operation")
            exit()

        print(f"The result is: {result}")

        return operation

    if repeat.lower() == 'y':
        run_again()
                
    else: '''

print("Exiting the calculator. Goodbye!")
exit()


