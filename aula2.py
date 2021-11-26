# --- O QUE SÃO VARIAVEIS E COMO MANIPULA-LAS ATRAVÉS DE OPERADORES ARITMETICOS E INTERAÇÃO COM USUÁRIO ---


#---- Condições ----
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



#--- Identificando qual o tipo da variável ---
print(type(soma))


#-- Convertendo uma variável do tipo inteiro para uma string ---
soma: str = str(soma)
print(type(soma))


#--- Concatenação de variáveis ---
print('soma: ' + str(soma))


#--- Cálculos ---
print (soma)
print (subtracao)

# --- Convertendo para tipo 'string' ---
print ('subtracao: ' + str(subtracao))



print (multiplicacao)
print(divisao)
print(resto)

# # --- Se eu quiser arrendodar o valor de acordo com que foi dado da condição, determinar um: 'int' ---
print(int(divisao))


# ---- Determinando uma variável do tipo 'int' para efetuar cálculo ---
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


# --- Comando FORMAT | Ele concatena independente se for um float ou string---

print('soma: {sm}. \nsubtracao: {sub}'
      '\nMultiplicacao : {mult}'
      '\nDivisao: {div}'
      '\nResto: {res}' .format(sm=soma,
                               sub=subtracao,
                               res=resto,
                               mult=multiplicacao,
                               div=divisao))


a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: {sm}. '
        '\nsubtracao: {sub}'
        '\nmultiplicacao: {mult}'
        '\ndivisao: {div}'
        '\nresto: {res}'. format(sm=soma,
                                 sub=subtracao,
                                 mult=multiplicacao,
                                 div=divisao,
                                 res=resto))

