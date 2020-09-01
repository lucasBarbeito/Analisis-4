import math
import decimal

# Ejercicio a
mathPi_A = math.pi
print(mathPi_A)

# Ejercicio b

def gauss_legendre_float(num):
    a = 1
    b = 1/math.sqrt(2)
    t = 1/4
    p = 1

    for i in range(num):
        y = a
        a = (a + b)/2
        b = math.sqrt(b*y)
        t = t - p * (y-a)**2
        p = 2 * p

    return (a + b)**2 / (4*t)

print(gauss_legendre_float(int (input("number of iterations Excersise b:"))))

# Ejercicio c

def gausslegendredecimal():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1
        pi = None
        while 1:
            an = (a + b) / 2
            b = (a * b).sqrt()
            t -= p * (a - an) * (a - an)
            a, p = an, 2*p
            piold = pi
            pi = (a + b) * (a + b) / (4 * t)
            if pi == piold:  # equal within given precision
                break
    return +pi
print(gausslegendredecimal())

# Ejercicio D

def Spigot(n):

    k, a, b, a1, b1 = 2, 4, 1, 12, 4
    while n > 0:
        p, q, k = k * k, 2 * k + 1, k + 1
        a, b, a1, b1 = a1, b1, p * a + q * a1, p * b + q * b1
        d, d1 = a / b, a1 / b1
        while d == d1 and n > 0:
            yield int(d)
            n -= 1
            a, a1 = 10 * (a % b), 10 * (a1 % b1)
            d, d1 = a / b, a1 / b1


print(list(Spigot(int (input("how many numbers of PI do you want?")))))

