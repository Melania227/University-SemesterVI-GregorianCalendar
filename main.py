# ------------------------------------- Variable Globales ---------------------------------------------
fecha_max = [9999, 12, 31]
fecha_min = [1582, 10, 15]
dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fecha_actual = (2021,9,27)

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
                    print("fecha desordenada")
                    return False
            else:
                print("no todo es entero positivo")
                return False
        else:
            print("no es tamanho 3")
            return False
    else:
        print("no es tuple")
        return False


#Entradas: cualquier tipo posible
#Salidas: boolean
#Descripción: Función que valida un dato es de tipo entero y además si es un número positivo
def es_entero_positivo(dato):
    return (type(dato) == int and dato>0)


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
def bisiesto(anno):
    if (es_entero_positivo(anno)):
        if anno_en_rango(anno):
            if (anno % 4 == 0):
                if (anno % 100):
                    return (anno % 400)
                return True
            return False
        return False
    return False


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
                    print("dias no dentro de rango")
                    return False
            else:
                print("mes no dentro de rango")
                return False
        else:
            print("anno no dentro de rango")
            return False
    else:
        print("no es tupla valida")
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
            print("mes de enero, 0 dias transcurridos")
            return 0
        elif anno <= fecha_actual[0] and mes <= fecha_actual[1] and dia <= fecha_actual[2]:
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
            print("fecha mayor a la actual")
            return 0
    else:
        print("fecha invalida")
        return False




#Entradas: string (representa el tipo de error por imprimir)
#Salidas: void / Impresión del error
#Descripción: Función específica para generar errores (consideraciones de diseño tomadas)
def generar_error(tipo):
    if tipo == 'es_tupla':
        print('ERROR: La fecha ingresada debe estar en formato de tupla')
    elif tipo == 'entero_positivo':
        print('ERROR: La tupla debe estar compuesta por números enteros positivos')
    elif tipo == 'formato_anno':
        print('ERROR: El año debe estar compuesto por 4 dígitos')
    elif tipo == 'entero_mes_dia':
        print('ERROR: El mes y el día deben estar compuestos por 1 o 2 dígitos')


print(dias_desde_primero_enero((2021,9,27)))