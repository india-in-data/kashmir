'''

'''

import geopandas
import pandas
import sys

shp_f = sys.argv[1]
dest = sys.argv[2]

src = geopandas.read_file(shp_f)

old_jk_districts = src[src['ST_NM'] == 'Jammu & Kashmir']

# new ladakh ut
ladakh_dists_strs = ['leh', 'kargil']

for dist in ladakh_dists_strs:
    locs = src.DISTRICT.str.contains(dist, case=False)
    src.loc[locs, 'ST_NM'] = 'Ladakh'
    src.loc[locs, 'ST_CEN_CD'] = None
    src.loc[locs, 'DT_CEN_CD'] = None
    src.loc[locs, 'censuscode'] = None

src.to_file(dest, driver='GeoJSON')
