# ------------------------------------- Variable Globales ---------------------------------------------
fecha_max = [9999, 12, 31]
fecha_min = [1582, 10, 15]
dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
fecha_actual = (2021,9,27)
dia = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']
dias_calendario = '  D  L  K  M  J  V  S |'
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']



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
    if (num % 4 == 0):
        if (num % 100 !=0):
            if (num % 400):
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
        
        es_bisiesto = 1 if bisiesto(anno) else 0
        if mes >=0 and mes <= 11:
            dias_del_mes = dias_mes[mes][es_bisiesto] if mes==1 else dias_mes[mes]
            if dia>=1 and dia <= dias_del_mes:
                if fecha_en_rango(fecha): 
                    return True
                else:
                    generar_error('rango_fecha')
                    return False
            else:
                generar_error('rango_dia')
                return False
        else:
            generar_error('rango_mes')
            return False
    else:
        return False


#Entradas: fecha en formato de tupla
#Salidas: boolean
#Descripción: Función que valida si la fecha ingresada se encuentra dentro de los rangos del calendario gregoriano
def fecha_en_rango(fecha):
    anno = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    if anno == fecha_min[0] and mes == fecha_min[1] and dia == fecha_min[2]:
        return False
    elif anno == fecha_min[0] and mes <= fecha_min[1]:
        return False
    elif anno >= fecha_min[0] and anno <= fecha_max[0]:
        return True



# ----------------------------------- dias_siguiente ------------------------------------------

#Entradas: Una tupla que representa una fecha
#Salidas: Una tupla que representa una fecha
#Descripcion: Ingresado una fecha, retorna la siguiente fecha válida.
def dia_siguiente(fecha):
    dia = fecha[2]
    mes = fecha[1]
    anno = fecha[0]
    es_bisiesto = 1 if bisiesto(anno) else 0
    if (fecha_es_valida(fecha)):
        if (mes == 2):
            (anno, mes, dia + 1) if dia < dias_mes[1][es_bisiesto] else (anno, mes + 1, 1)
        elif (dia < dias_mes[mes - 1]):
            return (anno, mes, dia + 1)
        elif (dia == dias_mes[mes - 1]):
            if (mes == 12):
                return (anno + 1, 1, 1)
            else:
                return (anno, mes + 1, 1)
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



# ----------------------------------- 6.imprimir_4x3 ------------------------------------------

#E: Un numero entero entre 1582 y 9999
#S: Un booleano. Imprimer en consola si el booleano es positivo.
#D: Ingresado un año se imprime en consola el calendario correspondiente en formato 4x3. 

def imprimir_4x3(anno):
    print('Calendario del año '+str(anno)+ ' D.C.')
    print(' ')
    if es_entero_positivo(anno) :
        if anno_en_rango(anno) :
            res = calendario(anno)
            orden = []
            for j in range (0,8):
                linea = ''
                c=0
                orden.append([])
                for i in range (0,12) :
                    linea += res[i][j]
                    if ((i+1)%3==0 ):
                        orden[j].append(linea)
                        linea = ''
                        c+=1
            for n in range (0,4) :
                for i in range (0,8) :
                    print(orden[i][n])
                
                print(' ')
            
            return True   
        
    return False
    

#E: Un numero entero entre 1582 y 9999
#S: Retorna una matriz
#D: Ingresado un año retorna en formato de matriz el calendario correspondiente. 
def calendario(anno) :
    calendario = []
    bis = 1 if bisiesto(anno) else 0
    dia_inicio = dia_primero_enero(anno)
    for i in range(0, 12) :
        res = imprimirMes(dia_inicio, i, bis)
        calendario.append(res[0])
        dia_inicio = res[1]+1
    
    return calendario


#E: Día de inicio, mes, un booleano.
#S: Retorna una tupla con el mes del año en formato de matriz y el ultimo día del mes.
#D: Funcion que genera la matriz de un mes del año.
def imprimirMes(inicio, mes, bis):
    matriz = []
    matriz.append(nombre_mes(mes))
    matriz.append(dias_calendario)
    cont = 1
    max = dias_mes[1][bis] if mes == 1 else dias_mes[mes]
    for i in range(2,8):
        linea = ''  if i != 2 else ('   '*(inicio))
        for dia in range(inicio,7):
            if cont <= max:
                if cont==max:
                    final = dia
                
                linea+= '  '  if (cont < 10 ) else  ' ' 
                linea+= str(cont)
                cont+=1
        if cont>max:
            matriz.append(linea+ (' '*(22 -len(linea)))+'|')
        else:
            matriz.append(linea+' |')
        inicio = 0
    return [matriz, final]


#E: Un numero.
#S: Una lista de string.
#D: Funcion que genera la primeras linea de un mes.
def nombre_mes(mes):
    m_l = len(meses[mes])
    linea = (' '*(11 - m_l//2) )+ meses[mes]
    linea = linea + (' '*(22 -len(linea)))+'|'
    return linea



# ------------------------------------------ dia_semana -------------------------------------------------

def dia_semana(fecha):
    anno = fecha[0]
    mes = fecha[1]
    dia = fecha[2]
    if (mes < 3):
        mes += 12
        anno -= 1
    res = (dia + ((13 * (mes + 1)) // 5) + anno + (anno // 4) - (anno // 100) + (anno // 400)) % 7
    if (res == 0):
        res == 6
    else:
        res -= 1
    return res



# ---------------------------------------- fecha_futura -------------------------------------------------

#Entradas: Una fecha válida y un número entero positivo (incluye al 0)
#Salidas: Una fecha válida
#Descripción: Ingresado un número entero positivo n y una fecha válida, el sistema deberá encontrar 
#             una fecha válida existente n días después la fecha indicada. 

def fecha_futura (fecha, dias):
    if (fecha_es_valida(fecha)):
        if (es_entero_positivo(dias)):
            anno = fecha[0]
            mes = fecha[1]
            dia = fecha[2]
            dias_temp = dias+dias_desde_primero_enero(fecha)
            dia=1 
            mes=1
            print(dias_temp)
            while(dias_temp>366):
                es_bisiesto = 1 if bisiesto(anno) else 0
                dias_temp -= 366 if es_bisiesto else 365
                anno+=1
            print(dias_temp)

            es_bisiesto = 1 if bisiesto(anno) else 0
            for i in range (0, 12):
                diasMes = dias_mes[i][es_bisiesto] if i==1 else dias_mes[i]
                if dias_temp > diasMes:
                    dias_temp -= diasMes
                    mes+=1
                    continue
                break
            dia += dias_temp
            print(dias_temp)

            return (anno, mes, dia)
        else:
            generar_error('numero_entero_positivo')
    else:
        generar_error('fecha_invalida')



# ----------------------------------------- dias_entre -------------------------------------------------

#Entradas: Dos fechas válidas
#Salidas: Un número entero
#Descripción: Ingresadas dos fechas válidas el sistema deberá encontrar la cantidad de días que hay entre 
#             ellas
def dias_entre (fecha_1, fecha_2):
    dias = 0
    if (fecha_es_valida(fecha_1) and fecha_es_valida(fecha_2)):
        if(fecha_1[0]!=fecha_2[0]):
            # Se calcula el tiempo entre los años completos y para calcular los días de años no completos
            # se usa la función de dias_entre_mismo_anho
            if(fecha_1[0]<fecha_2[0]):
                # Se le suma un día ya que al hacer el calculo de días_entre de la fecha hasta fin de año
                # se pierde uno de los días hábiles entre las dos fechas originales
                dias += dias_entre_mismo_anho(fecha_1, (fecha_1[0],12,31))+1
                dias += dias_entre_mismo_anho(fecha_2, (fecha_2[0],1,1))
                if (fecha_2[0]-fecha_1[0]!=1):
                    #Sumo los años completos que falten
                    for i in range ((fecha_1[0]+1), fecha_2[0]):
                        dias += (366 if bisiesto(i) else 365)
                return dias 
            else:
                # Se le suma un día ya que al hacer el calculo de días_entre de la fecha hasta fin de año
                # se pierde uno de los días hábiles entre las dos fechas originales
                dias += dias_entre_mismo_anho(fecha_2, (fecha_2[0],12,31))+1
                dias += dias_entre_mismo_anho(fecha_1, (fecha_1[0],1,1))
                if (fecha_1[0]-fecha_2[0]!=1):
                    #Sumo los años completos que falten
                    for i in range ((fecha_2[0]+1), fecha_1[0]):
                        dias += (366 if bisiesto(i) else 365)
                return dias 
        else:
            dias = dias_entre_mismo_anho(fecha_1, fecha_2)
        return dias
    else:
        generar_error('fecha_invalida')
        return 0
                

#Entradas: Dos fechas válidas
#Salidas: Un número entero
#Descripción: Ingresadas dos fechas válidas que estén dadas en el mismo año, el sistema deberá encontrar 
#             la cantidad de días que hay entre ellas
def dias_entre_mismo_anho (fecha_1, fecha_2):
    dias = 0
    if (fecha_1[1]!=fecha_2[1]):
        if(fecha_1[1]<fecha_2[1]):
            mesMayor = fecha_2[1]
            mesMenor = fecha_1[1]
            #Sumo dias sobrantes y restantes para luego sumar los meses completos entre medias
            dias += fecha_2[2]
            es_bisiesto = 1 if bisiesto(fecha_1[0]) else 0
            dias += dias_mes[mesMenor-1][es_bisiesto]-fecha_1[2] if mesMenor-1==1 else dias_mes[mesMenor-1]-fecha_1[2]
            #Sumo los meses completos que falten
            for i in range ((mesMenor+1), mesMayor):
                i=i-1
                if (i==1):
                    es_bisiesto = 1 if bisiesto(fecha_2[0]) else 0
                    dias += dias_mes[i][es_bisiesto]
                else:
                    dias += dias_mes[i]
        else:
            mesMayor = fecha_1[1]
            mesMenor = fecha_2[1]
            #Sumo dias sobrantes y restantes para luego sumar los meses completos entre medias
            dias += fecha_1[2]
            es_bisiesto = 1 if bisiesto(fecha_1[0]) else 0
            dias += dias_mes[mesMenor-1][es_bisiesto]-fecha_2[2] if mesMenor-1==1 else dias_mes[mesMenor-1]-fecha_2[2]
            #Sumo los meses completos que falten
            for i in range ((mesMenor+1), mesMayor):
                i=i-1
                if (i==1):
                    es_bisiesto = 1 if bisiesto(fecha_2[0]) else 0
                    dias += dias_mes[i][es_bisiesto]
                else:
                    dias += dias_mes[i]
    else:
        if(fecha_1[2]<=fecha_2[2]):
            dias += fecha_2[2] - fecha_1[2]
        else:
            dias += fecha_1[2] - fecha_2[2]
    return dias



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
    elif tipo == 'año_entero_positivo':
        print('ERROR: El año debe ser un número entero positivo')
    elif tipo == 'rango_fecha':
        print('ERROR: La fecha ingresada no se encuentra dentro del rango válido por el calendario gregoriano')
    elif tipo == 'numero_entero_positivo':
        print('ERROR: La número ingresado debe ser entero y positivo')
        


print(dias_entre((2001,2,27),(2001,6,7)))
print(dias_entre((2001,2,27),(2233,7,26)))
print(dias_entre((2001,2,27),(2142,2,23)))
print(dias_entre((2001,2,27),(2022,1,31)))
print(dias_entre((2001,2,27),(2203,12,1)))
print(dias_entre((2001,2,27),(2123,12,13)))
print(dias_entre((2001,2,27),(2020,3,4)))

imprimir_4x3(2021)
imprimir_4x3(2001)

print(dia_semana((2002, 12, 25)))
