'''

no. decided not to do


'''

pi = 3.1415926535

def deg_to_pi_rad(deg):
    return deg/180

def pi_rad_to_deg(pirad):
    return 180*pirad

def simplest_pi_rad(pirad):
    return pirad%2

def simplest_deg(deg):
    return deg%360

def factorial(number):

    if isinstance(number, int) and number > 1:
        initial_product = 1
        for i in range(1, number+1):
            initial_product = initial_product*i
        
        return initial_product
    else:
        raise ValueError("Number cannot be factorial-ed")

def sin(x):

    if x >= 2:
        x = x%2

    x = x*pi

    h = x

    for i in range(3, 102, 2):

        if i%4 == 1:

            h = h + ((x**i)/factorial(i))

        else:

            h = h - ((x**i)/factorial(i))

    return h

def cos(x):
    h = 1/2 - x # cos(x) = sin(90-x) = sin(pi/2 radians - x)
    return sin(h)

def tan(x):
    return sin(x)/cos(x)

def csc(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return cos(x)/sin(x)


print(round(sin(1/6),8))
print(round(cos(1/6),8))
print(round(tan(1/6),8))
