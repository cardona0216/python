#tipos de datos

# tipo srt(string) texto o cadena de caracteres

comillasSimples= 'este es un texto'
comillasDobles = "este es un texto"
comillasTriples = """este es un texto"""
comillasTriplesSimples = '''este es un texto'''

#int(integer) representa un numero entero
numero_entero = 2

#float(decimal)
numero_decimal = 3.14

#complex: representa un numero complejo( parte entera y parte imaginaria)
numero_complejo = 5 + 2j

#list[]: coleccion ordenada(cada elemento va a ir ordenado va a tener un indice) y mutable de elementos

lista = [0,1,2,3,4,3,3,3,33,4,4,4,4]
print(lista)

# tupla(): coleccion ordenada e inmutable de elementos (cada elemento tendra un indice)

tupla = (0,1,2,3,4)
tupla2 = ("a", 'b', "c")

#range: es una secuencia de numeros generada dentro de un rango
rango = range(1,10)

# dict (dictionary-diccionario){}: coleccion de pares clave-valor(key:value) desordenada y mutable

diccionario = {
    'nombre': 'walter',
    "edad": 37,
    'diccionario':{
        "nombre":'samuel'
    }
}

#set{}: coleccion desordenada de elementos unicos y mutables

conjunto = {1,1,1,2,2,3,3,3,4,4,4,4,4, 5,5,5}

print(conjunto)

#forzenSet([]): coleccion desordenada de elementos unicos y mutables

conjunto_inmutable= frozenset([1,2,3,4,4,4,44,])

print(conjunto_inmutable)

# bool(booleanos): este dato representa verdadero(true) falsp(false)


booleanoVerdadero = True
booleanoFalso = False








