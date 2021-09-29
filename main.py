# ------------------------------------- Variable Globales ---------------------------------------------
fecha_max = [9999, 12, 31]
fecha_min = [1582, 10, 15]
dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fecha_actual = (2021,9,27)
dia = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

# --------------------------------------- fecha_es_tupla ----------------------------------------------

#Entradas: string (representa el tipo de error por imprimir)
#Salidas: void / Impresión del error
#Descripción: Función que verifica si la fecha introducida está en formato de tupla compuesta por tres
#             números enteros positivos en el orden de año, mes, día
def fecha_es_tupla(fecha):
    if type(fecha) == tuple:
        if len(fecha)==3:
            if es_entero_positivo(fecha[0]) and es_entero_positivo(fecha[1]) and es_entero_positivo(fecha[2]):
                if orden_de_fecha(fecha):
                    return True
                else:
                    generar_error('fecha_desordenada')
                    return False
            else:
                generar_error('entero_positivo')
                return False
        else:
            generar_error('tamano_tupla')
            return False
    else:
        generar_error('no_es_tupla')
        return False


#Entradas: cualquier tipo posible
#Salidas: boolean
#Descripción: Función que valida un dato es de tipo entero y además si es un número positivo
def es_entero_positivo(dato):
    return (type(dato) == int and dato>=0)


#Entradas: tupla
#Salidas: boolean
#Descripción: Función que valida que el orden de la fecha sea correcta (año,mes,día)
def orden_de_fecha(fecha):
    anno = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    if formato_anno(anno) and formato_dia_mes(mes) and formato_dia_mes(dia):
        return True
    else:
        return False

#Entradas: entero
#Salidas: boolean
#Descripción: Función que valida que el año contenga 4 dígitos
def formato_anno(anno):
    contador = 0
    while (anno > 0):
        anno = anno//10
        contador += 1
    return contador==4

#Entradas: entero
#Salidas: boolean
#Descripción: Función que valida que el día o el mes estén compuestos por 1 o 2 dígitos
def formato_dia_mes(dia_mes):
    contador = 0
    while (dia_mes > 0):
        dia_mes = dia_mes//10
        contador += 1
    return contador==2 or contador==1



# ------------------------------------------ bisiesto ---------------------------------------------------

#Entradas: número entero entre 1582 y 9999
#Salidas: boolean
#Descripción: Ingresado un número, revisa que esté en el rango y retorna true en caso de ser bisiesto, 
#             en caso contrario retorna false
def bisiesto(num):
    if (es_entero_positivo(num)):
        if (anno_en_rango(num)):
            if (num % 4 == 0):
                if (num % 100):
                    return (num % 400)
                return True
            return False
        return generar_error('rango_anno')
    return generar_error('año_entero_positivo')


#Entradas: número entero positivo
#Salidas: boolean
#Descripción: Función que valida si un año se encuentra dentro del rango válifo según el calendario 
#             gregoriano
def anno_en_rango(anno):
    return fecha_min[0] <= anno and fecha_max[0] >= anno



# --------------------------------------- fecha_es_valida -----------------------------------------------

#Entradas: fecha en formato de tupla
#Salidas: boolean
#Descripción: Función que valida si la fecha ingresada es válida según el calendario gregoriano
def fecha_es_valida(fecha):
    if fecha_es_tupla(fecha):
        anno = fecha[0]
        mes = fecha[1]-1
        dia = fecha[2]
        if anno_en_rango(anno):
            es_bisiesto = 1 if bisiesto(anno) else 0
            if mes >=0 and mes <= 11:
                dias_del_mes = dias_mes[mes][es_bisiesto] if mes==1 else dias_mes[mes]
                if dia>=1 and dia <= dias_del_mes:
                    return True
                else:
                    generar_error('rango_dia')
                    return False
            else:
                generar_error('rango_mes')
                return False
        else:
            generar_error('rango_anno')
            return False
    else:
        generar_error('tupla_invalida')
        return False



# ----------------------------------- dias_desde_primero_enero ------------------------------------------

#Entradas: Una tupla que representa una fecha
#Salidas: Una tupla que representa una fecha
#Descripcion: Ingresado una fecha, retorna la sigueinte fecha válida.
def dia_siguiente(fecha):
    dia = fecha[2]
    mes = fecha[1]
    anno = fecha[0]
    es_bisiesto = 1 if bisiesto(anno) else 0
    if (fecha_es_valida):
        if (mes == 2):
            [anno, mes, dia + 1] if dia < dias_mes[1][es_bisiesto] else [anno, mes + 1, 1]
        elif (dia < dias_mes[mes - 1]):
            return [anno, mes, dia + 1]
        elif (dia == dias_mes[mes - 1]):
            if (mes == 12):
                return [anno + 1, 1, 1]
            else:
                return [anno, mes + 1, 1]
    return False
        


# ----------------------------------- dias_desde_primero_enero ------------------------------------------

#Entradas: fecha en formato de tupla
#Salidas: número entero positivo
#Descripción: Función que dada una fecha válida deberá determinar el número entero de días transcurridos
#             desde el primero de enero del año ingresado hasta el día de la fecha dada.
def dias_desde_primero_enero(fecha):
    if fecha_es_valida(fecha):
        anno = fecha[0]
        mes = fecha[1]-1
        dia = fecha[2]
        es_bisiesto = 1 if bisiesto(anno) else 0
        if mes==1:
            return 0
        else:
            res = 0
            for i in range(0,len(dias_mes)):
                d=dias_mes[i]
                if type(dias_mes[i]) != int:
                    d = dias_mes[i][es_bisiesto]
                if i==mes:
                    res+=dia-1
                    return res
                else:
                    res+=d
            return res
    else:
        generar_error('fecha_invalida')
        return 0



# ----------------------------------- dias_desde_primero_enero ------------------------------------------

#Entradas: Un numero entero entre 1582 y 9999
#Salidas: Un numero entero
#Descripción: Ingresado un número, el sistema determinará y retornará en formato codificado un número 
#             entero conforme al día de la semana que corresponde al primero de enero del año ingresado. 
#NOTA: Para esta solución se hizo uso de la fórmula de Gauss
def dia_primero_enero(anno):
    if es_entero_positivo(anno):
        if anno_en_rango(anno):
            f_g= [0, 5, 3, 1]
            c = (anno-1)//100
            g = anno - 1 - (100 * c)
            w = (1 +0 + f_g[c%4] + g + (g//4))%7
            return w
        else:
            generar_error('rango_anno')
            return 0
    else:
        generar_error('año_entero_positivo')
        return 0



# ------------------------------------- impresión de errores --------------------------------------------

#Entradas: string (representa el tipo de error por imprimir)
#Salidas: void / Impresión del error
#Descripción: Función específica para generar errores (consideraciones de diseño tomadas).
def generar_error(tipo):
    if tipo == 'no_es_tupla':
        print('ERROR: La fecha ingresada debe estar en formato de tupla')
    elif tipo == 'tamano_tupla':
        print('ERROR: La tupla debe estar compuesta por 3 números enteros positivos')
    elif tipo == 'entero_positivo':
        print('ERROR: La tupla debe estar compuesta por números enteros positivos')
    elif tipo == 'fecha_desordenada':
        print('ERROR: La fecha debe venir en el orden año, mes, día')
    elif tipo == 'tupla_invalida':
        print('ERROR: El formato de la tupla ingresada es inválido')
    elif tipo == 'formato_anno':
        print('ERROR: El año debe estar compuesto por 4 dígitos')
    elif tipo == 'formato_mes_dia':
        print('ERROR: El mes y el día deben estar compuestos por 1 o 2 dígitos')
    elif tipo == 'rango_anno':
        print('ERROR: El año no se encuentra dentro del rango válido por el calendario gregoriano')
    elif tipo == 'rango_mes':
        print('ERROR: El mes no se encuentra dentro del rango válido por el calendario gregoriano')
    elif tipo == 'rango_dia':
        print('ERROR: El día no se encuentra dentro del rango válido por el calendario gregoriano')
    elif tipo == 'fecha_invalida':
        print('ERROR: La fecha ingresada es inválida')
    elif tipo ==  'año_entero_positivo':
        print('ERROR: El año debe ser un número entero positivo')


print(dia_primero_enero((9999)))