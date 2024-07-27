my_dict = int(input("Entre com a quantidade de alunos: "))

notas = {}
soma_notas = 0
for i in range(my_dict):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    
    notas[nome] = nota
    soma_notas += nota
    
    media = soma_notas / my_dict
    print("Notas dos alunos:")
    for nome, nota in notas.items():
        print(f"{nome}: {nota:.2f}")