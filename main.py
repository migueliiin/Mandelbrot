import numpy as np
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

def mandelbrot(re, im, max_iter):
    c = complex(re, im)
    z = 0.0j
    for i in range(max_iter):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 4:
            return i
    return max_iter

columnas = 5000
filas = 5000

result = np.zeros([columnas, filas])

for row_index, re in enumerate(linspace(-2, 1, num=columnas)):
    for column_index, im in enumerate(linspace(-1, 1, num=filas)):
        result[row_index, column_index] = mandelbrot(re, im, 100)

plt.figure(dpi=100)
plt.imshow(result.T, cmap="viridis", extent=[-2, 1, -1, 1])
plt.show()
    
