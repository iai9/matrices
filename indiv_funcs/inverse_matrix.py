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

print(round(sin(101.55273),8))

