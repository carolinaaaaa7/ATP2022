import csv
import os
import matplotlib.pyplot as plt

def read_dataset (fnome):
    f= open(fnome,encoding='utf-8')
    f.readline()
    csv_reader = csv.reader (f, delimiter=';')
    obras = []
    for row in csv_reader:
        obras.append(tuple(row))
    f.close()
    print ("\n    [ Ficheiro RECUPERADO com sucesso. Total de OBRAS =",len(obras),"]" )
    return obras

#Print
def tabela_obras (lista):
    linha = 1
    print_cabeçalho = True
    for nome,_,ano , periodo, compositor, duracao, id in lista:
        if print_cabeçalho:
            os.system("cls")
            print("""
    -------------------------------------------------------------------------------------------------------------------
    |                                                  LISTAGEM DE OBRAS                                              |
    -------------------------------------------------------------------------------------------------------------------
    |      Nome                                Compositor                    Período            Ano       Duração     |
    -------------------------------------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print (f"        {nome[:30]:30}    {compositor[:30]:30}    {periodo:15}    {ano:6}    {duracao:10}")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla (p) para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p" or opcao=="P":
                return
            print_cabeçalho = True
        linha = linha + 1


#lista de tuplos (titulo, ano) 
def ordena_tuple(t):
    return t[0]

def ordena_indice (lista, indice):
    #ordena por indice da lista
    res = []
    for nome,_,ano, *_ in lista:
        if indice== 0:
            res.append ((nome, ano))
        elif indice==2:
            res.append ((ano, nome))
    res.sort(key = ordena_tuple)
    return res

def imprimir_por_ano (lista):
    linha = 1
    print_cabeçalho = True
    for ano, nome in lista:
        if print_cabeçalho:
            os.system("cls")
            print ("""
    --------------------------------------------------------------------------------------
    |                           LISTAGEM DE OBRAS                                        |
    --------------------------------------------------------------------------------------
    |     Ano                                   Título                                   |
    --------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print (f"       [ {ano:4} ]       [ {nome[:60]:60} ]")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1 

def imprimir_por_titulo (lista):
    linha = 1
    print_cabeçalho = True
    for nome, ano in lista:
        if print_cabeçalho:
            os.system("cls")
            print ("""
    --------------------------------------------------------------------------------------
    |                           LISTAGEM DE OBRAS                                        |
    --------------------------------------------------------------------------------------
    |     Título                                                               Ano       |
    --------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print (f"       [ {nome[:60]:60} ]     [ {ano:4} ]")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1  



###
def titulo_por_ano (lista):
    res = {}
    for nome,_,ano, *_ in lista:
        if ano in res.keys():
            res[ano].append(nome)
        else:
            res[ano] = [nome]
    res= dict(sorted (res.items()))
    return res


####
def compositores (lista):
    res = []
    for _,_,_,_, compositor,_,_ in lista:
        if compositor not in res:
            res.append(compositor)
    res.sort()
    return res



def distribuicao (lista, indice, amplitude):
    #se amplitude= 0 nao tem min nem max, ou seja, sem intervalo
    d={}
    for obra in lista:
        if amplitude != 0:
            min = (int(obra[indice])//amplitude) * amplitude
            max = min + amplitude -1
            intervalo = "[" + str(min)+ "-" + str(max) + "]"
        else:
            intervalo = "[ " + str(obra[indice]) + " ]"
        if intervalo in d:
            d[intervalo] += 1
        else:
            d[intervalo] = 1
    d= dict(sorted(d.items()))
    return d




def tabelar_distrib (dicionario, titulo):
    linha = 1
    print_cabeçalho = True
    for distribuicao, quantidade in dicionario.items():
        if print_cabeçalho:
            os.system("cls")
            print("    -----------------------------------------------------------------")
            print("    |                DISTRIBUIÇÃO DAS OBRAS POR " +str(titulo.ljust(20," "))+"|")
            print("    -----------------------------------------------------------------")
            print("    |        " + str(titulo.ljust(30," ")) + "    Número de obras      |")
            print("    -----------------------------------------------------------------")
            print_cabeçalho = False
        print (f"         {distribuicao:<40}      {str(quantidade)[0]:<4}    "    )
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1  



def tabelar_obras_anos (dicionario):
    linha = 1
    print_cabeçalho = True
    for ano, nomes in dicionario.items():
        #ano = "[ " + str(ano) +" ]"
        if print_cabeçalho:
            os.system("cls")
            print ("""
    --------------------------------------------------------------------------------------
    |                           LISTAGEM de OBRAS por ANO                                |
    --------------------------------------------------------------------------------------
    |     Ano                           Obras                                            |
    --------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print(f"       [ {ano:4} ]     {str(nomes)[:80]:80}")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p" or opcao=="P":
                return
            print_cabeçalho = True
        linha = linha + 1  


def tabelar_compositores (lista):
    linha = 1
    print_cabeçalho = True
    for compositor in lista:
        if print_cabeçalho:
            os.system("cls")
            print ("""
    --------------------------------------------------------------------------------------
    |                           LISTAGEM de COMPOSITORES                                 |
    --------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print ( "            " +str(compositor))
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1  


def graficos (distrib):
    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range (0, len(distrib.keys()))], distrib.keys(), rotation=75)
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9, wspace=0, hspace=0)
    plt.show()


def inver (lista):
    res= []
    for nome, _, _, _, compositores, *_ in lista:
        if compositores in res():
            res[compositores].append( nome)
        else:
            res[compositores] = [nome]
    res= sorted (res)
    return res
    
def inversao_estrutural (lista):
    res = {}
    for nome, _, _, _, compositores, *_ in lista:
        if compositores in res.keys():
            res[compositores].append(nome)
        else:
            res[compositores] = [nome]
    res = sorted (res.items())
    return res

def imprimir_inversão (lista):
    linha = 1
    print_cabeçalho = True
    for compositor, obras in lista:
        if print_cabeçalho:
            os.system("cls")
            print ("""
    ----------------------------------------------------------------------------------------------------------------------------------------------------
    |                                      LISTAGEM de OBRAS por COMPOSITOR                                                                            |
    |--------------------------------------------------------------------------------------------------------------------------------------------------|
    |     Compositor                      Obra1                       Obra2                       Obra3                       Obra4                    |
    ----------------------------------------------------------------------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        print(f"      {compositor[:30]:30} ",end='')
        for i in range(len(obras)):
            print(f" |{obras[i][:25]:<25} ", end ='')
        print("")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1 