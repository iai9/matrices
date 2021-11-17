'''

no. decided not to do


'''

pi = 3.1415926535

def factorial(number):

    if isinstance(number, int) and number > 1:
        initial_product = 1
        for i in range(1, number+1):
            initial_product = initial_product*i
        
        return initial_product
    else:
        raise ValueError("Number cannot be factorial-ed")

def to_rad(number): # hard coding, not iterating. idrc that the taylor series is infinite, I'll get close enough
    return number/pi

def rad_simplify(rad):
    pass

def sin(x):
    h =  x - ((x**3)/(factorial(3))) + ((x**5)/(factorial(5))) - ((x**7)/(factorial(7))) + ((x**9)/(factorial(9))) - ((x**11)/(factorial(11)))
    return h

print(sin(50))