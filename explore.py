import geopandas
import pandas
import sys

shp_f = sys.argv[1]
dest = sys.argv[2]

src = geopandas.read_file(shp_f)

old_jk_districts = src[src['st_nm'] == 'Jammu & Kashmir']

# new ladakh ut
ladakh_dists_strs = ['leh', 'kargil']

for dist in ladakh_dists_strs:
    locs = src.district.str.contains(dist, case=False)
    src.loc[locs, 'st_nm'] = 'Ladakh'
    src.loc[locs, 'st_cen_cd'] = None
    src.loc[locs, 'dt_cen_cd'] = None
    src.loc[locs, 'censuscode'] = None

src.to_file(dest, driver='GeoJSON')
