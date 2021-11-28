import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/01001000/json/'.format(cep))
    print(response.status_code)
    #--- FORMATO DE DICIONÁRIO | ACESSANDO DETERMINADA INFORMAÇÃO ---
    print(response.json())
    print(type(response.json()))
    dados_cep = response.json()
    print(dados_cep['localidade'])
    print(dados_cep['bairro'])
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return  dados_pokemon

#--- FAZENDO LEITURA DE PÁGINAS ---
def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    response = retorna_response('https://www.quantumblack.com/careers')
    print(response)
    # retorna_dados_cep('01001000')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)