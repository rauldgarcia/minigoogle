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

palabra=input('Ingrese la palabra que desea buscar:')
print(palabra)

cont=0
nlinea=0
with open("Analisis de Algoritmos.txt") as archivo:
    for linea in archivo:
        nlinea=nlinea+1
        busqueda=bmh(linea,palabra)
        if busqueda != None:
            print("La palabra se encuentra en la linea:",nlinea)
            print("La palabra se encuentra en el caracter:",busqueda)
            cont=cont+1

print("Se encontro la palabra:")
print(cont)