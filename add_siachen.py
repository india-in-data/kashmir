'''
Adds the Siachen polygon to Ladakh.
Subtracts it from Gilgit
'''

import pandas
import geopandas
import shapely
import sys


def siachen_polygon(siachen_f, kashmir_ladakh_f):
    siachen_src = geopandas.read_file(siachen_f)
    kashmir_ladakh_src = geopandas.read_file(kashmir_ladakh_f)

    # union with ladakh district
    # siachen_src['ST_NM'] = 'Ladakh'
    # siachen_src['DISTRICT'] = 'Siachen'
    # siachen_src['ST_CEN_CD'] = None
    # siachen_src['DT_CEN_CD'] = None
    # siachen_src['censuscode'] = None

    siachen_geometry = siachen_src['geometry'][0]
    leh_geometry = siachen_geometry

    # insert the siachen polygon
    for i, row in kashmir_ladakh_src[kashmir_ladakh_src.district.str.contains(
            'leh', case=False)].iterrows():
        leh_geometry = row['geometry'].union(
            siachen_geometry)
        leh_geometry = shapely.geometry.Polygon(leh_geometry.exterior)
        kashmir_ladakh_src.at[i, 'geometry'] = leh_geometry

    kashmir_ladakh_src.to_file('kashmir_ladakh_siachen.json', driver='GeoJSON')

    for i, row in kashmir_ladakh_src[kashmir_ladakh_src.st_nm.str.contains(
            'jammu', case=False)].iterrows():
        kashmir_ladakh_src.at[i, 'geometry'] = row['geometry'].difference(
            leh_geometry)

    kashmir_ladakh_src.to_file('kashmir_ladakh_siachen.json', driver='GeoJSON')


if __name__ == '__main__':
    kashmir_ladakh_dist = sys.argv[1]
    siachen = sys.argv[2]

    siachen_polygon(siachen, kashmir_ladakh_dist)
