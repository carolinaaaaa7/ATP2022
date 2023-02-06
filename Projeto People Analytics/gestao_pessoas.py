import PySimpleGUI as sg

def limpa_pessoa():
    nova_pessoa = {}
    nova_pessoa['nome']=''
    nova_pessoa['idade']=''
    nova_pessoa['BI']=''
    nova_pessoa['CC']=''
    nova_pessoa['morada']={}
    nova_pessoa['morada']['cidade']=''
    nova_pessoa['morada']['distrito']=''
    nova_pessoa['sexo']=''
    nova_pessoa['religiao']=''    
    nova_pessoa['marca_carro']=''
    nova_pessoa['profissao']=''
    nova_pessoa['partido_politico']={}
    nova_pessoa['partido_politico']['party_abbr']=''
    nova_pessoa['partido_politico']['party_name']=''
    nova_pessoa['descrição']=''
    nova_pessoa['desportos']=[]
    nova_pessoa['animais']=[]
    nova_pessoa['figura_publica_pt']=[]    
    nova_pessoa['destinos_favoritos']=[]
    nova_pessoa['atributos']={}
    nova_pessoa['atributos']['fumador']=False
    nova_pessoa['atributos']['gosta_cinema']=False
    nova_pessoa['atributos']['gosta_viajar']=False
    nova_pessoa['atributos']['acorda_cedo']=False
    nova_pessoa['atributos']['gosta_ler']=False
    nova_pessoa['atributos']['gosta_musica']=False
    nova_pessoa['atributos']['gosta_comer']=False
    nova_pessoa['atributos']['gosta_animais_estimacao']=False
    nova_pessoa['atributos']['gosta_dancar']=False
    nova_pessoa['atributos']['comida_favorita']=''
    return nova_pessoa

def gestao_pessoas(pessoas, indice):
    sg.theme('LightBlue2')
    leitura = True        # variável leitura: se True, campos não editáveis, só de leitura
    alteracao = False     # variável para distinguir quando o Registo é Gravado em modo «EDITAR» ou em modo «NOVO»
    lista_desportos = []
    lista_animais = []
    lista_figuras = []
    lista_destinos = []
    for pessoa in pessoas:
        for desporto in pessoa['desportos']:
            if desporto not in lista_desportos:
                lista_desportos.append(desporto)
        for animal in pessoa['animais']:
            if animal not in lista_animais:
                lista_animais.append(animal)
        for figura in pessoa['figura_publica_pt']:
            if figura not in lista_figuras:
                lista_figuras.append(figura)
        for destino in pessoa['destinos_favoritos']:
            if destino not in lista_destinos:
                lista_destinos.append(destino)
    lista_desportos.sort()
    lista_animais.sort()
    lista_figuras.sort()
    lista_destinos.sort()

    pessoa = pessoas[indice]
    documento = 'BI' if 'BI' in pessoa else 'CC'
    tipo_doc = True if documento == 'BI' else False
    tam_list =27
    tam_atrib=13

    # para abrir janelas de contexto - click com botão direito do rato
    popup_desporto=['', ['Remover Desporto']]
    popup_animal=['', ['Remover Animal']]
    popup_figura=['', ['Remover Figura']]
    popup_destino=['', ['Remover Destino']]

    
    layout=[[sg.Text(text='Ficha Individual da Pessoa',size=(40, 1), font=('Arial', 20), justification='left', pad=(8,0))],
            [sg.HorizontalSeparator(pad=((5,5),(7,7)))],
            [sg.Text(text='Nome',      size=(8,1), justification='right'),sg.Input(pessoa['nome'], size=(50,1), disabled=leitura, key='v_nome'),
             sg.Radio('BI', "Radio1", pad=((180,0),(0,0)), default=tipo_doc, disabled=leitura, size=(1,1), key='v_BI'), sg.Radio('CC', "Radio1", disabled=leitura, key='v_CC'), sg.Input(pessoa[documento], size=(20,1), disabled=leitura, key='v_documento')],
            [sg.Text(text='Morada',    size=(8,1), justification='right'),sg.Input(pessoa['morada']['cidade'], size=(50,1), disabled=leitura, key='v_cidade'),
             sg.Text(text='Idade',     size=(8,1), justification='right'),sg.Input(pessoa['idade'], size=(10,1), disabled=leitura, justification='center', enable_events=True, key='v_idade'),
             sg.Text(text='Religião',  pad=((24,0),(0,0)), size=(10,1), justification='right'),sg.Input(pessoa['religiao'], size=(20,1), disabled=leitura, key='v_religiao')],
            [sg.Text(text=' ',         size=(8,1), justification='right'),sg.Input(pessoa['morada']['distrito'], size=(50,1), disabled=leitura, key='v_distrito'),
             sg.Text(text='Sexo',      size=(8,1), justification='right'),sg.Combo(['masculino', 'feminino', 'outro'], size=(9,1), default_value=pessoa['sexo'], disabled=leitura, key='v_sexo'),
             sg.Text(text='Carro',     size=(11,1), justification='right'),sg.Input(pessoa['marca_carro'], size=(20,1), disabled=leitura, key='v_carro')],
            [sg.Text(text='Profissão', size=(8,1), justification='right'),sg.Input(pessoa['profissao'], size=(50,1), disabled=leitura, key='v_profissao'),
             sg.Text(text='Partido',   size=(8,1), justification='right'),sg.Input(pessoa['partido_politico']['party_abbr'], size=(10,1), disabled=leitura, key='v_partido_abreviatura'),
             sg.Input(pessoa['partido_politico']['party_name'],pad=((8,0),(0,0)), size=(35,1), disabled=leitura, key='v_partido_nome')],
            [sg.Text(text='Descrição', size=(8,1), justification='right'),sg.Multiline(pessoa['descrição'], size=(109,3), disabled=leitura, key='v_descricao')],
            [sg.HorizontalSeparator(pad=((5,15),(10,10)))],
            [sg.Text('Desportos         ', size=(tam_list, 1), justification='left', pad=(8,0)),
             sg.Text('Animais           ', size=(tam_list, 1), justification='left', pad=(0,0)),
             sg.Text('Figuras Públicas  ', size=(tam_list, 1), justification='left', pad=(0,0)),
             sg.Text('Destinos Favoritos', size=(tam_list, 1), justification='left', pad=(0,0))],
            [sg.Listbox(values=pessoa['desportos'], size=(tam_list, 5), right_click_menu=popup_desporto, key='v_desportos'),
             sg.Listbox(values=pessoa['animais'], pad=((8,5),(0,0)), size=(tam_list, 5), right_click_menu=popup_animal, key='v_animais'),
             sg.Listbox(values=pessoa['figura_publica_pt'], pad=((8,5),(0,0)), size=(tam_list, 5), right_click_menu=popup_figura, key='v_figuras'),
             sg.Listbox(values=pessoa['destinos_favoritos'], pad=((8,5),(0,0)),size=(tam_list, 5), right_click_menu=popup_destino, key='v_destinos')],
            [sg.Combo(lista_desportos, pad=((5,0),(0,0)),  size=(tam_list-3,1), disabled=leitura, key='vl_desportos'), sg.Button('+', pad=((4,0),(0,0)), size=(1,1), disabled=leitura, key='-DESPORTOS-'),
             sg.Combo(lista_animais,   pad=((14,0),(0,0)), size=(tam_list-3,1), disabled=leitura, key='vl_animais'), sg.Button('+', pad=((4,0),(0,0)), size=(1,1), disabled=leitura, key='-ANIMAIS-'),
             sg.Combo(lista_figuras,   pad=((14,0),(0,0)), size=(tam_list-3,1), disabled=leitura, key='vl_figura_publica_pt'), sg.Button('+', pad=((4,0),(0,0)), size=(1,1), disabled=leitura, key='-FIGURAS-'),
             sg.Combo(lista_destinos,  pad=((14,0),(0,0)), size=(tam_list-3,1), disabled=leitura, key='vl_destinos_favoritos'), sg.Button('+', pad=((4,0),(0,0)), size=(1,1), disabled=leitura, key='-DESTINOS-')],
            [sg.HorizontalSeparator(pad=((5,5),(10,10)))],
            [sg.Checkbox('Fumador',         size=(tam_atrib, 1), default=pessoa['atributos']['fumador'], disabled=leitura, key='v_fumador'), 
             sg.Checkbox('Gosta de Cinema', size=(tam_atrib, 1), default=pessoa['atributos']['gosta_cinema'], disabled=leitura,  key='v_cinema'),
             sg.Checkbox('Gosta de Viajar', size=(tam_atrib, 1), default=pessoa['atributos']['gosta_viajar'], disabled=leitura,  key='v_viajar'),
             sg.Checkbox('Acorda Cedo',     size=(tam_atrib, 1), default=pessoa['atributos']['acorda_cedo'], disabled=leitura,  key='v_acorda'),
             sg.Checkbox('Gosta de Ler',    size=(tam_atrib, 1), default=pessoa['atributos']['gosta_ler'], disabled=leitura,  key='v_ler'),
             sg.Checkbox('Gosta de Música', size=(tam_atrib, 1), default=pessoa['atributos']['gosta_musica'], disabled=leitura,  key='v_musica')], 
            [sg.Checkbox('Gosta de Comer',  size=(tam_atrib, 1), default=pessoa['atributos']['gosta_comer'], disabled=leitura,  key='v_comer'),
             sg.Checkbox('Gosta de Animais',size=(tam_atrib, 1), default=pessoa['atributos']['gosta_animais_estimacao'], disabled=leitura, key='v_animais_est'),
             sg.Checkbox('Gosta de Dançar', size=(tam_atrib, 1), default=pessoa['atributos']['gosta_dancar'], disabled=leitura,  key='v_dançar'),
             sg.Text(text='Comida Favorita',size=(16, 1), justification='right'),sg.Input(pessoa['atributos']['comida_favorita'], size=(37, 1), disabled=leitura, key='v_comida')],
            [sg.HorizontalSeparator(pad=((5,5),(10,20)))],
            [sg.Push(),
             sg.Button('', image_filename='primeiro.png', image_size=(40, 40), disabled=not leitura, visible=leitura, key='-PRIMEIRO-'),
             sg.Button('', image_filename='anterior.png', image_size=(40, 40), disabled=not leitura, visible=leitura, key='-ANTERIOR-'),
             sg.Button('', image_filename='seguinte.png', image_size=(40, 40), disabled=not leitura, visible=leitura, key='-SEGUINTE-'),
             sg.Button('', image_filename='ultimo.png',   image_size=(40, 40), disabled=not leitura, visible=leitura, key='-ULTIMO-'),
             sg.Button('EDITAR',     size=(12,2), button_color=('black','yellow'), disabled=not leitura, visible=leitura, key='-EDITAR-'),
             sg.Button('NOVO',     size=(12,2), button_color=('white','green'), disabled=not leitura, visible=leitura, key='-NOVO-'),
             sg.Button('APAGAR',   size=(12,2), button_color=('white','red'),   disabled=not leitura, visible=leitura, key='-APAGAR-'),
             sg.Button('GRAVAR',   size=(12,2), button_color=('white','green'), disabled=leitura, visible=not leitura, key='-GRAVAR-'),
             sg.Button('CANCELAR', size=(12,2), button_color=('white','red'),   disabled=leitura, visible=not leitura, key='-CANCELAR-')],
            [sg.StatusBar(' Nº do registo: ' + str(indice+1) + '    :: Total de '+ str(len(pessoas)) + ' registos.', key='-RODAPE-')]]
    window = sg.Window('UM - Projeto People Analytics', layout, size=(900,600), modal=True, resizable=False, finalize=True)
#disable close 
    while True:
        event, values = window.read()
        dados_invalidos = False  #controla campos obrigatórios
        match event:
            case sg.WIN_CLOSED | 'Exit':
                break
            case '-PRIMEIRO-':
                indice = 0
                pessoa = pessoas[indice]
            case '-ANTERIOR-':
                if indice==0:
                    sg.popup('\nInício do Ficheiro.                         \n', title='ATENÇÃO')
                else:
                    indice = indice - 1
                    pessoa = pessoas[indice]
            case '-SEGUINTE-':
                if indice==(len(pessoas)-1):
                    sg.popup('\nFim do Ficheiro.                            \n', title='ATENÇÃO')
                else:
                    indice = indice + 1
                    pessoa = pessoas[indice]
            case '-ULTIMO-':
                indice = len(pessoas)-1
                pessoa = pessoas[indice]
            case '-EDITAR-':
                leitura = False
                alteracao = True
                window['-PRIMEIRO-'].update(disabled=not leitura, visible=leitura)
                window['-ANTERIOR-'].update(disabled=not leitura, visible=leitura)
                window['-SEGUINTE-'].update(disabled=not leitura, visible=leitura)
                window['-ULTIMO-'].update(disabled=not leitura, visible=leitura)
                window['-EDITAR-'].update(disabled=not leitura, visible=leitura)
                window['-NOVO-'].update(disabled=not leitura, visible=leitura)
                window['-APAGAR-'].update(disabled=not leitura, visible=leitura)
                window['-GRAVAR-'].update(disabled=leitura, visible=not leitura)
                window['-CANCELAR-'].update(disabled=leitura, visible=not leitura)
                window['-RODAPE-'].update(' ')
            case '-NOVO-':
                leitura = False
                alteracao = False
                pessoa = limpa_pessoa()
                window['-PRIMEIRO-'].update(disabled=not leitura, visible=leitura)
                window['-ANTERIOR-'].update(disabled=not leitura, visible=leitura)
                window['-SEGUINTE-'].update(disabled=not leitura, visible=leitura)
                window['-ULTIMO-'].update(disabled=not leitura, visible=leitura)
                window['-EDITAR-'].update(disabled=not leitura, visible=leitura)
                window['-NOVO-'].update(disabled=not leitura, visible=leitura)
                window['-APAGAR-'].update(disabled=not leitura, visible=leitura)
                window['-GRAVAR-'].update(disabled=leitura, visible=not leitura)
                window['-CANCELAR-'].update(disabled=leitura, visible=not leitura)
                window['-RODAPE-'].update(' ')
            case '-APAGAR-':
                escolha = sg.popup('\nQuer mesmo APAGAR o registo?                      \n', button_type=sg.POPUP_BUTTONS_YES_NO, custom_text = ('Sim','Não'),  title='ATENÇÃO')
                if escolha=='Sim':
                    del pessoas[indice]
                    indice = 0
                    pessoa = pessoas[indice]
                
            case '-CANCELAR-':
                pessoa = pessoas[indice]
                leitura = True
                alteracao = False
                window['-PRIMEIRO-'].update(disabled=not leitura, visible=leitura)
                window['-ANTERIOR-'].update(disabled=not leitura, visible=leitura)
                window['-SEGUINTE-'].update(disabled=not leitura, visible=leitura)
                window['-ULTIMO-'].update(disabled=not leitura, visible=leitura)
                window['-EDITAR-'].update(disabled=not leitura, visible=leitura)
                window['-NOVO-'].update(disabled=not leitura, visible=leitura)
                window['-APAGAR-'].update(disabled=not leitura, visible=leitura)
                window['-GRAVAR-'].update(disabled=leitura, visible=not leitura)
                window['-CANCELAR-'].update(disabled=leitura, visible=not leitura)
            case '-DESPORTOS-':
                pessoa['desportos'].append(values['vl_desportos'])
                window['v_desportos'].update(pessoa['desportos'], disabled=leitura)
            case '-ANIMAIS-':
                pessoa['animais'].append(values['vl_animais'])
                window['v_animais'].update(pessoa['animais'], disabled=leitura)
            case '-FIGURAS-':
                pessoa['figura_publica_pt'].append(values['vl_figura_publica_pt'])
                window['v_figuras'].update(pessoa['figura_publica_pt'], disabled=leitura)
            case '-DESTINOS-':
                pessoa['destinos_favoritos'].append(values['vl_destinos_favoritos'])
                window['v_destinos'].update(pessoa['destinos_favoritos'], disabled=leitura)
            case 'Remover Desporto':
                try:
                    pessoa['desportos'].remove(values['v_desportos'][0])
                    window['v_desportos'].update(pessoa['desportos'], disabled=leitura)
                except:
                    sg.popup('\nClick com o Rato em cima do Item a REMOVER.                         \n', title='ATENÇÃO')

            case 'Remover Animal':
                try:
                    pessoa['animais'].remove(values['v_animais'][0])
                    window['v_animais'].update(pessoa['animais'], disabled=leitura)
                except:
                    sg.popup('\nClick com o Rato em cima do Item a REMOVER.                         \n', title='ATENÇÃO')
            case 'Remover Figura':
                try:
                    pessoa['figura_publica_pt'].remove(values['v_figuras'][0])
                    window['v_figuras'].update(pessoa['figura_publica_pt'], disabled=leitura)
                except:
                    sg.popup('\nClick com o Rato em cima do Item a REMOVER.                         \n', title='ATENÇÃO')
            case 'Remover Destino':
                try:
                    pessoa['destinos_favoritos'].remove(values['v_destinos'][0])
                    window['v_destinos'].update(pessoa['destinos_favoritos'], disabled=leitura)
                except:
                    sg.popup('\nClick com o Rato em cima do Item a REMOVER.                         \n', title='ATENÇÃO')

            case '-GRAVAR-':
                if values['v_nome']=='' or not values['v_idade'].isnumeric() or values['v_documento']=='':
                    sg.popup('\nCampos obrigatórios por preencher [ Nome, Idade, BI/CC ].                                     \n', title='ATENÇÃO     ')
                    dados_invalidos = True
                else:
                    dados_invalidos = False
                    leitura = True
                    window['-PRIMEIRO-'].update(disabled=not leitura, visible=leitura)
                    window['-ANTERIOR-'].update(disabled=not leitura, visible=leitura)
                    window['-SEGUINTE-'].update(disabled=not leitura, visible=leitura)
                    window['-ULTIMO-'].update(disabled=not leitura, visible=leitura)
                    window['-EDITAR-'].update(disabled=not leitura, visible=leitura)
                    window['-NOVO-'].update(disabled=not leitura, visible=leitura)
                    window['-APAGAR-'].update(disabled=not leitura, visible=leitura)
                    window['-GRAVAR-'].update(disabled=leitura, visible=not leitura)
                    window['-CANCELAR-'].update(disabled=leitura, visible=not leitura)
                    pessoa = {}
                    pessoa['nome']=values['v_nome']
                    pessoa['idade']=int(values['v_idade'])
                    if values['v_BI']:
                        pessoa['BI']=values['v_documento']
                    else:
                        pessoa['CC']=values['v_documento']
                    pessoa['morada']={}
                    pessoa['morada']['cidade']=values['v_cidade']
                    pessoa['morada']['distrito']=values['v_distrito']
                    pessoa['sexo']=values['v_sexo']
                    pessoa['religiao']=values['v_religiao']
                    pessoa['marca_carro']=values['v_carro']
                    pessoa['profissao']=values['v_profissao']
                    pessoa['partido_politico']={}
                    pessoa['partido_politico']['party_abbr']=values['v_partido_abreviatura']
                    pessoa['partido_politico']['party_name']=values['v_partido_nome']
                    pessoa['descrição']=values['v_descricao']
                    pessoa['desportos']=window['v_desportos'].Values
                    pessoa['animais']=window['v_animais'].Values
                    pessoa['figura_publica_pt']=window['v_figuras'].Values
                    pessoa['destinos_favoritos']=window['v_destinos'].Values
                    pessoa['atributos']={}
                    pessoa['atributos']['fumador']=values['v_fumador']
                    pessoa['atributos']['gosta_cinema']=values['v_cinema']
                    pessoa['atributos']['gosta_viajar']=values['v_viajar']
                    pessoa['atributos']['acorda_cedo']=values['v_acorda']
                    pessoa['atributos']['gosta_ler']=values['v_ler']
                    pessoa['atributos']['gosta_musica']=values['v_musica']
                    pessoa['atributos']['gosta_comer']=values['v_comer']
                    pessoa['atributos']['gosta_animais_estimacao']=values['v_animais_est']
                    pessoa['atributos']['gosta_dancar']=values['v_dançar']
                    pessoa['atributos']['comida_favorita']=values['v_comida']
                    if alteracao:
                        pessoas[indice]=pessoa
                    else:
                        pessoas.append(pessoa)
            case _:
                pass

        if ((event != '-DESPORTOS-') and (event != '-ANIMAIS-') and (event != '-FIGURAS-') and (event != '-DESTINOS-') and (event != 'v_idade') and 
            (event != 'Remover Desporto') and (event != 'Remover Animal') and (event != 'Remover Figura') and (event != 'Remover Destino')) and not dados_invalidos:
            print('«««««««««««   VAI ATUALIZAR  »»»»»»»»»»»»»» ', event,' «««')
            window['v_nome'].update(pessoa['nome'], disabled=leitura)
            window['v_idade'].update(pessoa['idade'], disabled=leitura)
            documento = 'BI' if 'BI' in pessoa else 'CC'
            tipo_doc = True if documento == 'BI' else False
            window['v_BI'].update(value=tipo_doc, disabled=leitura)
            window['v_CC'].update(value=not tipo_doc, disabled=leitura)
            window['v_documento'].update(pessoa[documento], disabled=leitura)
            window['v_cidade'].update(pessoa['morada']['cidade'], disabled=leitura)
            window['v_sexo'].update(pessoa['sexo'], disabled=leitura)
            window['v_religiao'].update(pessoa['religiao'], disabled=leitura)
            window['v_distrito'].update(pessoa['morada']['distrito'], disabled=leitura)
            window['v_carro'].update(pessoa['marca_carro'], disabled=leitura)
            window['v_profissao'].update(pessoa['profissao'], disabled=leitura)
            window['v_partido_abreviatura'].update(pessoa['partido_politico']['party_abbr'], disabled=leitura)
            window['v_partido_nome'].update(pessoa['partido_politico']['party_name'], disabled=leitura)
            window['v_descricao'].update(pessoa['descrição'], disabled=leitura)
            window['v_desportos'].update(pessoa['desportos'])
            window['v_animais'].update(pessoa['animais'])
            window['v_figuras'].update(pessoa['figura_publica_pt'])
            window['v_destinos'].update(pessoa['destinos_favoritos'])
            window['v_fumador'].update(pessoa['atributos']['fumador'], disabled=leitura)
            window['v_cinema'].update(pessoa['atributos']['gosta_cinema'], disabled=leitura)
            window['v_viajar'].update(pessoa['atributos']['gosta_viajar'], disabled=leitura)
            window['v_acorda'].update(pessoa['atributos']['acorda_cedo'], disabled=leitura)
            window['v_ler'].update(pessoa['atributos']['gosta_ler'], disabled=leitura)
            window['v_musica'].update(pessoa['atributos']['gosta_musica'], disabled=leitura)
            window['v_comer'].update(pessoa['atributos']['gosta_comer'], disabled=leitura)
            window['v_animais_est'].update(pessoa['atributos']['gosta_animais_estimacao'], disabled=leitura)
            window['v_dançar'].update(pessoa['atributos']['gosta_dancar'], disabled=leitura)
            window['v_comida'].update(pessoa['atributos']['comida_favorita'], disabled=leitura)
            window['vl_desportos'].update('', disabled=leitura)
            window['-DESPORTOS-'].update(disabled=leitura)
            window['vl_animais'].update('', disabled=leitura)
            window['-ANIMAIS-'].update(disabled=leitura)
            window['vl_figura_publica_pt'].update('', disabled=leitura)
            window['-FIGURAS-'].update(disabled=leitura)
            window['vl_destinos_favoritos'].update('', disabled=leitura)
            window['-DESTINOS-'].update(disabled=leitura)
            if event!='-NOVO-':
                window['-RODAPE-'].update(' Nº do registo: ' + str(indice+1) + '    :: Total de '+ str(len(pessoas)) + ' registos.')

        window.refresh()
    window.close()