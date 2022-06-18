import json

with open("dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)


def menorValor():
    for i in dados:
        lista = []
        lista.append(i['valor'])
        for j in range(len(lista)):
            for n in range(j):
                if n <= j:
                    return n


def maiorValor():
    for i in dados:
        lista = []
        lista.append(i['valor'])
        for j in range(len(lista)):
            for n in range(j):
                if n >= j:
                    return n


def mediaDoMes():
    for i in dados:
        lista = []
        lista.append(i['valor'])
            for n in mediaLista:
                media = lista += i / n
                return media

