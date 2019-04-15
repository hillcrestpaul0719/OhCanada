# https://www.raspberrypi.org/learning/astro-pi-flight-data-analysis/graphing/
from csv import reader
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
from pyecharts import Pie

with open('data.csv', 'r') as f:
    data = list(reader(f))
    f.close()

# print(data)

labels = [i[0] for i in data[1:]]
population = [float(i[1]) for i in data[1:]]
area = [float(i[2]) for i in data[1:]]
density = [population[i]/area[i] for i in range(0, len(labels))]

print([(labels[i], density[i]) for i in range(0, len(density))])

# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
#
#
#
#
# sizes = population
#
# explode = []
# for i in population[:-1]:
#     # if i/population[-1] < 0.05:
#     #     explode.append(0.5)
#     # else:
#     #     explode.append(0)
#     explode.append(0)
#
# fig1, ax1 = plt.subplots()
# ax1.pie(density[:-1], explode=explode, labels=labels[:-1], autopct='%1.1f%%',
#         shadow=False, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()

# fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
#
# recipe = labels
#
# data = density
#
# print(density)
# print(sum(density))
# densityPercentage = [round(i/sum(density)*100, 2) for i in density]
#
# wedges, texts = ax.pie(data, wedgeprops=dict(width=0.5), startangle=-40)
#
# bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
# kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
#           bbox=bbox_props, zorder=0, va="center")
#
# for i, p in enumerate(wedges):
#     ang = (p.theta2 - p.theta1)/2. + p.theta1
#     y = np.sin(np.deg2rad(ang))
#     x = np.cos(np.deg2rad(ang))
#     horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
#     connectionstyle = "angle,angleA=0,angleB={}".format(ang)
#     kw["arrowprops"].update({"connectionstyle": connectionstyle})
#     print(densityPercentage[i])
#     print("{0}% {1}".format(densityPercentage[i], recipe[i]))
#     ax.annotate("{0}% {1}".format(densityPercentage[i], recipe[i]), xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
#     horizontalalignment=horizontalalignment, **kw)
#
# ax.set_title("Matplotlib bakery: A donut")
#
# plt.show()



pie = Pie("Population density of Canada!")
pie.add("", labels, density, is_label_show=False, is_legend_show=False)
pie.render()
