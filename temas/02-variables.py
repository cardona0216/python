# variables

#que es una varaibles

# es una espwcio de menoria que se usa para almacenar datos este espacio de menoria o contenedor tendra un nombre
# las reglas generales para darle el nombre a las varianles es que deben de ser claras y en lo posible que sean
# semanticamente acordes a lo que queremos guardar es decir que se pueda entender que va a contener

# en python es algo especial

#Variables:
# es un contenedor para almacenar valores de datos
# este contenedor va a tener un nombre
# es creada la primera vez que se le asigne un valor

#nombres de las varables admitidas

# las variavles en pytohn son casesentive es decir desitingue entre minusculas y mayusculas

Mivariable = "nombre variable"

mivariable = 'otra variable'

# las vaiables en python no pueden iniciar con numeros

# 2variable = 'texto'

# print(2variable)


# solo pueden contener alfanumericos y guines bajos (A-z 0-9)

_123varaible= 'texto'
variable123 = """
 otro texto
"""
# valor$ = 'esta varible no es permitida'

# es case sensitive
miVarible = 'otro texto'
MiVariablE = 'otro texto mas'


# no se puede utilizar palabras reservadas de python(keywords)

# if = 'palabra reservada if'

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

    
# and = 'palabra reservada'

# convencines de escritura de varibles es decir como es lo recomendable o como es lo comun que se deben de usar

# camelCase
camelCase = 'comineza con minuscula y cada palabra siguibte comnezara con mayuscula'

# PascalCase
PascalCase = 'comineza con mayuscula y cada palabra siguiente comenzara con mayuscula'

#Snake Case

snake_case = 'se usan las palbras en minusculas y las palabras son separadas con guiones bajos'

#multiasignacion

x,y,z = 5,6,7

print(x)
print(y)
print(z)

a = b = c = "walter cardona"

b = 'samuel'
print(a)
print(b)
print(c)


frutas = ['naranja', "banana", 'mandarina']

n,m,o = frutas

print(n)
print(m)
print(o)

# uso de print y salidas

txt = 'curso '
txt2 = "de "
txt3 = " python"

print(txt + txt2 + txt3) # con esto estamos concatenando


# con numeros

num = 2
num2 = 3
num3 = 5

print(num + num2 + num3) # aqui estariamos sumando los numeros

print (num , num2 , num3)  # aqui si lo estariamos colocanod uno a l lado del otro

# entorno de las variables 
# esto quiere decir que hay variables de forma global y varinles de un entrono especifico (scope)

# Variables globales vs varibles scope(el alcance que tiene la variable)

variableGlobal = "esta variable va a estar disponible para todo el programa"

def funcion():
    global variableDeScope
    variableDeScope = "esta variable solo estara disponible dentro del alcance  de la funcion(scope)"
    variableGlobal = "este valor es solo para dentro de la funcion y luego recupera su valor"
    print(variableGlobal)
    print(variableDeScope)

funcion()

print(variableGlobal)
print(variableDeScope)
