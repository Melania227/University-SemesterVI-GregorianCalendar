
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


print(fecha_es_tupla((2001,2,27)))