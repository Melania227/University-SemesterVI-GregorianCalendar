const fecha_max = [9999, 12, 31];
const fecha_min = [1582, 10, 15];
const dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const nombre_dia = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

//E: -
//S: boolean
//D: Función que valida un dato es de tipo entero y además si es un número positivo
function es_entero_positivo(num) {
    if (typeof (num) == 'number')
        return (Number.isInteger(num) && num > 0)
    return false;
}

//--------------------------------------- fecha_es_tupla ----------------------------------------------

//E: string (representa el tipo de error por imprimir)
//S: void / Impresión del error
//D: Función que verifica si la fecha introducida está en formato de tupla compuesta por tres
//             números enteros positivos en el orden de año, mes, día
function fecha_es_tupla(fecha) {
    if (typeof (fecha) == 'object' && (fecha instanceof Array)) {
        if (fecha.length() == 3) {
            if (es_entero_positivo(fecha[0]) && es_entero_positivo(fecha[1]) && es_entero_positivo(fecha[2])) {
                if (orden_de_fecha(fecha)) {
                    return true;
                } else {
                    generar_error('fecha_desordenada');
                    return false;
                }
            } else {
                generar_error('entero_positivo');
                return false;
            }
        } else {
            generar_error('tamano_tupla');
            return false;
        }
    } else {
        generar_error('no_es_tupla');
        return generar_error('no_es_tupla');;
    }
}


//E: tupla
//S:  boolean
//D:  Función que valida que el orden de la fecha sea correcta (año,mes,día)
function orden_de_fecha(fecha) {
    let dia = fecha[2];
    let mes = fecha[1];
    let anno = fecha[0];
    if (formato_anno(anno) && formato_dia_mes(mes) && formato_dia_mes(dia))
        return true;
    else
        return false;
}

//E: entero
//S: boolean
//D: Función que valida que el año contenga 4 dígitos
function formato_anno(anno) {
    contador = 0;
    while (anno > 0) {
        anno = anno / 10;
        contador += 1;
    }
    return contador == 4;
}

//E: entero
//S: boolean
//D: Función que valida que el día o el mes estén compuestos por 1 o 2 dígitos
function formato_dia_mes(dia_mes) {
    contador = 0;
    while (dia_mes > 0) {
        dia_mes = dia_mes / 10;
        contador += 1;
    }
    return contador == 2 || contador == 1;
}






// ------------------------------------------ bisiesto ---------------------------------------------------



//E: Un numero entero entre 1582 y 9999
//S: Un Booleano
//D: Ingresado un número, revisa que esté en el rango y retorna true en caso de ser bisiesto, en caso contrario retorna false 
function bisiesto(num) {
    if (es_entero_positivo(num)) {
        if (anno_en_rango(num)) {
            if (num % 4 == 0) {
                if (num % 100) {
                    return (num % 400);
                }
                return true;
            }
            return false;
        }
        return generar_error('año_rango');
    }
    return generar_error('año_entero_positivo');
}

//E: número entero positivo
//S: boolean
//D: Función que valida si un año se encuentra dentro del rango válifo según el calendario gregoriano
function anno_en_rango(num) {
    return fecha_min[0] <= num && num <= fecha_max[0];
}

// --------------------------------------- fecha_es_valida -----------------------------------------------

//E: fecha en formato de tupla
//S: boolean
//D: Función que valida si la fecha ingresada es válida según el calendario gregoriano
function fecha_es_valida(fecha) {
    if (fecha_es_tupla(fecha)) {
        let anno = fecha[0];
        let mes = fecha[1] - 1;
        let dia = fecha[2];
        if (anno_en_rango(anno)) {
            es_bisiesto = bisiesto(anno) ? 1 : 0;
            if (mes >= 0 && mes <= 11) {
                dias_del_mes = mes == 1 ? dias_mes[mes][es_bisiesto] : dias_mes[mes];
                if (dia >= 1 && dia <= dias_del_mes)
                    return true;
                else {
                    generar_error('rango_dia');
                    return false;
                }
            } else {
                generar_error('rango_mes');
                return false;
            }
        } else {
            generar_error('rango_anno');
            return false;
        }
    } else {
        generar_error('tupla_invalida');
        return false;
    }
}

// ----------------------------------- dias_siguiente ------------------------------------------

//E: Una tupla que representa una fecha
//S: Una tupla que representa una fecha
//D: Ingresado una fecha, retorna la siguiente fecha válida
function dia_siguiente(fecha) {
    let dia = fecha[2];
    let mes = fecha[1];
    let anno = fecha[0];
    let es_bisiesto = bisiesto(anno) ? 1 : 0;
    if (fecha_es_valida) {
        if (mes == 2) { //Caso Febrero
            return dia < dias_mes[1][es_bisiesto] ? [anno, mes, dia + 1] : [anno, mes + 1, 1];
        } else {
            if (dia < dias_mes[mes - 1]) {
                return [anno, mes, dia + 1];
            } else if (dia == dias_mes[mes - 1]) {
                if (mes == 12) {
                    return [anno + 1, 1, 1];
                } else {
                    return [anno, mes + 1, 1];
                }
            }
        }
    }
    return false;
}

function generar_error(tipo) {
    switch (tipo) {
        case 'entero_positivo':
            return 'ERROR: La tupla debe estar compuesta por números enteros positivos.';
        case 'año_entero_positivo':
            return 'ERROR: El año debe estar compuesta por un número entero positivo.';
        case 'año_rango':
            return 'ERROR: El año ingresado está fuera del rango válido.';
    }
}

//E: Un numero entero entre 1582 y 9999
//S: Un numero
//D: Ingresado un número, el sistema determinará y retornará en formato codificado un número entero conforme al día de la semana que corresponde al primero de enero del año ingresado. 
function dia_primero_enero(anno) {
    if (es_entero_positivo(anno)) {
        if (anno_en_rango(anno)) {
            let codigo = ((anno - 1) % 7 + ((anno - 1) / 4 - (3 * ((anno - 1) / 100 + 1) / anno)) % 7 + 0 + 1 % 7) % 7;
            return codigo;
        }
        return generar_error('año_rango');
    }
    return generar_error('año_entero_positivo');
}