import operator
import numpy as np

libros=["Analisis de Algoritmos.txt",
    "Artificial Intelligence A Modern Approach.txt",
    "Introduction to algorithms.txt",
    "Introduction to the Design and Analysis of Algorithms.txt",
    "Introduction To The Theory Of Computation.txt",
    "Pattern Recognition and Machine Learning .txt",
    "Probability and Computing Randomization and Probabilistic Techniques in Algorithms and Data Analysis.txt",
    "PROLOG.txt",
    "Remote Sensing Digital Image Analysis.txt",
    "Theory of Computation.txt"]
contlibros=[0,0,0,0,0,0,0,0,0,0]

def construyeg(b): # construye un diccionario para representar la función g
    d={}
    for i in range(0,len(b)-1): # ignoramos el último caracter
        d[b[i]]=i
    return d

def bmh(a,b): # busca b dentro de a, retorna None (fracaso) o posición del calce
    g=construyeg(b) # Uso: g(c)=g.get(c,-1) para rellenar con -1 los valores faltantes
    n=len(a)
    m=len(b)
    k=m-1
    j=m-1
    while k<n:
        if j<0:
            return k-m+1
        if a[k-(m-1-j)]==b[j]:
            j=j-1
        else:
            k=k+(m-1-g.get(a[k],-1))
            j=m-1
    return None


#BUSQUEDA DE PALABRA EN ARCHIVO ESPECIFICO
palabra=input('Ingrese la palabra que desea buscar:')
texto=input("Ingrese el nombre del archivo de texto donde se buscara:")
cont=0
nlinea=0
with open(texto) as archivo:
    for linea in archivo:
        nlinea=nlinea+1
        busqueda=bmh(linea,palabra)
        if busqueda != None:
            print("La palabra se encuentra en la linea:",nlinea)
            print("La palabra se encuentra en el caracter:",busqueda)
            cont=cont+1

print("El numero de veces que se encontro la palabra es:")
print(cont)

#BUSQUEDA DE PALABRA EN TODA LA CARPETA Y ORDENAMIENTO
palabra=input('Ingrese lo que desea buscar:')
palabras=palabra.split()
largo=len(palabras)

#si es una sola palabra
if largo==1:
    for i in range(10):
        cont=0
        nlinea=0
        libro=libros[i]
        with open(libro) as archivo:
            for linea in archivo:
                nlinea=nlinea+1
                busqueda=bmh(linea,palabra)
                if busqueda != None:
                    cont=cont+1

        contlibros[i]=cont #se puede dividir entre nlinea para obtener la relacion de palabra/renglones

    dic=dict(zip(libros,contlibros))

    ord=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    for i in ord:
        print(i)

#si tiene mas de una palabra
if largo > 1:
    for i in range(10):

        cont=0
        nlinea=0
        libro=libros[i]
        with open(libro) as archivo:
            for linea in archivo:
                nlinea=nlinea+1
                busqueda=bmh(linea,palabra)
                if busqueda != None:
                    cont=cont+1
                for j in range(largo):
                    palabrasola=palabras[j]
                    busqueda=bmh(linea,palabrasola)
                    if busqueda != None:
                        cont=cont+1
        contlibros[i]=cont #se puede dividir entre nlinea para obtener la relacion de palabra/renglones

    dic=dict(zip(libros,contlibros))

    ord=(sorted(dic.items(),key=operator.itemgetter(1),reverse=True))
    for i in ord:
        print(i)