import csv
import os
import matplotlib.pyplot as plt
from alunos import *

opcao = "1"
os.system("cls")
alunos = read_dataset ("alunos.csv")
while opcao != "0":
    menu()
    opcao = input ("    Introduza uma opção: ")
    if opcao == "1":
        tabela_alunos(alunos)
    elif opcao == "2":
        tabelar_distribibuicao(distribuicao(alunos, 2), "CURSO")
    elif opcao == "3":
        media_tpc(alunos)
        tabela_alunos(alunos)
    #Porque é que o escalao dá sem criar a nova lista? A lista guarda automaticamente sem fazer alunos=media_tpc(alunos)
    elif opcao == "4":
        if tamanho_linha_lista(alunos)==7:
            print("\n      [ ERRO: Antes de Criar Distribuição por Médias é necessário Criar a MÉDIA. ]")
        else:
            tabelar_distribibuicao(distribuicao(alunos, 7), "MÉDIAS")
    elif opcao == "5":
        if tamanho_linha_lista(alunos)==8:
            escalao_notas(alunos)
            tabela_alunos(alunos)
        elif tamanho_linha_lista(alunos)==7:
            print ("\n    [ ERRO: Antes de Criar ESCALÃO é necessário Criar a MÉDIA. ]")
        elif tamanho_linha_lista(alunos)==9:
            print ("\n    [ ATENÇÃO: o coluna ESCALÃO já está criada. ]")
    elif opcao == "6":
        if tamanho_linha_lista(alunos)==9:
            tabelar_distribibuicao(distribuicao(alunos, 8), "ESCALÃO")
        else:
            print ("\n    [ ATENÇÃO: Ainda não está criada a coluna «ESCALÃO». ]")
    elif opcao == "7":
        distrib= input("\n      Que distribuição quer ver representada? (C)urso, (E)scalão:, (M)édias  ")
        if distrib== "c" or distrib=="C":
            print (" \n            Distribuição por CURSO   ")
            graficos(distribuicao(alunos, 2))
        elif distrib== "e" or distrib=="E":
            if tamanho_linha_lista(alunos)<7:
                print("\n      [ ERRO: Antes de pedir GRÁFICO é necessário Criar a DISTRIBUIÇÃO POR ESCALÃO. ]")
            else:
                print (" \n            Distribuição por ESCALÃO   ")
                graficos(distribuicao(alunos,8))
        elif distrib== "m" or distrib=="M":
            if tamanho_linha_lista(alunos)<7:
                print("\n      [ ERRO: Antes de pedir GRÁFICO é necessário Criar a DISTRIBUIÇÃO POR MÉDIAS. ]")
            print (" \n            Distribuição por MÉDIAS  ")
            graficos(distribuicao(alunos,7))
        else:
           print ("\n    [ ERRO: Comando não aceite, tente novamente. ]") 
    elif opcao== "8":
        grava_lista_ficheiro(alunos)
    elif opcao== "0":
        break
    else:
        print ("\n    [ ERRO: Comando não aceite, tente novamente. ]")
    input("\n    [ Tecla «ENTER» para continuar... ]")
    os.system("cls")
