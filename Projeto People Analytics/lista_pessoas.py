import PySimpleGUI as sg
from operator import itemgetter
from gestao_pessoas import *

def lista_pessoas(pessoas):
    sg.theme('LightBlue2')
    tabela = []
    lista_religioes = []
    lista_animais = ['-Todos-']
    tabela_cabeçalhos = ['Nome', 'Idade', 'BI/CC', 'Cidade', 'Religião', 'Profissão', 'Animais']
    tamanho_colunas = [30, 5, 15, 20, 20, 30, 30] 
    for pessoa in pessoas:
        documento = 'BI' if 'BI' in pessoa else 'CC'
        tabela.append([pessoa['nome'], pessoa['idade'], documento+"-"+pessoa[documento], pessoa['morada']['cidade'], pessoa['religiao'], pessoa['profissao'], pessoa['animais']])
        if pessoa['religiao'] not in lista_religioes:
            lista_religioes.append(pessoa['religiao'])
        for animal in pessoa['animais']:
            if animal not in lista_animais:
                lista_animais.append(animal)
    lista_animais.sort()   
    lista_religioes.sort()

    col1=[[sg.Text(text='Nome', pad=((5,0),(0,5)), size=(10,1), justification='right'),sg.Input('', size=(20,1), pad=((5,0),(0,5)), key='v_pesquisa_nome')],
          [sg.Text(text='BI/CC', pad=((5,0),(0,10)),size=(10,1), justification='right'),sg.Input('', size=(20,1), pad=((5,0),(0,10)), key='v_pesquisa_bi_cc')]]
    col2=[[sg.Text(text='Religião', pad=((5,0),(0,5)), size=(10,1), justification='right'),sg.Combo(lista_religioes, size=(30,1), pad=((5,0),(0,5)), key='v_pesquisa_religiao')],
          [sg.Text(text='Animal', pad=((5,0),(0,10)), size=(10,1), justification='right'),sg.Combo(lista_animais, size=(30,1), pad=((5,0),(0,10)), default_value='-Todos-', readonly=True, key='v_pesquisa_animal')]]
    col3=[[sg.Button('PESQUISAR', size=(15,2), pad=((2,0),(0,10)), key='-PESQUISA-')]]

    layout = [[sg.Text(text='Listagem de Pessoas',size=(20, 1), font=('Arial', 20), justification='left')],
              [sg.HorizontalSeparator(pad=((5,5),(7,7)))],
              [sg.Column(col1, element_justification='left'), sg.Column(col2, element_justification='left'), sg.Column(col3, element_justification='center')],
              [sg.Table(values=tabela,
                        headings=tabela_cabeçalhos,
                        max_col_width=35,
                        #display_row_numbers=True,
                        col_widths=tamanho_colunas,
                        auto_size_columns=False,
                        justification='left',
                        vertical_scroll_only=False,
                        #enable_events=True,
                        enable_click_events=True,
                        num_rows=28,
                       key='-TABELA-')]]

    window =sg.Window('UM - Projeto People Analytics', layout, size=(900,600), modal=True, finalize=True)
    # Add the ability to double-click a cell
    window['-TABELA-'].bind('<Double-Button-1>', 'Double')
    while True:
        event, values = window.read()
        print("\neventX ----->", event, " ValuesX ----->", values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == '-TABELA-Double':            
            if len(values['-TABELA-']) != 0:                # se duplo clic nos cabeçalhos, não vai mostrar Ficha! 
                linha_clickada = values['-TABELA-'][0]
                doc_tipo = tabela[linha_clickada][2][0:2]   # doc_tipo = 'BI' ou 'CC'
                doc_num = tabela[linha_clickada][2][3:]     # doc_num  = nº do Documento
                for indice, pessoa in enumerate(pessoas):
                    if doc_tipo in pessoa:
                        if pessoa[doc_tipo] == doc_num:
                            window.close()
                            return (pessoas, indice)

        if event == '-PESQUISA-':
            tabela = []
            for pessoa in pessoas:
                documento = 'BI' if 'BI' in pessoa else 'CC'
                filtro_animais = True if (values['v_pesquisa_animal'] == '-Todos-' or values['v_pesquisa_animal'] in pessoa['animais']) else False
                                
                if values['v_pesquisa_nome'] in pessoa['nome'] and values['v_pesquisa_bi_cc'] in pessoa[documento] and values['v_pesquisa_religiao'] in pessoa['religiao'] and filtro_animais:
                    tabela.append([pessoa['nome'], pessoa['idade'], documento+"-"+pessoa[documento], pessoa['morada']['cidade'], pessoa['religiao'], pessoa['profissao'], pessoa['animais']])            
            window['-TABELA-'].update(tabela)

        if isinstance(event, tuple):   
            # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
            # You can also call Table.get_last_clicked_position to get the cell clicked
            if event[0] == '-TABELA-':
                if event[2][0] == -1:    # click na linha dos cabeçalhos
                    coluna_clickada = event[2][1]
                    tabela=sorted(tabela, key=itemgetter(coluna_clickada))
                    window['-TABELA-'].update(tabela)
        window.refresh()
    window.close
    return (pessoas, None)

# fonte de inspiração :)    
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Table_Element_Header_or_Cell_Clicks.py

