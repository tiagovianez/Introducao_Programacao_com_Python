# --- CONSTRUINDO MÉTODOS, FUNÇÕES E CLASSES EM PYTHON ---
# --- DEFININDO A CLASSE DE UMA FUNÇÃO I ---
class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(a, b):
        return a + b

    def subtracao(c, d):
        return  c - d

    def multiplicacao(e, f):
        return e * f

    def divisao (g, h):
        return g / h

    print('soma: {}'.format(soma(8, 11)))
    print('subtracao: {}'.format(subtracao(45, 41)))
    print('multiplacao: {}'.format(multiplicacao(5, 6)))
    print('divisao: {}'.format(divisao(80, 13)))

calculadora = Calculadora(10, 5)
print(calculadora.valor_b)
print(calculadora.valor_a)


# # --- DEFININDO A CLASSE DE UMA FUNÇÃO II ---
class Calculadora:
    #--- definindo variáveis ---
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return  self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao (self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 5)
    print('Soma: {}'.format(calculadora.soma()))
    print('Subtracao: {}'.format(calculadora.subtracao()))
    print('Multiplicacao: {}'.format(calculadora.multiplicacao()))
    print('Divisao: {}'.format(calculadora.divisao()))