def remove_duplicatas(lista):
    conjunto = set(lista)
    lista_sem_duplicatas = list(conjunto)
    return lista_sem_duplicatas

def main():
    lista = input("Digite uma lista de números separados por espaço: ")
    lista = [int(x) for x in lista.split()]

    print("Lista original:", lista)
    lista_sem_duplicatas = remove_duplicatas(lista)
    print("Lista sem duplicatas:", lista_sem_duplicatas)

if __name__ == "__main__":
    main()