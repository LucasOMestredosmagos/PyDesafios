lista1 = input("Digite os elementos da lista 1 (separados por espaço): ").split()

lista2 = input("Digite os elementos da lista 2(separados por espaço): ").split()

conjunto1 = set(lista1)
conjunto2 = set(lista2)

uniao = conjunto1 | conjunto2

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("União", uniao)