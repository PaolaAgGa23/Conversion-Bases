#EQUIPO 1
#Coversión de unas bases a otras
import math

#Convertir las letras a los valores correspondientes
def convertir(valor):
  if valor =="A" or valor == "a":
    return "10"
  elif valor =="B" or valor == "b":
    return "11"
  elif valor =="C" or valor == "c":
    return "12"
  elif valor =="D" or valor == "d":
    return "13"
  elif valor =="E" or valor == "e":
    return "14"
  elif valor =="F" or valor == "f":
    return "15"
  else:
    return valor

#Convertir los valores a las letras correspondientes
def desconvertir(valor):
  if valor =="10":
    return "A"
  elif valor =="11":
    return "B"
  elif valor =="12":
    return "C"
  elif valor =="13":
    return "D"
  elif valor =="14":
    return "E"
  elif valor =="15":
    return "F"
  else:
    return valor


#Pedir los valores (no se verifica la entrada de los valores)
x = str(input(" Ingrese el valor a convertir: "))
origen = int(input(" Ingrese la base origen: "))
destino = int(input(" Ingrese la base destino: "))

suma=0
valEntero=""
valDecimal=""
bandera=0

#Separa el valor entero y el decimal para trabajar más fácil con él
for digito in x:
  if digito !="." and bandera==0:
    valEntero= valEntero+digito
  elif digito =="." and bandera==0:
    bandera=1
  elif digito!="." and bandera==1:
    valDecimal= valDecimal+digito

#Para la conversión a decimal del pedazo entero separado antes
sumaEntero = 0
posicion=len(valEntero) -1
for digito in valEntero:
  digito=int(convertir(digito))
  nuevoVal=digito*(origen**posicion)
  sumaEntero=sumaEntero+nuevoVal
  posicion=posicion-1

#Para la conversión a decimal del pedazo decimal separado antes
sumaDecimal = 0
posicion=-1
for digito in valDecimal:
  digito=int(convertir(digito))
  nuevoVal=digito*(origen**posicion)
  sumaDecimal=sumaDecimal+nuevoVal
  posicion=posicion-1
  
#Convertir la parte entera de base 10 a la base destino
cociente=1
finalEntero=""
while cociente!=0:
  cociente = (sumaEntero//destino)
  residuo = str(sumaEntero%destino)
  residuo = desconvertir(residuo)
  finalEntero= finalEntero+residuo
  sumaEntero = cociente

#Convertir la parte decimal de base 10 a la base destino
parte_decimal=0
parte_entera=0
finalDecimal=""
if sumaDecimal!=0:
  while parte_entera<=0:
    multiplicacion = sumaDecimal*destino
    parte_decimal, parte_entera = math.modf(multiplicacion)
    sumaDecimal = parte_decimal
    parte_entera_str = str(int(parte_entera))
    parte_entera_str = desconvertir(parte_entera_str)
    finalDecimal= finalDecimal+parte_entera_str

#Concatenar los resultados e imprimir el resultado final
resultado= finalEntero[::-1]+"."+finalDecimal
print("Tu resultado es: ", resultado)