import math


# z''' + b*z'' + c*z' + d*z = F(x)

# Consideraremos a Z''' multiplicada por 1
# z,y,w valores iniciales
# z'   = y
# z''  = y'  = w
# z''' = y'' = w'

def function(t, w, y, z):
    return math.exp(t) - 2 * w + y + z


def k_calculator(t, z, y, w):
    return [y, w, function(t, w, y, z)]


def rk4(z, t, y, w, h):
    k1 = k_calculator(t, z, y, w)
    k2 = k_calculator(t + h / 2, z + (h / 2) * k1[0], y + (h / 2) * k1[1], w + (h / 2) * k1[2])
    k3 = k_calculator(t + h / 2, z + (h / 2) * k2[0], y + (h / 2) * k2[1], w + (h / 2) * k2[2])
    k4 = k_calculator(t + h / 2, z + (h / 2) * k3[0], y + (h / 2) * k3[1], w + (h / 2) * k3[2])
    z1 = [z + (1 / 6) * h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]),
          y + (1 / 6) * h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]),
          w + (1 / 6) * h * (k1[2] + 2 * k2[2] + 2 * k3[2] + k4[2])]
    return z1


def n_rk4(z, t, y, w, h, n):
    z1 = [z, y, w]
    tArray = []
    zArray = []
    for i in range(n):
        zArray.append(z1)
        z1 = rk4(z1[0], t, z1[1], z1[2], h)
        tArray.append(t)
#       print(z1)
        t = t + h

    f0 = function(tArray[0],zArray[0][2],zArray[0][1],zArray[0][0])
    f1 = function(tArray[1],zArray[1][2],zArray[1][1],zArray[1][0])
    f2 = function(tArray[2],zArray[2][2],zArray[2][1],zArray[2][0])
    f3 = function(tArray[3],zArray[3][2],zArray[3][1],zArray[3][0])
    f4 = function(tArray[4],zArray[4][2],zArray[4][1],zArray[4][0])

    y5prime = tArray[4] + h/720 * (1901*f4 - 2774*f3 + 2616*f2 - 1274*f1 +251*f0)

    #Devuelvo y5Prime porque no hay ejemplos de ecuacuiones diferenciales de 3orden y para nuestra solucion necesitamos una matriz, cosa que
    # no se esta devolviendo una en los f de 0 a 4.

    #f5prime = function(t,y5prime)
    #y5 = tArray[4] + h/720 *(251*f5prime + 646*f4 - 264*f3 + 106 * f2 - 19 * f1)

    print(y5prime)




n_rk4(1, 0, -1, 0, 0.1, 5)
