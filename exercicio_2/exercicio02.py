# Segundo Exercício: Ordenação de Tuplas

# Dada uma lista de tuplas, onde cada tupla contém o nome de uma pessoa e sua idade,
# escreva uma função que retorne a lista ordenada pela idade de forma crescente.

# Exemplo: (“Samuel”, ‘Karynne”, “Carol”, “Kleber”, “Vinicius”)

# Saída: (“Carol”, “Karynne”, “Kleber”, “Samuel”, “Vinicius”)

# def ordenar_por_idade(pessoas):
    # return sorted(pessoas, key=lambda pessoas: pessoas[1])
#     return [pessoa[0] for pessoa in sorted(pessoas, key=lambda pessoa: pessoa[1])]

# pessoas = [("Samuel", 27), ("Karynne", 23), ("Carol", 29), ("Kleber", 27), ("Vinicius", 25)]
# print(ordenar_por_idade(pessoas))

def ordenar_por_idade(pessoas):
    return [pessoa[0] for pessoa in sorted(pessoas, key=lambda pessoa: pessoa[1])]

nomes = ["Samuel", "Karynne", "Carol", "Kleber", "Vinicius"]
pessoas = []
for nome in nomes:
    idade = int(input(f"Digite a idade de {nome}: "))
    pessoas.append((nome, idade))

print("Nomes ordenados por idade: ", ordenar_por_idade(pessoas))