import numpy as np
import rasterio
from rasterio.transform import from_origin
import os

# Create a data directory if it doesn't exist
os.makedirs("data", exist_ok=True)

# Define image dimensions and a simple spatial transform
width = height = 100
transform = from_origin(0, 100, 1, 1)  # arbitrary origin, pixel size 1x1

# Define the common profile for our GeoTIFF files
profile = {
    'driver': 'GTiff',
    'dtype': 'float32',
    'nodata': None,
    'width': width,
    'height': height,
    'count': 1,
    'crs': 'EPSG:4326',
    'transform': transform,
}

# --- Generate sample displacement data ---
# Create the "before" displacement: random small displacements around 0
disp_before = np.random.uniform(-5, 5, (height, width)).astype('float32')

# Create the "after" displacement: copy "before" then add deformation in a specific region
disp_after = disp_before.copy()
disp_after[30:60, 30:60] += 15  # simulate a deformation (15 mm increase) in a 30x30 pixel area

# Write the "before" displacement GeoTIFF
with rasterio.open("data/displacement_2025_03_01.tif", 'w', **profile) as dst:
    dst.write(disp_before, 1)

# Write the "after" displacement GeoTIFF
with rasterio.open("data/displacement_2025_03_18.tif", 'w', **profile) as dst:
    dst.write(disp_after, 1)

# --- Generate sample risk zone mask ---
# Create a binary mask: 1s in a region that represents the risk zone, 0s elsewhere
risk_mask = np.zeros((height, width), dtype='float32')
risk_mask[20:70, 20:70] = 1  # risk zone covering a large central area

# Write the risk zone mask GeoTIFF
with rasterio.open("risk_zones_mask.tif", 'w', **profile) as dst:
    dst.write(risk_mask, 1)

print("Sample GeoTIFF files have been generated:")
print("- data/displacement_2025_03_01.tif")
print("- data/displacement_2025_03_18.tif")
print("- risk_zones_mask.tif")
