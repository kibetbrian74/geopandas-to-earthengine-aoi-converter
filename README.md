# Geopandas to Earth Engine AOI Converter

A Python utility for converting shapefile-based Areas of Interest (AOIs) into **Google Earth Engine (GEE) FeatureCollections**. This tool handles geometry cleaning, 2D conversion, merging polygons, and provides an interactive web map visualization using **Geemap**.

---

## Features

- Read AOI shapefiles with **GeoPandas**
- Remove Z-dimensions from geometries for GEE compatibility
- Merge multiple polygons into a single AOI
- Convert shapefiles to GEE **FeatureCollection**
- Interactive visualization with **Geemap**
- Export map to HTML for browser viewing

---

## Requirements

- Python 3.10+
- [GeoPandas](https://geopandas.org/)
- [Shapely](https://shapely.readthedocs.io/)
- [Earth Engine Python API](https://developers.google.com/earth-engine/python_install)
- [Geemap](https://geemap.org/)

Install dependencies with:

```bash
pip install geopandas shapely earthengine-api geemap
```

## **Usage**

1. Clone the repository:

```bash
git clone https://github.com/kibetbrian74/geopandas-to-earthengine-aoi-converter.git
cd geopandas-to-earthengine-aoi-converter
```

2. Run the script:

```bash
python gpd_to_gee_featureCollection.py
```

3. Follow prompts:

- Enter the path to your AOI shapefile
- Enter the folder to save the interactive HTML map
- Open the exported HTML file in your browser to view your AOI.

This generates `output/aoi_map.html` containing an interactive map of your AOI

# Author

**Brian Cheruiyot**

Email: bkibetcheuiyot@gmail.com
