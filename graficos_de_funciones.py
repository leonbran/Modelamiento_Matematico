import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,2*np.pi,0.1)
y = np.sin(x)

#graficando
plt.plot(x,y)

#nombres de los ejes
plt.xlabel('x')
plt.ylabel('y')


#nombres de los ejes
plt.title('Grafico de y=sin(x)')
 
#mostrando el grafico
plt.show()