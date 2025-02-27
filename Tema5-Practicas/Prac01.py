def suma(a, b):
    return a+b

x = "El valor de (a+b)*c es"
a, b, c = 4, 3, 2
print('Valores:',a,b,c,sep=' ')
print('Suma a+b: ',suma (a,b))
print('Suma 2.7+4.0: ',suma(2.7, 4.0))
print('Suma palabras: ',suma('Me gusta', 'Python'))
imprimir = True
if imprimir:
 print("La suma es:", suma(a,b))

def calculo(a, b, c):
    return (a+b)*c

print(x,calculo (a,b,c))

def maxmin(lista): 
    return max(lista), min(lista)   # Devielveuna tupla de 2 elementos 

l = [1, 3, 5, 6, 0] 
maximo, minimo = maxmin(l)        
# Desempaqueta la tupla en 2 variables 
print('Rango: ',l)
print('Maximo:',minimo, 'Minimo: ',maximo)

def factorial(x): 
    if x>1: 
        return x*factorial(x-1) 
    else: 
        return 1

print('Factorial de 5 es: ',factorial(5))

def nueva(l): 
    l[0] = 1000     # Modificamos la lista en el interior 
    return min(l) 
 
l = [1, 2, 3] 
print(nueva(l[:])) # minimo modifica la lista aquí 
print(l)

def linealog(*a,b='LOG',c='-'):
    print(b,a,sep=c)

args = {'a':20, 'b':10, 'c':30, 'd':40} 
linealog(args,b='NEW',c=':')
