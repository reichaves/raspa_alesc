# coding: UTF-8

# exemplo de while

nomes_while = ["Altair", "José", "Maria"]
contador = 0
candidatos_while = {"Nome": []}

while contador < 3:
	candidatos_while['Nome'].append(nomes_while[contador])
	contador = contador + 1

# exemplo de for

nomes_for = ["Altair", "José", "Maria"]
candidatos_for = {'Nome':[]}

for item in nomes_for:
	candidatos_for['Nome'].append(item)