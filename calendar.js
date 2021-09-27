const fecha_max = [9999, 12, 31];
const fecha_min = [1582, 10, 15];
const dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const dia = ['domingo', 'lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado']

function validar_numero(num) {
    if (typeof (num) == 'number')
        return (Number.isInteger(num) && num > 0)
    return false;
}

function anno_en_rango(num) {
    return fecha_min[0] <= num && num <= fecha_max[0];
}

//E: Un numero entero entre 1582 y 9999
//S: Un Booleano
//D: Ingresado un número, revisa que esté en el rango y retorna true en caso de ser bisiesto, en caso contrario retorna false 
function bisiesto(num) {
    if (validar_numero(num)) {
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


//E: Una tupla que representa una fecha
//S: Una tupla que representa una fecha
//D: Ingresado una fecha, retorna la sigueinte fecha válida
function dia_siguiente(fecha) {
    let dia = fecha[2];
    let mes = fecha[1];
    let anno = fecha[0];
    let es_bisiesto = bisiesto(anno) ? 1 : 0;

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

function dia_primero_enero(num){

}