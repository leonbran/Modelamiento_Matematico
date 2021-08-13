import numpy as np


def divided_diff(x, y):
    '''Función para calular la tabla de 
       diferencias divididas para calcular el polinomio de Newton'''
    n = len(y)
    coef = np.zeros([n, n])
    # La primera columna es y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
           (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
                        
    return coef

def newton_poly(coef, x_data, x):
    ''' Evalua el polinomio de Newton en x'''
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p