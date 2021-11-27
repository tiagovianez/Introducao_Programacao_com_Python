import shutil
def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media =[]
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print('Nome do aluno: {}'.format(aluno))
        print('Notas: {}'.format(lista_notas))
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print('Média do aluno: {}'.format(media(lista_notas)))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, '/home/tiago/Documents/Projects/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, '/home/tiago/Documents/')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_arquivo('Data Engineer at Airbnb.\n'
    #                  'Data Engineer at Netflix.\n'
    #                  'Data Engineer at Meta.\n'
    #                  'Data Engineer Analytcs at Google.\n')

    # atualizar_arquivo('\nData Engineer at QuantumBlack.\n')
    # aluno = 'Cesar, 10, 8, 7, 9\n' \
    #         'Tiago, 8, 8, 9, 7\n' \
    #         'Felipe, 9, 8, 7, 6\n' \
    #         'Lucas, 8, 7, 7, 9\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')