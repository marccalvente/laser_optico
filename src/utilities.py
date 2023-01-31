import sympy
import numpy as np
import math
import matplotlib.pyplot as plt

def calcula_parametros(x1, y1, x2, y2, ri, d_arcos):
    '''
    Inputs: 
        Punto: (x1, y1)
        Punto: (x2, y2) 
        Radiio circunferencia interna: ri
        Distáncia entre los arcos: d_arcos

    Incógnitas/Outputs: 
        Centro circunferencia externa: (cxe, cye)
        Centro circunferencia interna: (cxi, cyi)
        Radio circunferencia externa: re

    eq1 = Circunferencia externa pasa por punto 1
    eq2 = Circunferencia externa pasa por punto 2
    eq3 = Circunferencia interna pasa por punto 1
    eq4 = Circunferencia interna pasa por punto 2
    eq5 = Distancia entre los arcos (aunque supone que están alineados los centros)

    Resuelve el sistema de ecuaciones cuadráticas siguiente para devolver los outputs necesarios para plottear las circunferencias.
    '''
    cxe, cye, cxi, cyi, re = sympy.symbols("cxe cye cxi cyi re", real=True)

    eq1 = sympy.Eq((x1 - cxe)**2 + (y1 - cye)**2 -(re**2), 0)
    eq2 = sympy.Eq((x2 - cxe)**2 + (y2 - cye)**2 -(re**2), 0)

    eq3 = sympy.Eq((x1 - cxi)**2 + (y1 - cyi)**2 -(ri**2), 0)
    eq4 = sympy.Eq((x2 - cxi)**2 + (y2 - cyi)**2 -(ri**2), 0)

    eq5 = sympy.Eq(re - ri + sympy.sqrt((cxe-cxi)**2+(cye-cyi)**2) - d_arcos, 0)

    result = sympy.solve([eq1, eq2, eq3, eq4, eq5])
    
    cxe = float(result[1][cxe].evalf())
    cye = float(result[1][cye].evalf())
    cxi = float(result[1][cxi].evalf())
    cyi = float(result[1][cyi].evalf())
    re = float(result[1][re].evalf())
    
#     cxe = float(result[0][cxe].evalf())
#     cye = float(result[0][cye].evalf())
#     cxi = float(result[0][cxi].evalf())
#     cyi = float(result[0][cyi].evalf())
#     re = float(result[0][re].evalf())
       
    return cxe, cye, cxi, cyi, re


def calcula_angulo(d_arcos, profundidad):
    '''
    inputs: 
        d_arcos: distáncia entre los arcos
        profundidad: profundidad donde deben cortarse los arcos
            
    outputs: 
        ángulo_externo: ángulo de corte para la sección más externa
        ángulo_interno: ángulo de corte para la sección más interna (+ cercana centro ojo)
    '''
    angulo_externo = math.degrees(math.atan(profundidad/(d_arcos*0.5)))
    angulo_interno = 180 - angulo_externo

    return angulo_externo, angulo_interno


def genera_grafico(x1, y1, x2, y2, cxe, cye, re, cxi, cyi, ri):
    '''
    inputs: 
        Dos puntos en el espacio (x1, y1), (x2, y2)
        Centro de la circunferencia externa (cxe, cye) y su radio re
        Centro de la circunferencia interna (cxi, cyi) y su radio ri

    output: fig: una figura de matplotlib que tiene ploteados los puntos (x1, y1), (x2, y2), la circunferencia externa, la circunferencia interna
                 y la circunferencia de una córnea humana estándar
    '''
    plt.ioff()
    fig, ax =  plt.subplots()
    cm = 1/2.54 #Para convertir el tamaño
    fig.set_size_inches(20*cm, 20*cm)
    
    radio_cornea = 12/2 #Tamaños estándar humanos en mm (radio)

    cornea = plt.Circle((0, 0), radio_cornea, color='turquoise', fill=False)
    corte_externo = plt.Circle((cxe, cye), re, color='red', fill=False, linewidth=0.2)
    corte_interno = plt.Circle((cxi, cyi), ri, color='red', fill=False, linewidth=0.2)

    ax.cla() # clear things for fresh plot

    ax.set_aspect('equal') # Para que el gráfico sea cuadrado

    # Cambiar el límite que se muestra
    ax.set_xlim((-7, 7))
    ax.set_ylim((-7, 7))

    # Plot puntos
    ax.plot((x1), (y1), 'o', color='coral')
    ax.plot((x2), (y2), 'o', color='coral')

    # Plot ejes
    plt.axvline(x = 0, color = 'k', linewidth=0.5)
    plt.axhline(y = 0, color = 'k', linewidth=0.5)

    # Plot los círculos
    ax.add_patch(cornea)
    ax.add_patch(corte_externo)
    ax.add_patch(corte_interno)
    
    return fig


def calcula_longitud_arco(x1, y1, x2, y2, cx, cy):
    '''
    inputs: 
        Punto 1: x2, y1
        Punto 2: x2, y2
        Centro: cx, cy

    outputs: angulo en grados

    Calcula el ángulo que forman dos puntos respecto a un centro.
    '''
    P1 = [x1, y1]
    P2 = [x2, y2]
    C = [cx, cy]

    angulo = 2*math.asin(math.dist(P1,P2)*0.5/(math.dist(C,P1)))

    return math.degrees(angulo)

    
def calcula_angulo_con_horizontal(x, y, cx, cy):
    '''
    input: 
        coordenadas cartesianas(x, y)
        centro de coordenadas (cx, cy)
    output: ángulo que forma con la horizontal en grados (º)

    Calcula el ángulo que forma la coordenada cartesiana con la horizontal (con el 0 situado a las 9h, a la izquierda)
    '''
    phi = np.arctan2(y-cy, x-cx)
    angulo_grados = math.degrees(phi)
    angulo_resultado = (angulo_grados+180)%360
    return angulo_resultado
