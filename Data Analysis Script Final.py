import numpy as np
import rasterio
from scipy.ndimage import median_filter
import matplotlib.pyplot as plt
 
# --- CONFIGURATION PARAMETERS ---
DEFORMATION_THRESHOLD_MM = 10  # mm of ground movement in observation window
CLUSTER_THRESHOLD_PIXELS = 50  # number of pixels showing large deformation to trigger alert
PIXEL_AREA_M2 = 100  # assuming each pixel is 10m x 10m (adjust as needed)
RISK_ZONE_MASK_PATH = "risk_zones_mask.tif"  # binary mask of known seismic zones
 
# --- HELPER FUNCTION TO LOAD GEOTIFF DATA ---
def load_geotiff(path):
    with rasterio.open(path) as src:
        data = src.read(1)  # Read first band
        profile = src.profile
    return data, profile
 
# --- MAIN EARTHQUAKE PREDICTION FUNCTION ---
def detect_seismic_risk(before_path, after_path, mask_path=RISK_ZONE_MASK_PATH):
    # Load before and after deformation data (in mm)
    disp_before, _ = load_geotiff(before_path)
    disp_after, _ = load_geotiff(after_path)
    # Compute delta displacement
    delta = disp_after - disp_before
    # Denoise with median filter
    delta_filtered = median_filter(delta, size=3)
    # Load seismic risk zone mask (1 inside zone, 0 outside)
    mask, _ = load_geotiff(mask_path)
    # Apply threshold to detect abnormal displacement
    deformation_mask = np.abs(delta_filtered) > DEFORMATION_THRESHOLD_MM
    risk_area_mask = deformation_mask & (mask == 1)
    # Count number of "risky" pixels
    risky_pixels = np.sum(risk_area_mask)
    risky_area_m2 = risky_pixels * PIXEL_AREA_M2
    # Determine if alert should be triggered
    alert_triggered = risky_pixels > CLUSTER_THRESHOLD_PIXELS
 
    print(f"Displacement threshold exceeded in {risky_pixels} pixels (~{risky_area_m2} m²)")
    if alert_triggered:
        print("🚨 EARTHQUAKE RISK ALERT TRIGGERED 🚨")
        return {
            "alert": True,
            "risky_pixels": risky_pixels,
            "risky_area_m2": risky_area_m2,
        }
    else:
        print("✅ No significant deformation detected.")
        return {
            "alert": False,
            "risky_pixels": risky_pixels,
            "risky_area_m2": risky_area_m2,
        }
 
# --- EXAMPLE USAGE ---
if __name__ == "__main__":
    # Paths to InSAR displacement GeoTIFFs (in mm) – get from SNAP or Earth Engine
    before_image = "data/displacement_2025_03_01.tif"
    after_image = "data/displacement_2025_03_18.tif"
    results = detect_seismic_risk(before_image, after_image)
