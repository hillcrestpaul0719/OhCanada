# https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/graphing/
from csv import reader
# from matplotlib import pyplot
# import matplotlib.pyplot as plt
# import numpy as np
from pyecharts import Pie
from pyecharts import Bar

with open('data.csv', 'r') as f:
    data = list(reader(f))
    f.close()

# print(data)

label = [i[0] for i in data[1:]]
population = [float(i[1]) for i in data[1:]]
area = [float(i[2]) for i in data[1:]]
density = [population[i]/area[i] for i in range(0, len(label))]
populationPercent = [round(population[i]/sum(population[:-1])*100, 2) for i in range(0, len(population[:-1]))]

# print([(labels[i], density[i]) for i in range(0, len(density))])

bar = Bar("Population distribution of Canada! (By %)")
bar.add("", label[:-1], populationPercent, is_convert=True)
bar.render()
