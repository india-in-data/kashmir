'''
Adds the Siachen polygon to Ladakh.
Subtracts it from Gilgit
'''

import pandas
import geopandas
import shapely
import sys


def outlines_polygon(kashmir_ladakh_f):
    kashmir_ladakh_src = geopandas.read_file(kashmir_ladakh_f)

    jk = kashmir_ladakh_src[kashmir_ladakh_src.st_nm.str.contains(
        'jammu', case=False) | kashmir_ladakh_src.st_nm.str.contains(
        'ladakh', case=False)]

    jk = jk.dissolve(by='st_nm')

    jk.to_file('kashmir_ladakh_siachen_adm1.json', driver='GeoJSON')


if __name__ == '__main__':
    kashmir_ladakh_dist = sys.argv[1]

    outlines_polygon(kashmir_ladakh_dist)
