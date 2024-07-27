class Conjunto:
    def __init__(self, elementos):
        self.elementos = set(elementos)

    def uniao(self, outro_conjunto):
        return self.elementos.union(outro_conjunto.elementos)

def main():
    qtde_conjuntos = int(input("Entre com a quantidade de conjuntos: "))

    conjuntos = []
    for i in range(qtde_conjuntos):
        elementos = input(f"Digite os elementos do conjunto {i+1} separados por espaço: ")
        conjuntos.append(Conjunto(elementos.split()))

    uniao_resultante = conjuntos[0]
    for conjunto in conjuntos[1:]:
        uniao_resultante = Conjunto(list(uniao_resultante.uniao(conjunto)))

    print("Conjunto resultante:", uniao_resultante.elementos)

if __name__ == "__main__":
    main()