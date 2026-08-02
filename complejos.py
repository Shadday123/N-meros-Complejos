import math

def suma(c1, c2):
    real = c1[0] + c2[0]
    img = c1[1] + c2[1]
    return (real, img)

def resta(c1, c2):
    real = c1[0] - c2[0]
    img = c1[1] - c2[1]
    return (real, img)

def multiplicacion(c1, c2):
    real = c1[0] * c2[0] - c1[1] * c2[1]
    img = c1[0] * c2[1] + c2[0] * c1[1]
    return (real, img)

def conjugado(c1):
    return (c1[0], -c1[1])

def modulo(c1):
    return math.sqrt(c1[0]**2 + c1[1]**2)

def fase(c1):
    return math.atan2(c1[1], c1[0])

def division(c1, c2):
    if c2 == (0, 0):
        raise ZeroDivisionError("No se puede dividir entre el número complejo 0.")

    conj = conjugado(c2)

    numerador = multiplicacion(c1, conj)
    divisor = multiplicacion(c2, conj)

    real = numerador[0] / divisor[0]
    img = numerador[1] / divisor[0]

    return (real, img)

def cartesiano_a_polar(c1):
    magnitud = modulo(c1)
    angulo = fase(c1)
    return (magnitud, angulo)

def polar_a_cartesiano(r, theta):
    real = r * math.cos(theta)
    img = r * math.sin(theta)
    return (real, img)

def main():
    c1 = (0, 3)
    c2 = (-1, -1)
    

main()
