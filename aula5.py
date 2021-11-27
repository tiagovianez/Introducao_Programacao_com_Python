# --- ORGANIZANDO DADOS EM UMA LISTA OU TUPLA E REALIZANDO OPERAÇÕES COM OS MESMOS ---
# -- PRIMEIRA LISTA DE INTEIROS ---
lista = [1, 5, 9, 13]
lista_animal = ['cat', 'dog', 'elephant', 'parrot']
print(lista_animal[3])

# -- PERCORRENDO UMA LISTA USANDO O LAÇO DE REPETIÇÃO ---
lista = [1, 5, 9, 13]
lista_animal = ['cat', 'dog', 'elephant', 'parrot']

for x in lista_animal:
    print(x)

# -- USANDO UMA SOMA DENTRO DE UMA LISTA ---
lista = [1, 5, 9, 13]
lista_animal = ['cat', 'dog', 'elephant', 'parrot']

print(sum(lista))

# -- BUSCANDO O VALOR MÁXIMO DESSA LISTA ---
lista = [13, 7, 205, 107]
lista_animal = ['cat', 'dog', 'elephant', 'parrot']

# --- MULTIPLICANDO OS CARACTERES DE UMA LISTA ---
nova_lista = lista * 3
print(nova_lista)

if 'wolf' in lista_animal:
    print('Existe um wolf na lista')
else:
    print('Não existe um wolf na lista')

# --- INCLUINDO NOVOS REGISTROS A LISTA (APPEND)---
lista_animal = ['cat', 'dog', 'parrot', 'elephant']
if 'butterfly' in lista_animal:
    print('Há uma borboleta na lista')
else:
    print('Não há uma borboleta na lista. Será incluida')
    lista_animal.append('butterfly')
    print(lista_animal)

# --- REMOVENDO CARACTERES DE UMA LISTA ---
lista_animal.pop(0)
print(lista_animal)

# --- REMOVENDO CARACTERES DE UMA LISTA ATRAVÉS DO NOME ---
lista_animal.remove('parrot')
print(lista_animal)

# --- ORDENANDO UMA LISTA POR ORDEM NUMERICA E ALFABETICA---
lista = [8, 75, 2, 94]
lista_animal = ['cat', 'dog', 'parrot', 'elephant', 'arara']
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

# --- REVERTENDO A LISTA ---
lista_animal.reverse()
print(lista_animal)


# --- TUPLAS ---
# NÃO É POSSÍVEL ALTERAR UM OBJETO DA TUPLA
lista_animal = ['cat', 'dog', 'parrot', 'elephant', 'arara']
lista_animal [0] = 'monkey'
print(lista_animal)

# --- CONTANDO QUANTOS ELEMENTOS ESTÃO EM UM TUPLA ---
tupla = (4, 15, 18, 65, 78, 744)
print(len(tupla))

# --- CONVERTENDO UMA LISTA EM UMA TUPLA ---
tupla_animal = tuple(lista_animal)
print(tupla_animal)
print(type(tupla_animal))