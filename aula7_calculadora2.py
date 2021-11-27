# --- DEFININDO A CLASSE DE UMA FUNÇÃO III ---
class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return  valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao (self, valor_a, valor_b):
        return valor_a / valor_b

calculadora = Calculadora()
print('Soma: {}'.format(calculadora.soma(8, 3)))
print('Subtracao: {}'.format(calculadora.subtracao(10, 3)))
print('Multiplicacao: {}'. format(calculadora.multiplicacao(5, 5)))
print('Divisao: {}'. format(calculadora.divisao(49, 7)))
