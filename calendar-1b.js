const fecha_max = [9999, 12, 31];
const fecha_min = [1582, 10, 15];
const dias_mes = [31, [28, 29], 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const dias_calendario = '  D  L  K  M  J  V  S |';
const nombre_dia = [' D', ' L', ' K', ' M', ' J', ' V', ' S'];
const meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Setiembre', 'Octubre', 'Noviembre', 'Diciembre']
const f_g = [0, 5, 3, 1];

//E: -
//S: boolean
//D: Función que valida un dato es de tipo entero y además si es un número positivo
function es_entero_positivo(num) {
    if (typeof (num) == 'number')
        return (Number.isInteger(num) && num > 0)
    return false;
}

//--------------------------------------- 0.fecha_es_tupla ----------------------------------------------

//E: string (representa el tipo de error por imprimir)
//S: void / Impresión del error
//D: Función que verifica si la fecha introducida está en formato de tupla compuesta por tres
//             números enteros positivos en el orden de año, mes, día
function fecha_es_tupla(fecha) {
    if (typeof (fecha) == 'object' && (fecha instanceof Array)) {
        if (fecha.length == 3) {
            if (es_entero_positivo(fecha[0]) && es_entero_positivo(fecha[1]) && es_entero_positivo(fecha[2])) {
                if (orden_de_fecha(fecha)) {
                    return true;
                } else {
                    console.log(generar_error('fecha_desordenada'));
                    return false;
                }
            } else {
                console.log(generar_error('entero_positivo'));
                return false;
            }
        } else {
            console.log(generar_error('tamano_tupla'));
            return false;
        }
    } else {
        console.log(generar_error('no_es_tupla'));
        return false;
    }
}

//E: tupla
//S:  boolean
//D:  Función que valida que el orden de la fecha sea correcta (año,mes,día)
function orden_de_fecha(fecha) {
    let dia = fecha[2];
    let mes = fecha[1];
    let anno = fecha[0];
    return (formato_anno(anno) && formato_dia_mes(mes) && formato_dia_mes(dia))
}

//E: entero
//S: boolean
//D: Función que valida que el año contenga 4 dígitos
function formato_anno(anno) {
    return anno.toString().length == 4 ? true : false;
}

//E: entero
//S: boolean
//D: Función que valida que el día o el mes estén compuestos por 1 o 2 dígitos
function formato_dia_mes(dia_mes) {
    return (dia_mes.toString().length == 2 || dia_mes.toString().length == 1) ? true : false;
}


// ------------------------------------------ 1.bisiesto ---------------------------------------------------

//E: Un numero entero entre 1582 y 9999
//S: Un Booleano
//D: Ingresado un número, revisa que esté en el rango y retorna true en caso de ser bisiesto, en caso contrario retorna false 
function bisiesto(num) {
    if (es_entero_positivo(num)) {
        if (anno_en_rango(num)) {
            if (num % 4 == 0) {
                if (num % 100 == 0) {
                    if (num % 400 == 0) {
                        return true;
                    }
                    return false;
                }
                return true;
            }
            return false;
        }
        console.log(generar_error('rango_anno'));
        return false
    } else {
        console.log(generar_error('año_entero_positivo'));
        return false;
    }
}

//E: número entero positivo
//S: boolean
//D: Función que valida si un año se encuentra dentro del rango válifo según el calendario gregoriano
function anno_en_rango(num) {
    return fecha_min[0] <= num && num <= fecha_max[0];
}


// --------------------------------------- 2.fecha_es_valida -----------------------------------------------

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
                if (dia >= 1 && dia <= dias_del_mes) {
                    if (fecha_en_rango(fecha))
                        return true;
                    else {
                        generar_error('rango_fecha');
                        return false;
                    }
                } else {
                    console.log(generar_error('rango_dia'));
                    return false;
                }
            } else {
                console.log(generar_error('rango_mes'));
                return false;
            }
        } else {
            console.log(generar_error('rango_anno'));
            return false;
        }
    } else {
        return false;
    }
}


//E:fecha en formato de tupla
//S: boolean
//D: Función que valida si la fecha ingresada se encuentra dentro de los rangos del calendario gregoriano
function fecha_en_rango(fecha) {
    let anno = fecha[0];
    let mes = fecha[1];
    let dia = fecha[2];
    if (anno == fecha_min[0] && mes == fecha_min[1] && dia == fecha_min[2])
        return false;
    else if (anno == fecha_min[0] && mes <= fecha_min[1])
        return false;
    else if (anno >= fecha_min[0] && anno <= fecha_max[0])
        return true;
}


//E: Una tupla que representa una fecha
//S: Una tupla que representa una fecha
//D: Ingresado una fecha, retorna la siguiente fecha válida
function dia_siguiente(fecha) {
    let dia = fecha[2];
    let mes = fecha[1];
    let anno = fecha[0];
    let es_bisiesto = bisiesto(anno) ? 1 : 0;
    if (fecha_es_valida(fecha)) {
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

// ----------------------------------- 4.dias_desde_primero_enero ------------------------------------------

//E: fecha en formato de tupla
//S: número entero positivo
//D: Función que dada una fecha válida deberá determinar el número entero de días transcurridos
//             desde el primero de enero del año ingresado hasta el día de la fecha dada.
function dias_desde_primero_enero(fecha) {
    if (fecha_es_valida(fecha)) {
        let anno = fecha[0];
        let mes = fecha[1] - 1;
        let dia = fecha[2];
        es_bisiesto = bisiesto(anno) ? 1 : 0;

        res = 0;
        for (let i = 0; i < dias_mes.length; i++) {
            d = dias_mes[i]
            if (typeof (dias_mes[i]) != 'number') {
                d = dias_mes[i][es_bisiesto];
            }
            if (i == mes) {
                res += dia - 1;
                return res;
            } else {
                res += d;
            }
        }
        return res;

    } else {
        return 0;
    }
}

// ----------------------------------- 5.dia_primero_enero ------------------------------------------


//E: Un numero entero entre 1582 y 9999
//S: Un numero
//D: Ingresado un número, el sistema determinará y retornará en formato codificado un número entero conforme al día de la semana que corresponde al primero de enero del año ingresado. 
function dia_primero_enero(anno) {
    let c = Math.trunc((anno - 1) / 100);
    let g = anno - 1 - (100 * c);
    let n = Math.trunc((g / 4));
    if (es_entero_positivo(anno)) {
        if (anno_en_rango(anno)) {
            return (1 + 0 + f_g[c % 4] + g + (n)) % 7;
        }
        console.log(generar_error('rango_anno'));
        return false;
    }
    console.log(generar_error('año_entero_positivo'));
    return false;
}


// ----------------------------------- 6.imprimir_4x3 ------------------------------------------

//E: Un numero entero entre 1582 y 9999
//S: Un booleano. Imprimer en consola si el booleano es positivo.
//D: Ingresado un año se imprime en consola el calendario correspondiente en formato 4x3. 

function imprimir_4x3(anno) {
    console.log('Calendario del año ' + anno + ' D.C.')
    console.log(' ')
    if (es_entero_positivo(anno)) {
        if (anno_en_rango(anno)) {
            let res = calendario(anno);
            let orden = Array(8)
            for (let j = 0; j < 8; j++) {
                let linea = '';
                let c = 0;
                orden[j] = [];
                for (let i = 0; i < 12; i++) {
                    linea += res[i][j];
                    if ((i + 1) % 3 == 0) {
                        orden[j][c] = linea;
                        linea = '';
                        c++;
                    }
                }
            }
            for (let n = 0; n < 4; n++) {
                for (let i = 0; i < 8; i++) {
                    console.log(orden[i][n])
                }
                console.log(' ')
            }
            return true
        }
        return false;
    }
}

//E: Un numero entero entre 1582 y 9999
//S: Retorna una matriz
//D: Ingresado un año retorna en formato de matriz el calendario correspondiente. 
function calendario(anno) {
    let calendario = [];
    let bis = bisiesto(anno) ? 1 : 0;
    let dia_inicio = dia_primero_enero(anno);
    for (let i = 0; i < 12; i++) {
        let res = imprimirMes(dia_inicio, i, bis);
        calendario[i] = res[0];
        dia_inicio = res[1] + 1;
    }
    return calendario;
}

//E: Día de inicio, mes, un booleano.
//S: Retorna una tupla con el mes del año en formato de matriz y el ultimo día del mes.
//D: Funcion que genera la matriz de un mes del año.
function imprimirMes(inicio, mes, bis) {
    let matriz = [];
    matriz[0] = nombre_mes(mes);
    matriz[1] = dias_calendario;
    let cont = 1;
    let final;
    let max = mes == 1 ? dias_mes[1][bis] : dias_mes[mes];
    for (let i = 2; i < 8; i++) {
        linea = i != 2 ? '' : '   '.repeat(inicio);
        for (let dia = inicio; dia < 7; dia++) {
            if (cont <= max) {
                if (cont == max) {
                    final = dia;
                };
                linea += (cont < 10) ? '  ' : ' ';
                linea += cont++;
            }
        }
        if (cont > max) {
            matriz[i] = linea + ' '.repeat(22 - linea.length) + '|';
        } else {
            matriz[i] = linea + ' |';
        }
        inicio = 0;
    }
    return [matriz, final];
}

//E: Un numero.
//S: Una lista de string.
//D: Funcion que genera la primera linea de un mes (nombre ).
function nombre_mes(mes) {
    let m_l = meses[mes].length;
    let linea = ' '.repeat(11 - Math.floor(m_l / 2)) + meses[mes];
    linea = linea + ' '.repeat(22 - linea.length) + '|';
    return linea;
}

// ----------------------------------- 7. dia_semana ------------------------------------------

function dia_semana(fecha) {
    let anno = fecha[0];
    let mes = fecha[1];
    let dia = fecha[2];
    if (mes < 3) {
        mes += 12;
        anno -= 1;
    }
    let res = (dia + Math.floor((13 * (mes + 1)) / 5) + anno + Math.floor(anno / 4) - Math.floor(anno / 100) + Math.floor(anno / 400)) % 7;
    if (res == 0) {
        res == 6;
    } else {
        res -= 1;
    }
    return res;
}


// ------------------------------------- impresión de errores --------------------------------------------

//E: string (representa el tipo de error por imprimir)
//S: void / Impresión del error
//D: Función específica para generar errores (consideraciones de diseño tomadas).
function generar_error(tipo) {
    switch (tipo) {
        case 'no_es_tupla':
            return 'ERROR: La fecha ingresada debe estar en formato de tupla.';
        case 'tamano_tupla':
            return 'ERROR: La tupla debe estar compuesta por 3 números enteros positivos.';
        case 'entero_positivo':
            return 'ERROR: La tupla debe estar compuesta por números enteros positivos.';
        case 'fecha_desordenada':
            return 'ERROR: La fecha debe venir en el orden año, mes, día.';
        case 'tupla_invalida':
            return 'ERROR: El formato de la tupla ingresada es inválido.';
        case 'formato_anno':
            return 'ERROR: El año debe estar compuesto por 4 dígitos.';
        case 'formato_mes_dia':
            return 'ERROR: El mes y el día deben estar compuestos por 1 o 2 dígitos.';
        case 'rango_anno':
            return 'ERROR: El año no se encuentra dentro del rango válido por el calendario gregoriano.';
        case 'rango_mes':
            return 'ERROR: El mes no se encuentra dentro del rango válido por el calendario gregoriano.';
        case 'rango_dia':
            return 'ERROR: El día no se encuentra dentro del rango válido por el calendario gregoriano.';
        case 'fecha_invalida':
            return 'ERROR: La fecha ingresada es inválida.';
        case 'fecha_posterior':
            return 'ERROR: La fecha ingresada es posterior a la fecha actual.';
        case 'año_entero_positivo':
            return 'ERROR: El año debe ser un número entero positivo.';
        case 'rango_fecha':
            return 'ERROR: La fecha ingresada no se encuentra dentro del rango válido por el calendario gregoriano';
    }

}

console.log(dia_semana([2021, 1, 1]))