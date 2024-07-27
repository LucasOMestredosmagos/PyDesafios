def verificar_chaves(dicionario, chaves):
    return all(chave in dicionario for chave in chaves)

dicionario = {"nome": "Julio", "idade": 15, "cidade": "Rio De janeiro"}
chaves = ["nome", "idade", "cidade"]
print(verificar_chaves(dicionario, chaves))

chaves = ["nome", "idade", "pais"]
print(verificar_chaves(dicionario, chaves))