# Función que genera la secuencia de Fibonacci con un parámetro que solicita la posición y devuelve el valor de la posición seleccionada
# La primera posición es el 0, la segunda posición es el 1, la tercera es el 2, etc...
def fibonacci(n):

    a = 0
    b = 1
    
    if n < 0:
        print("Incorrecto")

    # Si el valor es 0 devuelve 0
    elif n == 0:
        return 0

    # Si el valor es 1 devuelve 1
    elif n == 1:    
        return b
    else:
        # Sino generamos una secuencia Fibonacci hasta el valor dado
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        # Devuelve el valor de la posición dada
        return b

if __name__ == '__main__' : main()