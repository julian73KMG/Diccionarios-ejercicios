##-- Problema 1 --
# Desarrollar un algoritmo que imprima de manera ascendente los valores (todos del mismo tipo) de un diccionario


def dicAscendente(dic,o):
    # se vuelve lista el diccionario
    dic_list = list(dic.items())
    dic_list.sort() #Se ordena la lista
    dic = dict(dic_list) #lo volvemos a diccionario  
    if o == 'k' or o == 'K':
         R = list(dic.keys()) #Se imprime como una lista las keys
    elif o == 'v' or o == 'V':
         R = list(dic.values())  #Se imprime como una lista los values
    else:
        return "Letra incorrecta, solo 'k' o 'v'" #Retorna un error de typeo
    
    return R

##-- Problema 2 --
# Desarrollar un algoritmo que verifique si todas las 'clave:valor' de un diccionario se encuentran en otro diccionario

def dicRepetido(dic1,dic2):
     #Analiza si alguno de los dos es subconjunto del otro o es el mismo diccionario
     if dic1.items() <= dic2.items() or dic2.items() <= dic1.items():
          return True    #Retorna True su hay algun subdiccionario o son iguales
     else:
          return False   #Retorna False de lo contrario

##-- Problema 3 --
# Desarrollar una funcion que reciba dos diccionarios como parametros y los mezcle, es decir, que se construya un nuevo diccionario
# con las llaves de los dos diccionarios; si hay una clave repetida en ambos diccionarios, se debe asignar el valor que tenga la clave en el primer diccionario.

def dicMezclado(dic1,dic2):
     #Se inicia el nuevo diccionario con los elementos del primer diccionario
     dicM = dic1.copy()
     #Añadir los elementos del segundo diccionario
     for k,v in dic2.items():
          #Si la key no esta en el diccionario mezclado, se agrega
          if k not in dicM:
               dicM[k] = v
     return dicM



##-- Problema 4 --
# Desarrollar un programa que dada una lista de personas, cada persona representada como el siguiente ejemplo:
# {"nombres":"Pedro Julio", "apellidos":"Tristan Merchan", "edad":101},
# imprima los nombres y apellidos de las personas que estan en un rango de edades.


def dicEdades(p,min,max):
     #Se inicializa un diccionario vacío para guardar los nombres y apellidos
     dicRango = {}
     for v in p:    #Recorrer la lista
          edad = v.get("edad",'No encontrado')    #Metodo get para buscar todas las edades
          if edad != 'No encontrado' and min <= edad <= max:     #Si se encuentra el value y está en el rango
              n = f"{v['nombres']} {v['apellidos']}"   #guarda value en 'nombre' y 'apellido'
              dicRango[n] = True   #Se guarda cada nombre y apellido con un True

     return dicRango #Retorna el diccionario, si no hay personas en el rango saldrá vacío

dicVacio = {}

puertos = {22:"SSH", 80:"HTTP", 23:"Telnet",  3306:"MySQL", 1:"NET"}
puertos1 = {22:"SSH", 23:"Telnet",  3306:"MySQL", 80:"HTTP"}

dicMez1 = {1: "a", 2: "b", 3: "c"}
dicMez2 = {3: "d", 4: "e", 5: "f"}

dicRep1 = {22: "veintidos", 443: "cuatrocuatrotres", 1:"uno"}
dicRep2 = {22: "veintidos", 443: "cuatrocuatrotres"}

personas = [
    {"nombres": "Pedro Julio", "apellidos": "Tristán Merchán", "edad": 101},
    {"nombres": "Ana María", "apellidos": "González Pérez", "edad": 45},
    {"nombres": "Juan Carlos", "apellidos": "Martínez López", "edad": 30},
    {"nombres": "Lucía Fernanda", "apellidos": "Rodríguez Díaz", "edad": 25},
]

print(dicAscendente(puertos1,'h'))
print(dicRepetido(dicMez1,dicMez2))
print(dicMezclado(dicRep1,dicRep2))
print(dicEdades(personas,50,30))