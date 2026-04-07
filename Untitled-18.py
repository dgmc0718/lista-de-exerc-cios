numero = int(input("Digite um número:"))
if(numero%2 == 0) and (numero > 0):
    print("O número é par positivo")
elif(numero%2 == 0) and (numero < 0):
    print("O número é par negativo")
elif(numero%2 != 0) and (numero >0):
    print("O número é impar positivo")
elif(numero%2 != 0) and (numero <0):
    print("O número é impar negativo")
else:
    print("O número é neutro")