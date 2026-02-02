import geopandas as gpd
import ee
from shapely.ops import unary_union, transform
from shapely.geometry import mapping

try:
    print("ee initializing...")
    ee.Initialize(project = "ee-cheruiyotkb")
    ee.Authenticate()
    print("ee initialized!")
except Exception as e:
    print(f"error!\n{e}")

aoi_path = input("path to aoi shapefile: ")
gdf = gpd.read_file(aoi_path).to_crs(epsg=4326)
# remove the z-dimension if present
gdf['geometry'] = gdf["geometry"].apply(
    lambda geom: transform(lambda x, y, z=None: (x, y), geom)
)

merged_polygon = unary_union(gdf.geometry)

geojson = mapping(merged_polygon)

ee_geometry = ee.Geometry.Polygon(geojson["coordinates"]) if geojson['type'] == "Polygon" else\
               ee.Geometry.MultiPolygon(geojson["coordinates"])
ee_feature = ee.Feature(ee_geometry)
ee_feature_collection = ee.FeatureCollection([ee_feature])

print("FeatureCollection created!")
# plot the geometry on geemap
import geemap
map = geemap.Map()
map.add_layer_control(position="topright")
map.add_basemap("OpenStreetMap")
map.add_basemap("Esri.WorldImagery")
map.add_basemap("Esri.WorldTopoMap")
map.add_basemap("NLCD 2021 CONUS Land Cover")
map.add_basemap("Esri.WorldTerrain")
map.add_basemap("OneMapSG.Night")
map.add_basemap("Stadia.StamenTerrain")
map.centerObject(ee_feature_collection, 10)
map.addLayer(ee_feature_collection, {}, "AOI")

# save to a folder
import os
output_path = input("Path to save the map (e.g., ./output): ")
os.makedirs(output_path, exist_ok=True)
output_file = os.path.join(output_path, "aoi_map.html")
map.to_html(output_file, title="Mwea Area Map")