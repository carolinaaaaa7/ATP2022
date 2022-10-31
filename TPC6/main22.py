
import os 
import matplotlib.pyplot as plt
from obras22 import *
#compositores, distrib_ano, distrib_compositor, distrib_periodo, graficos, imprimir_por_ano, imprimir_por_titulo, numero_obras, ordem_ano, ordem_titulo, read_dataset, tabela_obras, tabelar_compositores, tabelar_distrib, tabelar_obras_anos, titulo_por_ano 


def menu():
    print ("""
    -------------------------------------
    |    Menu Principal                 |
    -------------------------------------
    (1) Obras Catalogadas
    (2) Obras Ordenadas por Título/ Ano
    (3) Obras Associadas a Cada Ano
    (4) Compositores
    (5) Distribuição por Ano
    (6) Distribuição por Período
    (7) Distribuição por Compositor
    (8) Gráficos das distribuções
    (9) Inversão Estrutural
    (0) Sair
    -------------------------------------
    """)


opcao = "1"
os.system("cls")
obras = read_dataset ("obras.csv")
while opcao != "0":
    menu()
    opcao = input ("    Introduza uma opção: ")
    if opcao == "1":
        tabela_obras(obras)
    elif opcao == "2":
        ordem = input ("\n      Que ordenação quer ver representada? (A)no, (T)ítulo:  ")
        if ordem=="a" or ordem=="A":
            imprimir_por_ano(ordena_indice(obras,2))
        elif ordem=="t" or ordem=="T":
            imprimir_por_titulo(ordena_indice(obras,0))
        else:
            print ("\n    [ ERRO: Comando não aceite, tente novamente. ]")
    elif opcao == "3":
        tabelar_obras_anos(titulo_por_ano(obras))
    elif opcao == "4":
        tabelar_compositores(compositores(obras))
    elif opcao == "5":
        tabelar_distrib(distribuicao(obras, 2, 25), "ANO")
    elif opcao == "6":
        tabelar_distrib(distribuicao(obras,3,0), "PERÍODO")
    elif opcao == "7":
        tabelar_distrib(distribuicao(obras,4,0), "COMPOSITOR")
    elif opcao == "8":
        tipo= input("\n      Que distribuição quer ver representada? (C)ompositor, (A)no, (P)eríodo:  ")
        if tipo== "a" or tipo=="A":
            print (" \n            Distribuição por ANO   ")
            graficos(distribuicao(obras, 2, 25))
        elif tipo== "c" or tipo=="C":
            print (" \n            Distribuição por COMPOSITOR   ")
            graficos(distribuicao(obras, 4, 0))
        elif tipo== "p" or tipo=="P":
            print (" \n            Distribuição por PERÍODO   ")
            graficos(distribuicao(obras,3,0))
        else:
           print ("\n    [ ERRO: Comando não aceite, tente novamente. ]") 
    elif opcao== "9":
        imprimir_inversão(inversao_estrutural(obras))
    elif opcao== "0":
        break
    else:
        print ("\n    [ ERRO: Comando não aceite, tente novamente. ]")
    input("\n    [ Tecla «ENTER» para continuar... ]")
    os.system("cls")
