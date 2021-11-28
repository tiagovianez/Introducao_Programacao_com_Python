# --- O QUE SÃO VARIAVEIS E COMO MANIPULA-LAS ATRAVÉS DE OPERADORES ARITMETICOS E INTERAÇÃO COM USUÁRIO ---
#---- CONDIÇÕES ----
a = 20
b = 3

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print(soma)
print(subtracao)
print(divisao)
print(multiplicacao)
print(resto)


#--- IDENTIFICANDO QUAL O TIPO DA VARIÁVEL ---
print(type(soma))


#--- CONVERTENDO UMA VARIÁVEL DO TIPO INTEIRO PARA STRING ---
soma: str = str(soma)
print(type(soma))


#--- CONCATENAÇÃO DE VARIÁVEIS ---
print('soma: ' + str(soma))


#--- Cálculos ---
print (soma)
print (subtracao)


# --- CONVERTENDO PARA TIPO 'string' ---
print ('subtracao: ' + str(subtracao))
print (multiplicacao)
print(divisao)
print(resto)


# # --- ARREDONDANDO UM VALOR DE ACORDO COM A CONDIÇÃO 'int' ---
print(int(divisao))


# ---- DETERMINANDO UMA VARIÁVEL DO TIPO 'int' PARA EFETUAR CÁLCULO ---
x = '7'
soma2 = int(x) + 1
print(soma2)


#--- INTERAÇÃO COM O USUÁRIO | DETERMINADO VARIAVEL INTEIRA PARA INSERIR VALORES NO INPUT ---
a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b


# --- COMANDO 'format' | CONCATENAÇÃO INDEPENDENTE DE UMA 'float' OU 'string' ---
print('soma: {sm}. '
        '\nsubtracao: {sub}'
        '\nmultiplicacao: {mult}'
        '\ndivisao: {div}'
        '\nresto: {res}'. format(sm=soma,
                                 sub=subtracao,
                                 mult=multiplicacao,
                                 div=divisao,
                                 res=resto))
