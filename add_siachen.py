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

    # just add siachen geomtry to this
    siachen_src['ST_NM'] = 'Ladakh'
    siachen_src['DISTRICT'] = 'Siachen'
    siachen_src['ST_CEN_CD'] = None
    siachen_src['DT_CEN_CD'] = None
    siachen_src['censuscode'] = None

    # insert the siachen polygon
    kashmir_ladakh_src = geopandas.GeoDataFrame(
        pandas.concat(
            [kashmir_ladakh_src, siachen_src], ignore_index=True
        )
    )

    # now delete the siachen polygon from POK

    import ipdb
    ipdb.set_trace()

    kashmir_src = kashmir_ladakh_src[kashmir_ladakh_src.ST_NM.str.contains(
        'jammu', case=False)]
    ladakh_src = kashmir_ladakh_src[kashmir_ladakh_src.ST_NM.str.contains(
        'ladakh', case=False)]

    kashmir_geometries = kashmir_src['geometry']
    ladakh_geometries = ladakh_src['geometry']

    # new ladakh src with siachen


if __name__ == '__main__':
    kashmir_ladakh_dist = sys.argv[1]
    siachen = sys.argv[2]

    siachen_polygon(siachen, kashmir_ladakh_dist)
