import sympy
import math

def calcula_parametros(x1, y1, x2, y2, ri, d_arcos):
    '''
    Inputs: x1, y1, x2, y2, ri, d_arcos
    Incógnitas/Outputs: cxe, cye, cxi, cyi, ri
    eq1 = Circunferencia externa pasa por punto 1
    eq2 = Circunferencia externa pasa por punto 2
    eq3 = Circunferencia interna pasa por punto 1
    eq4 = Circunferencia interna pasa por punto 2
    eq5 = Distancia entre los arcos (aunque supone que están alineados los centros)
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
    inputs: d_arcos: distáncia entre los arcos
            profundidad: profundidad donde deben cortarse los arcos
            
    outputs: angulo_externo: ángulo de corte para la sección más externa
             angulo_interno: ángulo de corte para la sección más interna (+ cercana centro ojo)
    '''
    angulo_externo = math.degrees(math.atan(profundidad/(d_arcos*0.5)))
    angulo_interno = 180 - angulo_externo
    return angulo_externo, angulo_interno