# --- IDENTIFICANDO SE UMA TV ESTÁ LIGADA OU DESLIGADA | MUDANÇA DE CANAL ---
class Televisao:
    #variável inicial | Inicialmente a TV está desligada
    def __init__(self):
        self.ligada = False
        self.canal  = 5
    #ligando a TV caso esteja desligada
    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

#--- AO CRIAR MÓDULOS, SEMPRE FAZER OS TESTES NOS MESMOS ---
if __name__ == '__main__':
    televisao = Televisao()
    print('Televisao ligada: {}'.format(televisao.ligada))
    #ligando a TV
    televisao.power()
    print('Televisao ligada: {}'.format(televisao.ligada))
    #desligando a TV
    televisao.power()
    print('Televisao ligada: {}'.format(televisao.ligada))
    #aumentando o canal 2x | Caso a TV esteja ligada
    televisao.power()
    print('Canal: {}'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal: {}'.format(televisao.canal))
    #diminuindo o canal 1x
    televisao.diminui_canal()
    print('Canal: {}'.format(televisao.canal))












