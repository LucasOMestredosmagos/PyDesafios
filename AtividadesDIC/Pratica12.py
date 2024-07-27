votos = {}

def iniciar_votacao():
    global votos
    votos = {}
    num_opcoes = int(input("Digite o número de opções: "))
    for i in range(num_opcoes):
        opcao = input(f"Digite a opção {i+1}: ")
        votos[opcao] = 0
        
def votar():
    global votos
    opcao = input("\033[36mDigite a opção que você deseja votar: \033[0m")
    if opcao in votos:
        votos[opcao] += 1
        print("\033[32mVoto registrado com sucesso!\033[0m")
    else:
        print("\033[31mOpção Inválida. Tente Novamente.\033[0m")
        
def exibir_resultados():
    global votos
    print("\033[33mResultados finais:\033[0m")
    for opcao, voto in votos.items():
        print(f"{opcao}: {voto} votos")
                
while True:
    print("Sistema de Votação")
    print("1, Iniciar votação")
    print("2, Votar")
    print("3, Exibir resultados")
    print("0, Encerrar votação e exibir resultados finais")
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        iniciar_votacao()
    elif opcao == 2:
        votar()
    elif opcao == 3:
        exibir_resultados()
    elif opcao == 0:
        exibir_resultados()
        break
    else:
        print("\033[31mOpção Inválida. Tente Novamente.\033[0m")
            
                    