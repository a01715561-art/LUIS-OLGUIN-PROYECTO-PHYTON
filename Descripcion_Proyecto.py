
# Calculadora de impuestos, yo creo que interesa porque es facilitar el calcular los
# impuestos de las personas, con tan solo poner tu salario semanal, cuantas horas normales 
# trabajas a la semana y cuantas horas extra hiciste en el mes y te da los impuestos que pagas
# al mes y el porcentaje de impuestos que pagas, dependiendo de cuanto gana una persona el porcentaje de cuantos 
# imouestos tiene que pagar es mayor, mi intencion es facilitar la duda y la investigada de 
# cuanto deben de pagar y desglosando en que se van esos impuestos.
# Entrada:
# N = numero entero
# N = numero entero
# N = numero entero 
# ALGORITMO:
# 1.-SOLICITAR cuantas horas trabaja a la semana,
# cuanto gana a la semana, cuantas horas extra hizo en el mes 
# 2.-lo que gana a la semana por cuatro para sacar cuanto gana al mes
#  2.1.-mostrar cuanto gana al mes 
# 3.-dividir el sueldo semanal entre las horas trabajadas a la semana 
#  3.1.-multiplicar horas trabajadas por horas extra 
#   3.1.1.-multiplicar el resultado por 2
#  3.2.-si son mas de nueve horas extra apartir de la decima pasa lo siguiente
#    3.2.1.-de la hora numero 10 en adelante se multiplica el resultado por 3 
#  3.3.-sumar las horas dobles mas las horas triples = horas extra totales 
#  3.4.-sumar salario mensual mas horas extra totales = salario total 
#  3.5.-mostrar salario total
# 4.-establecer lista de rango de porcentaje de impuestos dependiendo rango del ssalario
# 5.-si salario total esta entra en cierto rango numerico ubicar  
#  5.1.-si el salario total sobrepasa el rango comprobar con otro rango numerico mas elevado
#  5.2.-asi sucesivamente hasta llegar al rango en el que se encuentre 
#  5.3.-restarle el porsentaje al salario total 
# 6.-mostrar cuanto es de impuestos 
# SALIDA:
# N = numero decimal
# N = numero decimal
# N = numero decimal

   #solicitar los datos
import math 

def calcularHoras(extras, horaPagada) :
    if extras <= 9 :
        extrasPagadas = horaPagada * extras * 2
    else:
        extrasPagadas = (9 * horaPagada * 2) + ((extras - 9) * horaPagada * 3)

        return extrasPagadas
    
salarios = []
horasNormales = []
horasExtras = []
salariosAlMes = []
extrasPagadas = []

empleados = int(input("Cuantos empleadops vas a ingresar? "))

for i in range(empleados) :
    print(f"\n --- EMPLEADO {i + 1} --- ")
    salario = int(input("Ingresa salario semanal: "))
    horas = int(input("Ingresa horas normales trabajadas a la semana: "))
    extras = int(input("Ingresa horeas extra trabajadas en el mes: "))

    salarios.append(salario)
    horasNormales.append(horas)
    horasExtras.append(extras)

    salarioMes = salario * 4
    horaPagada = salario / horas
    extraPagada = calcularHoras(extras, horaPagada)

    salariosAlMes.append(salarioMes)
    extrasPagadas.append(extraPagada)

    print(f"El salario munsual es de: {salarioMes}")
    print(f"A la hora ganas: {horaPagada}")
    print(f"Pago horas extra al mes: {extrasPagadas}")
