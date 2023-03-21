# Máximo común divisor EJ 1
def mcd(numberA, numberB):
    aux = 0
    while numberB != 0:
        aux = numberB
        numberB = numberA % numberB
        numberA = aux
    return numberA

# Mínimo común múltiplo


def mcm(numberA, numberB):
    return (numberA * numberB) / mcd(numberA, numberB)


print("Ingrese dos números")
print("A =")
numberA = int(input())
print("B =")
numberB = int(input())


print(f"El MCD de {numberA} y {numberB} es {int(mcd(numberA,numberB))}")

print(
    f"El mínimo común múltiplo de {numberA} y {numberB} es {int(mcm(numberA,numberB))}")
