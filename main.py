from function.function import *
from function.utilities import *

import matplotlib.pyplot as plt


f = Function(math.cos, label="cos")
g = Function(lambda x: x**2, label="x**2")
k = Function(math.sqrt, label="sqrt")

h = k( g ) + 5 + f

interval_point_cnt = 100
interval = [math.pi * (2*i/interval_point_cnt - 1) for i in range(interval_point_cnt) ]

interval_triple = [math.pi * (6*i/interval_point_cnt - 3) for i in range(interval_point_cnt) ]

f = Function(lambda x: x**2 if x < 0 else 1)

plt.plot(interval, [f(k) for k in interval])

part_sum = get_fourier_partial_series(f, 20)

plt.plot(interval, [part_sum(k) for k in interval])
plt.show()