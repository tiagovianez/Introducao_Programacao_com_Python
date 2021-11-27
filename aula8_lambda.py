#--- FAZENDO UM FOR EM UMA LISTA | FUNÇÃO ANÔNIMA | len(x): INFORMA A QUANTIDADE DE LETRAS
#PS.: Não há necessidade de criar um outro método
contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['gato', 'cachorro', 'girafa', 'lobo', 'raposa']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
multiplicacao = lambda a, b: a * b
divisao = lambda a, b: a / b

print(soma(80, 100))
print(subtracao(100, 20))
print(multiplicacao(5, 5))
print(divisao(60, 10))


# --- CRIANDO UMA CALCULADORA | DICIONÁRIO ---
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

print(type(calculadora))
print('Soma: {}'.format(soma(70, 100)))
print('Subtracao: {}'.format(subtracao(1000, 400)))
print('Multiplicacao: {}'.format(multiplicacao(5, 5)))
print('Divisao: {}'.format(divisao(5, 5)))