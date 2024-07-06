from scipy.optimize import *
import numpy as np
import matplotlib.pyplot as plt

a = 1
b = 0.01  # Постоянные для функций спроса и предложения


def fun_1(x, a):  # Функция спроса
    return np.e**(-a*x**2)


def fun_2(x, b):  # Функция предложения
    return b*x**2


x0 = round(fsolve(lambda x: fun_1(x, a)-fun_2(x, b), 1)
           [0], 3)  # Равновесная цена
x = np.arange(0, x0+1, 0.01)
plt.figure()
plt.title('Паутинообразная модель динамики цен и объёмов производства', size=12)
plt.xlabel('Цена товара', size=12)
plt.plot(x, fun_1(x, a), 'r', linestyle='--',
         linewidth=1, label='Функция спроса')
plt.plot(x, fun_2(x, b), 'b', linestyle='-',
         linewidth=1, label='Функция предложения ')
plt.plot(x0, fun_2(x0, b), marker='o',  markersize=6,
         markerfacecolor='g', label='Равновесное производство ')
plt.plot(x0, 0, marker='s',  markersize=6,
         markerfacecolor='r', label='Равновесная цена товара ')
plt.legend(loc='best')
plt.grid(True)
q = []
p = []
x = []
q.append(0.6)
p.append(round(fsolve(lambda x: fun_1(x, a)-q[0], 1)[0], 3))
for i in np.arange(0, 7):
    x.append(i)
    if i != 0:
        q.append(fun_2(p[i-1], b))
        p.append(round(fsolve(lambda x: fun_1(x, a)-q[i], 1)[0], 3))
plt.figure()
plt.title('Колебания цены и объёмов производства ', size=12)
plt.xlabel('Период времени', size=12)
plt.plot(x, p, 'r', marker='s',  markersize=6,
         markerfacecolor='r', label='Колебания цены')
plt.plot(x, q, 'b', marker='o',  markersize=6,  markerfacecolor='b',
         label='Колебания объёмов производства')
plt.legend(loc='best')
plt.grid(True)
plt.show()
