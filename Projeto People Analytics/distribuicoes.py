import os
import PySimpleGUI as sg
import matplotlib.pyplot as plt

def distribuicoes (pessoas, parametro, tipo):
    # parametro = chave a distribuir
    # tipo = tipo de dados a distribuir
    distrib={}
    for pessoa in pessoas:
        if tipo=="lista": #desportos, animais, destinos
            if parametro in pessoa.keys():
                for aux_parametro in pessoa[parametro]:
                    if aux_parametro in distrib:
                        distrib[aux_parametro] +=1
                    else:
                        distrib[aux_parametro] = 1
        elif tipo=="string": #profissao, religiao
            if parametro in pessoa.keys():
                if pessoa[parametro] in distrib:
                    distrib[pessoa[parametro]] += 1
                else:
                    distrib[pessoa[parametro]] = 1
        else: #dic
            if parametro in pessoa.keys():
                if parametro=="partido_politico":#partido politico
                    if pessoa[parametro]["party_abbr"] in distrib: 
                        distrib[pessoa[parametro]["party_abbr"] ] += 1
                    else:
                        distrib[pessoa[parametro]["party_abbr"] ] = 1
                if parametro== "morada": #morada
                    if pessoa[parametro]["distrito"] in distrib:
                       distrib[pessoa[parametro]["distrito"]] += 1
                    else:
                        distrib[pessoa[parametro]["distrito"]] = 1 
    return distrib


def ordena_valores(v):
    return v[1]

def topx (distrib, x):
    if x== '':
        x= 10
    valores = list(distrib.items())
    valores.sort(key = ordena_valores)
    novaDistrib = dict(valores[-int(x):])
    return novaDistrib

def graficos(distrib):
    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range (0, len(distrib.keys()))], distrib.keys(), rotation=75)
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9, wspace=0, hspace=0)
    plt.show()

def distribuicoes_pessoas(pessoas):
    sg.theme('LightBlue2')
    lista_distribuicoes= ['Desportos', 'Animais', 'Destinos', 'Profissão', 'Religião', 'Partido', 'Distrito']
    tradutor_chaves= {'Animais': 'animais', 'Desportos': 'desportos', 'Destinos': 'destinos_favoritos', 'Profissão': 'profissao', 'Religião': 'religiao', 'Partido': 'partido_politico', 'Distrito': 'morada'}
    coluna1= [[sg.Text(text='Distribuição por', pad=((25,0),(0,5)), size=(15,1), justification='right'),sg.Combo(lista_distribuicoes, size=(20,1), pad=((5,0),(0,5)), key='v_pesquisa_distribuicao')],
              [sg.Text(text='TOP', pad=((25,0),(0,5)), size=(15,1), justification='right'),sg.Input('', size=(20,1), pad=((5,0),(0,5)), key='v_pesquisa_top')]]
    coluna2=[[sg.Button('PESQUISAR', size=(15,2), pad=((10,0),(0,10)), key='-PESQUISA-')]]
    layout = [#sg.Text(text='', pad=((5,0),(0,0)))],
              [sg.Text(text='Distribuição de Pessoas',size=(20, 1), font=('Arial', 20), justification='left')],
              [sg.HorizontalSeparator(pad=((5,5),(7,7)))],
              [sg.Column(coluna1, element_justification='left'), sg.Column(coluna2, element_justification='left')]]  
    window =sg.Window('UM - Projeto People Analytics', layout, size=(900,600), modal=True, finalize=True)
    while True:
        event, values = window.read()
        print("\neventX ----->", event, " ValuesX ----->", values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-PESQUISA-':
            if values['v_pesquisa_distribuicao']== 'Desportos' or values['v_pesquisa_distribuicao']== 'Animais' or values['v_pesquisa_distribuicao']== 'Destinos':
                graficos(topx(distribuicoes(pessoas, tradutor_chaves[values['v_pesquisa_distribuicao']], 'lista'), values['v_pesquisa_top']))
            elif values['v_pesquisa_distribuicao']== 'Profissão' or values['v_pesquisa_distribuicao']== 'Religião':
                graficos(topx(distribuicoes(pessoas, tradutor_chaves[values['v_pesquisa_distribuicao']], 'string'), values['v_pesquisa_top']))
            elif values['v_pesquisa_distribuicao']== 'Partido' or values['v_pesquisa_distribuicao']== 'Distrito':
                graficos(topx(distribuicoes(pessoas, tradutor_chaves[values['v_pesquisa_distribuicao']], 'dic'), values['v_pesquisa_top']))
