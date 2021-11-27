#--- ORGANIZANDO CONJUNTOS E SUBCONJUNTOS DE ELEMENTOS EM PYTHON ---
conjunto = {1, 2, 3, 4, 4, 2}
conjunto.add(6)
conjunto.discard(2)
print(conjunto)


# --- UNIÃO DE CONJUNTOS ---
conjunto = {1, 3, 5, 8}
conjunto2 = {2, 4, 6, 10}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))


#--- IDENTIFICANDO UMA INTERSEÇÃO DE CONJUNTOS ---
conjunto = {1, 3, 5, 8}
conjunto2 = {2, 4, 6, 8, 5, 10}
conjunto_uniao = conjunto.intersection(conjunto2)
print('Interseção: {}'. format(conjunto_uniao))


# --- IDENTIFICANDO UMA DIFERENÇA DE CONJUNTOS ---
conjunto = {1, 3, 5, 8}
conjunto2 = {2, 4, 6, 10}
conjunto_diferença1 = conjunto.difference(conjunto2)
print('Diferença: {}'. format(conjunto_diferença1))


# --- IDENTIFICANDO UMA DIFERENÇA SIMÉTRICA (TUDO QUE NÃO TEM NOS DOIS CONJUNTOS) ---
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {}'.format(conjunto_diff_simetrica))


# --- INDENTIFICANDO SE É UM SUBCONJUNTO OU NÃO ---
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B: {}'. format(conjunto_subset))


# --- IDENTIFICANDO UM SUPERCONJUNTO (B é um superconjunto sobre A porque consegue atender todos os elementos que tem em A ---
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset))


# --- CONVERTENDO UMA LISTA PARA CONJUNTO ---
lista = ['dog', 'dog', 'cat', 'giraffe', 'duck', 'cat']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)