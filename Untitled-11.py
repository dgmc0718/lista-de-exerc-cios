numero = int(input("Insira um numero"))
if(numero%2 == 0) and (numero > 0):
    print("O número par positivo")
elif(numero%2 == 0) and (numero < 0):
    print("O número é par negativo")
else:
    print("O número é impar")

