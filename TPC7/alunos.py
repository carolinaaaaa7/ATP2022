import csv
import os
import matplotlib.pyplot as plt



def read_dataset (fnome):
    f= open(fnome,encoding='utf-8')
    f.readline()
    csv_reader = csv.reader (f, delimiter=',')
    alunos = list(csv_reader)
    #for row in csv_reader:
     #   alunos.append(list(row))
    f.close()
    print ("\n    [ Ficheiro RECUPERADO com sucesso. Total de ALUNOS =",len(alunos),"]" )
    return alunos

#  [[id, nome, curso, tpc1, tpc2, tpc3, tpc4]]

    

def menu():
    print ("""
    -------------------------------------
    |    Menu Principal                 |
    -------------------------------------
    (1) Lista Total de Alunos
    (2) Distribuição por Curso
    (3) Criar coluna: MÉDIA 
    (4) Distribuição por Médias
    (5) Criar coluna: ESCALÃO
    (6) Distribuição por Escalão
    (7) Gráficos das distribuções
    (8) Gravar em ficheiro 
    (0) Sair
    -------------------------------------
    """)


def tabela_alunos (lista):
    # id, nome, curso, tp1, tp2, tp3, tp4, media, escalao
    linha_aux = 1
    media=""
    escalao=""
    print_cabeçalho = True
    for linha in lista:
        if print_cabeçalho:
            os.system("cls")
            print("""
    ---------------------------------------------------------------------------------------------------------
    |                                           LISTAGEM DE ALUNOS                                          |
    ---------------------------------------------------------------------------------------------------------
    |    ID       Nome                           Curso         TPC1  TPC2  TPC3  TPC4    Média      Escalão |
    ---------------------------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        if len(linha)>=8: 
            media=linha[7]
        if len(linha)==9: 
            escalao=linha[8]
        print (f"      {linha[0]:>5}    {linha[1]:30}    {linha[2]:10}   {linha[3]:>4}  {linha[4]:>4}  {linha[5]:>4}  {linha[6]:>4}    {media:>6}    {escalao:>10}")
        if linha_aux % 20 == 0:
            opcao = input("\n    [ Tecla (p) para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p" or opcao=="P":
                return
            print_cabeçalho = True
        linha_aux += 1

        
def distrib_curso (lista):
    distrib= {}
    for _,_, curso, _,_,_,_ in lista:
        if curso in distrib:
             distrib[curso] += 1
        else:
            distrib[curso]= 1
    return distrib


def graficos (distrib):
    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range (0, len(distrib.keys()))], distrib.keys(), rotation=75)
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9, wspace=0, hspace=0)
    plt.show()

#medias
def media_tpc (lista):
    #for _,_,_,tpc1, tpc2,tpc3,tpc4 in lista:
        #lista.append((int(tpc1)+int(tpc2)+ int(tpc3)+int(tpc4))% 4)
    for linha in lista:
        if len(linha)>=8:  # lista já tem coluna com a MÉDIA
            break
        else:
            linha.append ((int(linha[3])+int(linha[4])+int(linha[5])+int(linha[6]))/4)
    #return lista


#notas
def escalao_notas (lista): 
    for linha in lista:
        if linha[7]  >=16.5 and linha[7]<=20:   linha.append("A [17-20]")
        elif linha[7]>=12.5 and linha[7]<16.5:  linha.append("B [13-16]")
        elif linha[7]>= 8.5 and linha[7]<=12.5: linha.append("C [09-12]")
        elif linha[7]>= 4.5 and linha[7]<=8.5:  linha.append("D [05-08]")
        elif linha[7]>=   0 and linha[7]<=4.5:  linha.append("E [01-04]") 
    return lista

#distribuicao escalao
def distrib_escalao (lista):
    distrib = {}
    for _,_,_, _,_,_,_,_,escalao in lista:
        if escalao in distrib:
             distrib[escalao] += 1
        else:
            distrib[escalao]= 1
    return distrib

#distribuicoes juntas
def distribuicao (lista, indice):
    d={}
    for linha in lista:
        intervalo = "[ " + str(linha[indice]) + " ]"
        if intervalo in d:
            d[intervalo] += 1
        else:
            d[intervalo] = 1
    d= dict(sorted(d.items()))
    return d

#print distribuicoes
def tabelar_distribibuicao(dicionario, titulo):
    linha = 1
    print_cabeçalho = True
    for distribuicao, quantidade in dicionario.items():
        if print_cabeçalho:
            os.system("cls")
            print("    -----------------------------------------------------------------")
            print("    |               DISTRIBUIÇÃO de ALUNOS por " +str(titulo.ljust(20," "))+" |")
            print("    -----------------------------------------------------------------")
            print("    |        " + str(titulo.ljust(30," ")) + "    Número de Alunos     |")
            print("    -----------------------------------------------------------------")
            print_cabeçalho = False
        print (f"         {distribuicao:<40}      {str(quantidade):<4}    ")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1  


def tamanho_linha_lista(lista):
    for linha in lista:
            return len(linha)

def grava_lista_ficheiro(lista):
    cabeçalho=['id_aluno','nome','curso','tpc1','tpc2','tpc3','tpc4']
    if tamanho_linha_lista(lista)>=8:
        cabeçalho.append('media')
    if tamanho_linha_lista(lista)==9:
        cabeçalho.append('escalao')
    #ficheiro=input("Qual o nome do ficheiro a gravar?")
    ficheiro='alunos.csv'
    with open(ficheiro, 'w',encoding='utf-8') as f:
        writer=csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(cabeçalho)
        for linha in lista:
            writer.writerow(linha)