#--- IMPORTANDO MAIS DE UMA FUNCAO ---
from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_letras import contador_letras, teste


# --- TV ---
televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)


# --- CALCULADORA 1 ---
calculadora = Calculadora(10, 5)
print(calculadora.multiplicacao())
print(calculadora.divisao())
print(calculadora.soma())
print(calculadora.subtracao())


# --- CONTADOR DE LETRAS ---
lista =['papagaio', 'gato', 'cachorro', 'cegonha']
print(contador_letras(lista))


# --- TESTE ---
print(teste())



