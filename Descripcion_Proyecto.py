
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

  
import math


def calcular_horas_extras(extras, hora_pagada):
    if extras <= 9:
        extras_pagadas = hora_pagada * extras * 2
    else:
        extras_pagadas = (9 * hora_pagada * 2) + ((extras - 9) * hora_pagada * 3)
    return extras_pagadas 

TABLA_ISR_MENSUAL_2025 = [
    (0.01,        746.04,       0.00,      0.0192),
    (746.05,      6332.05,     14.32,      0.0640),
    (6332.06,     11128.01,   371.83,      0.1088),
    (11128.02,    12935.82,   893.63,      0.1600),
    (12935.83,    15487.71,  1182.88,      0.1792),
    (15487.72,    31236.49,  1640.18,      0.2136),
    (31236.50,    49233.00,  5004.12,      0.2352),
    (49233.01,    93993.90,  9236.89,      0.3000),
    (93993.91,   125325.20, 22665.17,      0.3200),
    (125325.21,  375975.61, 32691.18,      0.3400),
    (375975.62,        float("inf"), 117912.32, 0.3500),
]

def calcular_isr_mensual(base_gravable):
    if base_gravable <= 0:
        return 0.0
    for lim_inf, lim_sup, cuota_fija, tasa in TABLA_ISR_MENSUAL_2025:
        if lim_inf <= base_gravable <= lim_sup:
            excedente = base_gravable - lim_inf
            return cuota_fija + excedente * tasa

    lim_inf, _, cuota_fija, tasa = TABLA_ISR_MENSUAL_2025[-1]
    return cuota_fija + (base_gravable - lim_inf) * tasa

salarios_semanales = []
horas_normales_semana = []
horas_extras_mes = []
salarios_mensuales = []
extras_pagadas_mes = []
isr_mensual = []
neto_mensual = []

empleados = int(input("¿Cuántos empleados vas a ingresar? "))

for i in range(empleados):
    print(f"\n --- EMPLEADO {i + 1} --- ")
    salario_sem = float(input("Ingresa salario semanal: "))
    horas_sem = float(input("Ingresa horas normales trabajadas a la semana: "))
    extras_mes = float(input("Ingresa horas extra trabajadas en el mes: "))

    salarios_semanales.append(salario_sem)
    horas_normales_semana.append(horas_sem)
    horas_extras_mes.append(extras_mes)

    salario_mes = salario_sem * 4
    hora_pagada = salario_sem / horas_sem if horas_sem > 0 else 0.0
    pago_extras = calcular_horas_extras(extras_mes, hora_pagada)

    base_isr = salario_mes + pago_extras
    isr = calcular_isr_mensual(base_isr)
    neto = base_isr - isr

    salarios_mensuales.append(salario_mes)
    extras_pagadas_mes.append(pago_extras)
    isr_mensual.append(isr)
    neto_mensual.append(neto)

    print(f"Salario mensual: ${salario_mes:,.2f}")
    print(f"Paga por hora: ${hora_pagada:,.2f}")
    print(f"Pago horas extra (mes): ${pago_extras:,.2f}")
    print(f"ISR mensual calculado: ${isr:,.2f}")
    print(f"Total neto mensual (después de ISR): ${neto:,.2f}")
