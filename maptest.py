#coding=utf-8
from __future__ import unicode_literals

from pyecharts import Map
# from echarts_canada_pypkg import NM_WESTMINSTER_2016_UK

value = []
attr = []
map = Map('United Kingdom', width=800, height=600)
map.add(
    "",
    attr,
    value,
    maptype="加拿大",
    is_visualmap=True,
    visual_text_color="#000",
#     name_map=NM_WESTMINSTER_2016_UK,
)
map.render()
