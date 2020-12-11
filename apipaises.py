import json

import requests
import sys
url_all = 'https://restcountries.eu/rest/v2/all'
url_name = 'https://restcountries.eu/rest/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print('Erro ao fazer requisição  em:', url)

def parsing(texto_da_resposta):
    try:
        return json.loads(texto_da_resposta)
    except:
        print('Erro ao fazer parsing')

def contagem_de_paises():
    resposta = requisicao(url_all)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)

def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])

def mostrar_populacao(nome_do_pais):
    resposta = requisicao('{}/{}'.format(url_name, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('{}:{} habitantes'.format(pais['name'], pais['population']))
    else:
        print('Pais não encontrado')

def mostrar_moedas(nome_do_pais):
    resposta = requisicao('{}/{}'.format(url_name, nome_do_pais))
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print('Moedas do', pais['name'])
                moedas = pais['currencies']
                for moeda in moedas:
                    print('{}:{}'.format(moeda['name'], moeda['code']))
    else:
        print('Pais não encontrado')

def ler_nome_do_pais():
    try:
        nome_do_pais = argumento2 = sys.argv[2]
        return nome_do_pais
    except:
        print('É preciso passar o nome do país')




if __name__=='__main__':

    if len(sys.argv) ==1:
        print('## Bem vindo ao sistema de países ##')
        print('Uso: python paises.py <ação><nome do pais>')
        print('Ações disponiveis: contagem, moeda, população')
    else:
        argumento1 = sys.argv[1]

        if argumento1 =='contagem':
           numero_de_paises = contagem_de_paises()
           print('Existem {} paises no mundo todo'.format(numero_de_paises))
        elif argumento1 == 'moeda':
            pais = ler_nome_do_pais()
            if pais:
                mostrar_moedas(pais)
        elif argumento1 == 'populacao':
            pais = ler_nome_do_pais()
            if pais:
                mostrar_populacao(pais)
        else:
            print('Argumento invalido')

