# Sétimo Exercício: Top 3 mais frequentes

# Dada uma lista de números, crie uma função que retorne os três números mais frequentes
# em ordem decrescente de frequência. Se houver empates, ordene pelo valor numérico.

# Exemplo: [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]

# Saída: [2, 1, 4]

from collections import Counter

def top_3_mais_frequentes(numeros):
    contagem = Counter(numeros)
    return [num for num, _ in contagem.most_common(3)]


lista = [1, 3, 3, 2, 1, 1, 4, 4, 4, 2, 2, 2, 5, 5]
print(top_3_mais_frequentes(lista))
