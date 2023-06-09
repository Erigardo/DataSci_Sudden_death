import numpy as np


def act(x):
    return 0 if x < 0.5 else 1


def go(young, ill, sport):
    x = np.array([young, ill, sport])
    w11 = [0.3, 0.3, 0]
    w12 = [0.4, -0.5, 1]
    weight1 = np.array([w11, w12])  # матрица 2x3
    weight2 = np.array([-1, 1])  # вектор 1х2

    sum_hidden = np.dot(weight1, x)  # вычисляем сумму на входах нейронов скрытого слоя
    print("Значения сумм на нейронах скрытого слоя: " + str(sum_hidden))

    out_hidden = np.array([act(x) for x in sum_hidden])
    print("Значения на выходах нейронов скрытого слоя: " + str(out_hidden))

    sum_end = np.dot(weight2, out_hidden)
    y = act(sum_end)
    print("Выходное значение НС: " + str(y))

    return y


young = input('Вы молоды? (y/n): ').lower() == 'y'
ill = input('У вас есть хронические заболевания? (y/n): ').lower() == 'y'
sport = input('Вы занимаетесь спортом? (y/n): ').lower() == 'y'

res = go(int(young), int(ill), int(sport))
if res == 1:
    print("Здоров")
else:
    print("Высокий риск")