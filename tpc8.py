

#1a

def inicDiferente(s1, s2):
    # se uma das Strings for vazia, o resultado é 0
    if len(s1)==0: 
        return 0
    if len(s2)==0:
        return len(s1)
    res = 0
    i = 0
    encontrou = False
    while not encontrou and i<=len(s1):
        if s1[i] in s2:
            encontrou=True
        else:
            res += 1
        i += 1
    return res


#1b

def acimaMedia(n):
    res = 0
    i= 1
    soma= 0
    numeros= []
    while i<=n:
        numero= int(input("Introduza o número"))
        numeros.append(numero)
        i+= 1
    for num in numeros:
        soma += num
    res= soma / n
    return res


#1c

def merge(l1, l2):
    res= []
    i1 = 0  
    i2 = 0   
    while i1<len(l1) and i2<len(l2):
        if l1[i1]<=l2[i2]:
            res.append(l1[i1])
            i1 += 1
        else:
            res.append(l2[i2])
            i2 += 1
    if i1>=len(l1):
        res = res + l2[i2:] 
    if i2>=len(l2):
        res = res + l1[i1:] 
    return res


#1d

def figuais(f1, f2):
    i=0
    aux=0
    res= True
    texto1_aux = open (f1, encoding='utf-8')
    texto2_aux = open (f2, encoding='utf-8')
    texto1= []
    texto2 = []
    for linha in texto1_aux:
        texto1.append(linha)
    for linha2 in texto2_aux:
        texto2.append(linha2)
    while aux < len(texto1):
        if texto1[i] != texto2[i]:
            res= False
        aux += 1
    return res


#EXERCICCIO 2

#2a

def atores(cinemateca):
    atores= []
    for _,_, elenco, _ in cinemateca:
        #_,_, elenco, _= filme
        for ator in elenco:
            if ator not in atores:
                atores.append(ator)
    atores.sort()
    return atores


#2b

def listarPorGenero(cinemateca, genero):
    filmes= []
    for titulo,_, _,gen in cinemateca:
        if genero in gen:
            filmes.append(titulo)
    filmes.sort()    
    return filmes


#2c

def maiorElenco( cinemateca ):
    maior= len(cinemateca[0][3])
    for titulo,_, elenco, _ in cinemateca:
        if len(elenco) >= maior:
            maior= len(elenco)
            filme= titulo   
    return filme 


#2d

def filmePorGenero( cinemateca ):
    distrib= {}
    for _,_,_, generos in cinemateca:
        for genero in generos:
            if genero in distrib.keys():
                distrib[genero] += 1
            else:
                distrib[genero]= 1
    return distrib


#2e

import matplotlib.pyplot as plt

def graficos (distrib):
    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range (0, len(distrib.keys()))], distrib.keys(), rotation=75)
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9, wspace=0, hspace=0)
    plt.title("Distrbuição dos Filmes por Género")
    plt.show()
