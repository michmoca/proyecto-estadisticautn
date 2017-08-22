from scipy.stats import t
from scipy.stats import chi2
from scipy.stats import binom
from scipy.special import ndtri
from scipy.stats import poisson as calcular_poisson
from scipy.stats import mode
import math
import numpy as np

def calcular_chi_cuadrado_buscar_tabla(n, std, varianza_muestra, valor_tabla = None):
    valor_tabla = ((n-1) * varianza_muestra) / math.pow(std,2)
    resultado = chi2.sf(valor_tabla, (n-1))
    resultado = format(resultado, '.3f')
    return resultado

def calcular_prueba_hipotesis_diferencia_medias(promedio1, promedio2, media1, media2, std1, std2, n1, n2):
    resultado = ((promedio1 - promedio2) - (media1 - media2)) / math.sqrt( (math.pow(std1,2)/n1) + (math.pow(std2,2)/n2))
    resultado = format(resultado, '.3f')
    return resultado

#P es el porcentaje mayor
#p es el porcentaje menor
def calcular_prueba_hipotesis_proporcion(P, p, n):
    q = 1 - P
    resultado = (p-P) / math.sqrt(((P*q)/n))
    resultado = format(resultado, '.3f')
    return resultado

def calcular_prueba_hipotesis_media(promedio, media, std, n):
    resultado = (promedio - media) / (std / math.sqrt(n))
    resultado = format(resultado, '.3f')
    return resultado

def calcular_z_alfa(alfa):
    '''esta funcion calcula y retorna el valor de Z recibiendo alfa de parametro'''
    valor_tabla = 1 - (alfa / 2)
    z = ndtri(valor_tabla)
    z = format(z, '.3f')
    return z


def descriptiva_info(lista):
    lista= lista.split(',')
    lista_np = np.array(lista)
    lista_np = lista_np.astype(float)
    mediana = np.median(lista_np)
    media = np.mean(lista_np)
    moda = mode(lista_np)
    varianza = np.var(lista_np)
    desv = np.std(lista_np)
    tamano = len(lista_np)
    dict_resultados = {
                    'mediana': mediana,
                    'media': media,
                    'moda': moda.mode[0],
                    'varianza': varianza,
                    'std': desv,
                    'tamano':tamano,
                 }
    return dict_resultados

def poisson(mu, k=None, inicio=None, fin=None):
    total = 0
    if inicio:
        fin = fin + 1
        for x in range(inicio,fin):
            total+= calcular_poisson.pmf(x, mu, loc=0)
    else:
        total = calcular_poisson.pmf(k, mu, loc=0)

    total = total * 100
    total = format(total, '.2f')
    return total

def binomial(x,n,p):
    porcentaje = binom.pmf(x, n, p)
    porcentaje = porcentaje * 100
    return format(porcentaje, '.2f')


def binomial_rango(n,p, inicio, fin):
    total = 0
    fin = fin + 1

    for x in range(inicio,fin):
        total += binom.pmf(x, n, p)

    total = total * 100
    total = format(total, '.2f')
    return total

def calcular_z(confianza):
    '''esta funcion calcula y retorna el valor de Z'''
    alfa = 1 - (confianza / 100)
    valor_tabla = 1 - (alfa / 2)
    z = ndtri(valor_tabla)
    return z

def intervalo_confianza_proporcion(p, confianza, n):
    '''esta funcion calcula y retorna un string con el intervalo
    de acuerdo a los parametros recibidos'''
    #se calculan los intervalos con la suma y la resta
    z = calcular_z(confianza)
    intervalo1 = p - z * math.sqrt(p *(1-p) /n) #izquierda - resta
    intervalo2 = p + z * math.sqrt(p *(1-p) /n) #derecha + suma
    #se redondean los numeros a 2 decimales
    intervalo1 = format(intervalo1, '.2f')
    intervalo2 = format(intervalo2, '.2f')
    #se da formato al string antes y se retorna
    return ("[{} - {}]".format(intervalo1, intervalo2))

def intervalo_confianza_media(n, std, x, confianza):
    z = calcular_z(confianza)

    intervalo1 = x - z * (std / math.sqrt(n)) #izquierda - resta
    intervalo2 = x + z * (std / math.sqrt(n)) #derecha + suma

    intervalo1 = format(intervalo1, '.2f')
    intervalo2 = format(intervalo2, '.2f')
    #se da formato al string antes y se retorna
    return ("[{} - {}]".format(intervalo1, intervalo2))

def t_student(N, t_score1, t_score2=None ):
    '''metodo que calcula la probabilidad de "t" segun el N dado'''
    N = N - 1
    dict_resultados = {}

    if t_score2 is not None:
        print("otra funcion")
        #evaluamos casos a < t < b
        tabla_a = t.sf(t_score1, N)

        tabla_b = t.sf(t_score2, N)

        resultado = tabla_a - tabla_b
        resultado = format(resultado, '.4f')

        tabla_a = format(tabla_a, '.4f')
        tabla_b = format(tabla_b, '.4f')

        dict_resultados = {
                        'caso1' :"P({} < T < {}) = {})".format(tabla_a, tabla_b, resultado),
                     }
    else:
        tabla = t.sf(t_score1, N)
        caso1 = 1 - tabla
        caso1 = format(caso1, '.4f')
        caso2 = format(tabla, '.4f')
        caso3 = 0.5

        dict_resultados = {
                        'caso1' :"P(T<={}) = {}".format(t_score1, caso1),
                        'caso2' :"P(T >= {}) = {}".format(t_score1, caso2),
                        'caso3' :"P(T = 0) = {}".format(caso3),
                     }

    return dict_resultados
