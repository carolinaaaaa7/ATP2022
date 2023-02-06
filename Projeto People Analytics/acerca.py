import PySimpleGUI as sg

def acerca_de():
      tam_letra = 12
      col1=[[sg.Text(text='Projeto :', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='Autores :', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='         ', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='         ', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='         ', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='Cadeira :', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')],
          [sg.Text(text='Ano        :', pad=((150,0),(0,10)), size=(8,1), font=('Arial', tam_letra, 'bold'), justification='left')]]

      col2=[[sg.Text(text='People Analytics',  pad=((5,0),(0,10)), size=(20,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='Carolina Teixeira   A100470', pad=((5,0),(0,10)), size=(22,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='Joana Branco        A96532',      pad=((5,0),(0,10)), size=(22,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='João Veloso          A101395',      pad=((5,0),(0,10)), size=(22,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='            ',      pad=((5,0),(0,10)), size=(20,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='Algoritmos e Técnicas de Programação',            pad=((5,0),(0,10)), size=(40,1), font=('Arial', tam_letra), justification='left')],
          [sg.Text(text='2022 / 2023',       pad=((5,0),(0,10)), size=(20,1), font=('Arial', tam_letra), justification='left')]]
          


      layout = [[sg.Text(text='Ficha Técnica',size=(20, 1), font=('Arial', 20), justification='left')],
            [sg.HorizontalSeparator(pad=((5,5),(7,25)))],
            [sg.Column(col1, element_justification='left'), sg.Column(col2, element_justification='left')],
            [sg.Text(text= 'Universidade do Minho', pad=((150,0),(0,10)), size=(20,1), font=('Arial', tam_letra, 'bold'), justification='left')]]
      window =sg.Window('UM - Projeto People Analytics', layout, size=(900,600), modal=True, finalize=True)

      while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                  break