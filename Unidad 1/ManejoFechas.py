import datetime

#Extracción del dia actual
x = datetime.datetime.now()
print(x)

#Extraccion del año y del dia en formato de texto como Lunes, Martes, Miercoles, Jueves y viernes
print(x.year)
print(x.strftime("%A")) 

#I
x = datetime.datetime(2020, 5, 17)
print(x) 

Fecha = datetime.datetime(2021, 9, 3)
print(Fecha) 
print(Fecha.strftime("%B"))

#tres variables para partir la fecha en dia, mes año en numeral
anio = Fecha.strftime("%Y")
mes = Fecha.strftime("%m")
dia = Fecha.strftime("%d")
print(anio,'-',mes,'-',dia)