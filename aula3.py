# --- CRIANDO UM CÓDIGO EM PYTHON QUE FUNCIONE DE ACORDO COM A RELACAO DAS VARIÁVEIS ---
a = int(input('Inserir o primeiro número: '))
b = int(input('Inserir o segundo número: '))
c = int(input('Inserir o terceiro número: '))

if a > b and a > c:
    print('O maior número é: {}'.format(a))
elif b > a and b > c:
    print('O maior número é: {}'.format(b))
else:
    print('O maior número é: {}'.format(c))

# --- IDENTIFICANDO SE UM NÚMERO É PAR OU ÍMPAR ---
a = int(input('Entre com um valor: '))
b = int(input('Entre com um valor: '))

resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or resto_b == 0:
    print('Um número par foi digitado')
else:
    print('Nenhum número par foi digitado')

# --- IDENTIFICANDO SE UM NÚMERO NÃO É PAR E NEM ÍMPAR (MENTIRA)---

a = int(input('Entre com um valor: '))
b = int(input('Entre com um valor: '))

resto_a = a % 2
resto_b = b % 2
if resto_a == 0 or not resto_b == 0:
    print('Um número par foi digitado')
else:
    print('Nenhum número par foi digitado')

#-- RODANDO A MÉDIA DE UM ALUNO --
a = int(input('Nota do Primeiro bimestre: '))
b = int(input('Nota do Segundo bimestre: '))
c = int(input('Nota do Terceiro bimestre: '))
d = int(input('Nota do Quarto bimestre: '))

media = (a + b + c + d) / 4
print('média: {}'. format(media))

#-- IDENTIFICANDO UMA NOTA DO ALUNO DIGITADA ERRADA NO SISTEMA --
a = int(input('Nota do Primeiro bimestre: '))
b = int(input('Nota do Segundo bimestre: '))
c = int(input('Nota do Terceiro bimestre: '))
d = int(input('Nota do Quarto bimestre: '))

media = (a + b + c + d) / 4
if a <=10 and b <= 10 and c <= 10:
    print('média: {}'. format(media))
else:
    print('Foi informado alguma nota digitada de forma incorreta')

#-- IDENTIFICANDO UMA NOTA DO ALUNO DIGITADA ERRADA NO SISTEMA --
a = int(input('Nota do Primeiro bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Nota do Segundo bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Nota do Terceiro bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Nota do Quarto bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))


media = (a + b + c + d) / 4
print('media: {}'. format(media))
