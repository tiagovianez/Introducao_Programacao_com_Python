# --- CONTANDO LETRAS DE CADA PALAVRA DE UMA LISTA ---
def contador_letras(lista_palavras):
    #determinando uma lista
    contador = []
    for x in lista_palavras:
        #Irá devolver uma lista com o total de letras por posição
        quantidade = len(x)
        contador.append(quantidade)
    return  contador

def teste():
    return 'teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'girafa', 'lobo','leao', 'raposa']
    print(contador_letras(lista))














