#Esse progrma devolve o fatorial de n ("!n")
#Pode ser transformado em uma função para calcular o fatorial 

numero = int(input("Digite o valor de n: ") )

resultado=1
count=1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
