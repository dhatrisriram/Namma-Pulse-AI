from sklearn.cluster import DBSCAN
import pandas as pd
import folium

# Load the dataset
ride_data = pd.read_csv("Updated_Bangalore_Wards.csv")

# Apply DBSCAN clustering
demand_locations = ride_data[['latitude', 'longitude']].dropna().values
clustering = DBSCAN(eps=0.005, min_samples=3).fit(demand_locations)

# Add cluster labels back to the DataFrame (only for rows with lat/lon)
ride_data.loc[ride_data['latitude'].notna(), 'cluster'] = clustering.labels_

# Initialize a map centered around Bangalore
surge_map = folium.Map(location=[12.9716, 77.5946], zoom_start=12)

# Add markers for ride requests with surge zones highlighted
for _, row in ride_data.iterrows():
    color = "red" if row.get("cluster") != -1 else "blue"  # Red for demand zones, blue for normal
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=f"Ward: {row['Ward']} | Cluster: {row.get('cluster', 'N/A')}",
        icon=folium.Icon(color=color)
    ).add_to(surge_map)

# Save and display the map
surge_map.save("surge_map.html")
print("Surge map saved as surge_map.html")
