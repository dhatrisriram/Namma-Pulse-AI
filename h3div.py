import h3
import pandas as pd

# Set resolution for 500m–1km zones
resolution = 9  # 500m; use 8 for ~1km

# Load the dataset
ride_data = pd.read_csv("Updated_Bangalore_Wards.csv")

# Apply H3 conversion to create microzones
ride_data['h3_index'] = ride_data.apply(
    lambda row: h3.latlng_to_cell(row['latitude'], row['longitude'], resolution), axis=1
)

# Count unique zones
unique_zones = ride_data['h3_index'].nunique()
print(f"Unique Microzones at Resolution {resolution}: {unique_zones}")

# Save the updated data back to the same file
ride_data.to_csv("Updated_Bangalore_Wards.csv", index=False)
print("Microzones added to Updated_Bangalore_Wards.csv!")

