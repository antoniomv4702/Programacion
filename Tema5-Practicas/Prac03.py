import pickle
from pathlib import Path

mydic=dict()

#file_name=input("Digite nombre archivo datos: ")
file_name="lista-dni.pkl"

path= Path(file_name)
if path.is_file():
    input_file=open(file_name,'rb')
    mydic=pickle.load(input_file)
    input_file.close()
else:
    print("Fichero no existe, creamos nuevo")
salir="N"
while salir != "S":
    dni=input("Digite DNI: ")
    if dni in mydic:
        print("La edad de "+dni+" es "+str(mydic[dni])+" años")
    else:
        edad=input("El dni no existe, añade su edad: ")
        if edad.isnumeric():
            mydic[dni]=int(edad)
        print("Añadido nuevo dni : "+dni+" con edad: "+edad)

    listar=input("Quieres listarlo(S/N)? ")
    if listar == 'S':
        for elem,valor in mydic.items():
            print('Dni: {} Edad: {}'.format(elem,valor))

    """         for elem in mydic:
            print('Dni: {} Edad: {}'.format(elem,mydic[elem]))
    """    
    salir=input("Quieres salir(S/N)? ")

output_file=open(file_name,'wb')
pickle.dump(mydic, output_file)
output_file.close()