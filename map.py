from __future__ import unicode_literals

from pyecharts import Map
# from echarts_united_kingdom_pypkg import NM_WESTMINSTER_2016_UK

from csv import reader
from pyecharts import Map

with open('data.csv', 'r') as f:
    data = list(reader(f))
    f.close()

# print(data)

label = [i[0] for i in data[1:]]
population = [float(i[1]) for i in data[1:]]
area = [float(i[2]) for i in data[1:]]
density = [round(population[i]/area[i], 2) for i in range(0, len(label[:-1]))]
densityPercentage = [round(i/sum(density)*100, 2) for i in density]
populationPercent = [round(population[i]/sum(population[:-1])*100, 2) for i in range(0, len(population[:-1]))]

value = density
attr = label[:-1]
map = Map('Canada Map of Population Density of Provinces (ppl/km2)', width=800, height=600)
map.add(
    "",
    attr,
    value,
    maptype="加拿大",
    is_visualmap=True,
    visual_text_color="#000",
    visual_range=[0, max(density)]
#     name_map=NM_WESTMINSTER_2016_UK,
)
map.render()
