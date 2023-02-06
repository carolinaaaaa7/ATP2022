import json
import PySimpleGUI as sg
from lista_pessoas import *
from gestao_pessoas import *
from distribuicoes import *
from acerca import *

# Pessoas = [pessoa]
# pessoa = {nome, idade, sexo, {morada}, BI, descrição, profissao, {partido_politico}, religiao, [desportos], [animais], [figura_publica_pt], marca_carro, [destinos_favoritos], {atributos}}
# morada {cidade, distrito}
# partido_politico {party_abbr, party_name}
# desportos [desporto]
# animais [animal]
# figura_publica_pt [figura]
# destinos_favoritos [destino_favorito]
# atributos = {
#    'fumador': false,
#    'gosta_cinema': false,
#    'gosta_viajar': true,
#    'acorda_cedo': false,
#    'gosta_ler': true,
#    'gosta_musica': false,
#    'gosta_comer': false,
#    'gosta_animais_estimacao': true,
#    'gosta_dancar': true, 
#    'comida_favorita': 'italiana' }

def ordem_nome(e):
    return e['nome']

def verifica_întegridade(pessoas, lista_existente):
    # verifica a integridade (se campos Religião e Descrição existem em todos os registos)
    sem_religiao  = 0    # conta os que NÃO têm o campo religião
    sem_descricao = 0    # conta os que NÃO têm o campo descrição
    mensagem1 = "Tamanho do Ficheiro a Importar : " + str(len(pessoas)) + " PESSOAS.\n"
    mensagem2 = ""
    mensagem3 = ""
    mensagem4 = ""
    mensagem5 = ""
    lista_bi_cc= []
    for pessoa_existente in lista_existente:
        documento = 'BI' if 'BI' in pessoa_existente else 'CC'
        lista_bi_cc.append(pessoa_existente[documento])
    lista_eliminados = []
    for posicao, pessoa in enumerate(pessoas):
        # se existem AMBAS ou NENHUMAS 
        if ('BI' in pessoa and 'CC' in pessoa) or ('BI' not in pessoa and 'CC' not in pessoa):
            lista_eliminados.append(pessoa)
        else:
            # se existe UMA delas mas valor = Vazio
            if ('BI' in pessoa and pessoa['BI']=='') or ('CC' in pessoa and pessoa['CC']==''):
                lista_eliminados.append(pessoa)
            else:
                # Nota: se chegou aqui, existe apenas UMA chave NÃO Vazia
                # se existe chave válida mas é REPETIDA
                if ('BI' in pessoa and pessoa['BI'] in lista_bi_cc) or ('CC' in pessoa and pessoa['CC'] in lista_bi_cc):
                    lista_eliminados.append(pessoa)
                else:
                    # tudo bem, a Pessoa será carregada
                    if 'religiao' not in pessoa:
                        pessoa['religiao']="----------"
                        sem_religiao += 1
                    if 'descrição' not in pessoa:
                        pessoa['descrição']="----------"
                        sem_descricao += 1
                    documento = 'BI' if 'BI' in pessoa else 'CC'
                    lista_existente.append(pessoa)
                    lista_bi_cc.append(pessoa[documento])
    
    if sem_religiao!=0: 
        mensagem4 = "\nNota: Existiam " + str(sem_religiao) + " PESSOAS sem o campo «Religião». Corrigido!                \n"
    if sem_descricao!=0: 
        mensagem5 = "\nNota: Existiam " + str(sem_descricao) + " PESSOAS sem o campo «Descrição». Corrigido!               \n"
    mensagem2 = "\nTotal de Pessoas Importadas    : " + str(len(pessoas)-len(lista_eliminados)) + " PESSOAS.               \n"
    mensagem3 = "\nTotal Geral de Pessoas         : " + str(len(lista_existente)) + " PESSOAS.                             \n"

    sg.popup(mensagem1 + mensagem2 + mensagem3 + mensagem4 + mensagem5, title='Informações                                            ')
    pessoas = lista_existente
    pessoas.sort(key=ordem_nome)

    return pessoas

# carrega ficheiro (se faz_update=True apenas vai verificar a integridade do novo ficheiro cerregado
def carrega_ficheiro (pessoas, fnome, faz_update):
    with open(fnome, encoding="UTF-8") as f:
        dados = json.load(f)
    f.close()
    if faz_update:
        pessoas =  verifica_întegridade(dados['pessoas'], pessoas)
    else:
        pessoas =  verifica_întegridade(dados['pessoas'], [])
    return pessoas

def grava_ficheiro(pessoas, fnome):
    dicionario = {}
    dicionario['pessoas'] = pessoas
    with open(fnome, 'w', encoding='utf-8') as f:
        json.dump(dicionario, f, ensure_ascii=False, indent = 2)
    sg.popup("Ficheiro " + fnome + " gravado com SUCESSO.\n", title='Informação')

pessoas=[]
sg.theme('LightBlue2')
menu_inicio=[['Ficheiro', ['Abrir Ficheiro', 'Acrescentar Ficheiro','Gravar Ficheiro', 'Sair']],
             ['Pessoas',['Lista de Pessoas', 'Gestão de Pessoas', 'Dados Estatísticos']],
             ['Acerca de',['Ficha Técnica']]]
layout=[[sg.Menu(menu_inicio)],
        [sg.Text(key='-EXPANDE-', font='ANY 1', pad=(0,0))],
        [sg.StatusBar(' Nº de registos carregados: ' + str(len(pessoas)), key='-ESTADO-')]]
window =sg.Window('UM - Projeto People Analytics', layout, resizable=True, disable_close=True).Finalize()
window.Maximize()
window['-EXPANDE-'].expand(True, True, True)
while True:
    event, values = window.read()    
    if event in (sg.WIN_CLOSED, 'Sair'):
        escolha = sg.popup('\nDeseja gravar este ficheiro?                      \n', button_type=sg.POPUP_BUTTONS_YES_NO, custom_text = ('Gravar','Não Gravar'),  title='ATENÇÃO')
        if escolha=='Gravar':
            ficheiro = sg.popup_get_file('nota: sem Janela PySimpleGUI', no_window=True, file_types=(("JSON", ".json"),), default_extension='json', save_as=True)
            if ficheiro:         
                grava_ficheiro(pessoas, ficheiro)
        else:
            break
    elif event == 'Abrir Ficheiro':
        ficheiro = sg.popup_get_file('nota: sem Janela PySimpleGUI', no_window=True)
        if ficheiro:         
            pessoas = carrega_ficheiro(pessoas, ficheiro, False)
    elif event == 'Acrescentar Ficheiro':
        ficheiro = sg.popup_get_file('nota: sem Janela PySimpleGUI', no_window=True)
        if ficheiro:         
            pessoas = carrega_ficheiro(pessoas, ficheiro, True)
    elif event == 'Gravar Ficheiro':
        ficheiro = sg.popup_get_file('nota: sem Janela PySimpleGUI', no_window=True, file_types=(("JSON", ".json"),), default_extension='json', save_as=True)
        if ficheiro:         
            grava_ficheiro(pessoas, ficheiro)
    elif event == 'Gestão de Pessoas':
        if len(pessoas)>0:
            gestao_pessoas(pessoas, 0)
        else:
            sg.popup('\nNão existem «Pessoas» para gerir.\n', title='ATENÇÃO')    
    elif event == 'Lista de Pessoas':
        pessoas, indice = lista_pessoas(pessoas)
        if indice!=None:
            gestao_pessoas(pessoas, indice)
    elif event == 'Dados Estatísticos':
        if len(pessoas)>0:
            distribuicoes_pessoas(pessoas)
        else:
            sg.popup('\nNão existem «Pessoas» para distribuir.\n', title='ATENÇÃO')       
    elif event == 'Ficha Técnica':
        acerca_de()

    # atualiza o ESTADO
    window['-ESTADO-'].update(' Nº de registos carregados: ' + str(len(pessoas)))
window.close()