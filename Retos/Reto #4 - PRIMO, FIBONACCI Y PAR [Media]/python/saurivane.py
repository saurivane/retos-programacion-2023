"""/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
"""


def par(num):
    if num % 2 != 0:
        return "y es impar"
    else:
        return "y es par"


def primo(num):
    if num < 2:
        return " no es primo, "
    i = 1
    for i in range(2, i):
        if num % i == 0:
            return " no es primo, "
    return " es primo, "


def fibonacci(num):
    resultado = "no es fibonacci "
    numero_a = 0
    numero_b = 1
    while ((numero_a < num) | (numero_b < num)):
        siguiente = numero_a + numero_b
        numero_a = numero_b
        numero_b = siguiente
        resultado = "es fibonacci " if ((num == numero_a) | (num == numero_b)) else "no es fibonacci "
    return resultado


num = int(input("Introduce número:"))

print(f"El numero " + str(num) + primo(num) + fibonacci(num) + par(num))
