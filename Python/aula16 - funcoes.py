def calcula_dobro(numero):
    total = numero * 2
    return total

def calcula_suma_numeros(num1, num2, **numeros):
    import pdb ; pdb.set_trace()
    return sum(numeros.values())

resultado = calcula_dobro(8)
print(resultado)

soma = calcula_suma_numeros(num1=5, num2=10, num3=20, num4=7, num5=90)
print("O resultado da soma e %d" % soma)
