#Impresión de cadenas de texto, estas pueden ir en comillas simples y comillas dobles
print('Hello\n')

#Conctatendando varios strings con comillas triples
a='''Usar Colab es algo nuevo para mi
pero prefieron usar Visual Code\n'''
print(a)

#Manejando strings usando posiciones
b='Hola Mundo\n'
print(b[1])

#Imprimiendo solo partes de una cadena de texto
print(b[0], b[1], b[2], b[3], b[4], "\n")

#Recorriendo un string con un loop for
for x in "banana\n":
    print(x)

#Recorriendo un string pero esta vez usando una variable
a = "Hola Mundo\n"
for x in a:
    print(x)

#Función length para saber la longitud de la cadena de texto
cadena = '''Hola mundo como estas el dia de hoy porque el ha estado muy soleado y con algunas nubes que apenas dan sombra\n'''
print(len(cadena))

#Verificar si existe una frase dentro de una cadena de texto
if 'hola' in cadena.lower():
    print('Si')
else:
    print('No')

#Verificar si existe frasde en una cadena de texto pero en negacion
if 'mando' not in cadena:
    print('No existe')

#Cortar un string
print(cadena[20:50])

#cortas cadena desde un putno x hasta el final
print(cadena[50:])

#Cortar cadena de derecha a izquierda
print(cadena[-20:-10])

#Uppercase and lowercase
frase = "  Hola, buen, dia  "
print(frase.upper())
print(frase.lower())

##Quita espacios de los extremos
print(frase.strip())

#Reemplazar caracteres
print(frase.replace("buen", "buenos"))

#Separar frase en varios elementos usando un caracter
print(frase.split(','))

#Uso de parantesis para insertar valores dentro de una cadena de texto
age = 50
palabras = "Hoy esta siendo {} muy tecnica la clase"
print(palabras.format(age))

#Usar index para ubicar valores dentro de una cadena 
cade = "Esta algo teorica{2} la materia {0}cuando es inicio{1} de clases"
print(cade.format("40", "100", "#"))