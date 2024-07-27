def adicionar_ao_dicionario(dicionario, chave, valor):
    dicionario[chave] = valor
    return dicionario

dicionario = {'nome': 'Julio', "idade": 30}
print("Dicionário original:", dicionario)

chave = "idade"
valor = 31
dicionario_atualizado = adicionar_ao_dicionario(dicionario, chave, valor)
print("Dicionário atualizado:", dicionario_atualizado)

chave = "cidade"
valor = "São Paulo"
dicionario_atualizado = adicionar_ao_dicionario(dicionario, chave, valor)
print("Dicionário atualizado:", dicionario_atualizado)
    