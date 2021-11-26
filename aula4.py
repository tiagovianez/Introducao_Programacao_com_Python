# --- IMPRIMINDO NO TERMINAL UM RANGE ATÉ O 100 ---

for x in range(90, 100):
    print(x)



# --- IDENTIFICANDO NO TERMINAL SE UM NÚMERO É PRIMOO ATRAVÉS DO IMPUT DO USER ---

a = int(input('Entre com um número: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('número {} é primo'.format(a))
else:
    print('número {} não é primo'.format(a))


# --- IMPRIMINDO OS NUMEROS PRIMOS NO INTERVALO DE 0 A 100 ---

for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)

# --- DETERMINADO UM VALOR DE INTERVALO DE NUMEROS PRIMOS ---
a = int(input('Entre com um valor: '))
for num in range(a+1):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        # print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num)


# --- WHILE | FORCANDO UMA REPETIÇÃO ATÉ QUE UMA AFIRMAÇÃO SEJA VERDADEIRA ---
a = 0
while a <= 10:
    print(a)
    a += 1

--- INSERINDO COM UMA NOTA CORRETA ---
nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota inválida. Entrar com outra nota: '))
print(nota)


#-- IDENTIFICANDO UMA NOTA DO ALUNO DIGITADA ERRADA NO SISTEMA --
a = int(input('Nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Nota inválida. Digite novamente: '))
b = int(input('Nota do segundo bimestre: '))
while b > 10:
    b = int(input('Nota inválida. Digite novamente: '))
c = int(input('Nota do terceiro bimestre: '))
while c > 10:
    c = int(input('Nota inválida. Digite novamente: '))
d = int(input('Nota do quarto bimestre: '))
while d > 10:
    d = int(input('Nota inválida. Digite novamente: '))
media = (a + b + c + d )/4
print(media)