# programa que lê o nome de uma cidade
# ver se o nome começa com SANTO

cidade = input("Digite o nome de uma cidade: ").strip()
print(cidade.upper().startswith("SANTO"))

# funcionando (antes da correção)

# correção do guanabara

# cid = str(input("Em que cidade você nasceu? ")).strip()
# print(cid.upper() == "SANTO")