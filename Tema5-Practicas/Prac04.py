import random
letras = list ('abcdefghijklmnopqrstuvwxyz')
vocales = 'aeiou'
""" for i in range(len(letras)):
    print(letras[i],end=' ') """
for i in letras:
    print(i,end=' ')

l1=letras[:8]
l2=letras[8:16]
l3=letras[16:]

random.shuffle(l1)
random.shuffle(l2)
random.shuffle(l3)

""" print ('',join(letras)) """

for a,b,c in zip(l1,l2,l3):
    print(a+b+c,end=' ')

for i, letra in enumerate(letras):
    if letra in vocales:
        print('{} en la posicion {}'.format(letra, i))

zen='''\
    Bello es mejor que feo.
    Explicito es mejor que implicito.
    Simple es mejor que complejo.
    Complejo es mejor que complicado.'''
fich=open('short.zen.txt','w')
fich.writelines(zen) # Escribe el fichero
fich.close()         # Cierra el fichero

""" fich=open('short.zen.txt','r')
fich.readline()
fich.readline()
fich.readline()
fich.readline()
fich.readline()
fich.close """

""" fich=open('short.zen.txt','r')
fich.__next__()
fich.__next__()
fich.__next__()
fich.__next__()
fich.__next__() """

fich=open('short.zen.txt','r')
next(fich)
next(fich)
next(fich)
next(fich)

l4=iter(letras)
next(l4)
next(l4)
next(l4)



class Repetidor():

    def __init__(self, veces, item):
        self.veces=veces
        self.item=item
        self.counter=0
    
    def __next__(self):
        if self.counter == self.veces:
            raise StopIteration('Iterador comsumido')
        self.counter += 1
        return self.item
    
    def __iter__(self):
        return self

for r in Repetidor(3, 'Python!'):
    print(r, end=' ')