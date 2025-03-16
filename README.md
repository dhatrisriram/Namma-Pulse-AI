# Namma-Surge
🚀 Predictive Surge Forecasting System

## 📌 Project Overview
The **Predictive Surge Forecasting System** helps **Namma Yatri** proactively predict **hyperlocal ride demand surges** 30-60 minutes in advance. Using **Google's Temporal Fusion Transformer (TFT)** for time-series forecasting and **Graph Neural Networks (GNNs)** for spatial demand patterns, it enables **optimized driver repositioning** using the **Hungarian algorithm** while analyzing zone connectivity with a **Traffic Connectivity Matrix**.

---

🚦 **How does it address the problem effectively?**
- **Proactive Driver Repositioning:** Predicts surges 30-60 minutes in advance, allowing the platform to reposition drivers ahead of time.
- **Real-Time Insights:** Integrates traffic, weather, and event data to provide a holistic view of demand influencers.
- **Reduced Ride Denials:** Matches supply to predicted demand hotspots, minimizing unfulfilled requests and wait times.
- **Data-Driven Decision-Making:** Provides actionable insights through a heatmap dashboard and automated alerts.

---


🌟 **Unique Aspects or Differentiators:**
- **Hyperlocal Predictions:** Micro-zone granularity (500m-1km) ensures highly localized forecasts.
- **Hybrid Model Architecture:** Combines LSTM/GRU for temporal patterns, Transformers for long-range dependencies, and GNNs for spatial understanding.
- **Transfer Learning:** Speeds up development by leveraging data from similar cities, with fine-tuning for Namma Yatri’s unique environment.
- **Visualization Focus:** A user-friendly dashboard with confidence intervals and automated alerts ensures interpretability and quick action.

---

## 🏗️ Tech Stack
### **Data Processing & Integration**
- **Python (Pandas)** – For lightweight data cleaning, manipulation, and analytics.
- **HereMaps API** – For real-time traffic and geospatial data.
- **OpenWeather API** – For weather data integration (rain forecasts).
- **PredictHQ API** – For event data (concerts, sports, etc.).
- **Traffic Connectivity Matrix** – Analyzing real-time zone accessibility.  
- **H3 (Hexagonal Grids)** – Spatial division of the city.  
- **DBSCAN (Scikit-learn)** – Identifying demand hotspots.  

### **Machine Learning & Optimization**
- **Google Temporal Fusion Transformer (TFT)** – Multi-horizon time-series forecasting.  
- **Graph Neural Networks (GNNs)** – Capturing spatial demand patterns.  
- **Hungarian Algorithm** – Optimized driver repositioning.   

### **Visualization & Alerting**
- **Streamlit** – Real-time interactive dashboard.  
- **Leaflet.js (Streamlit Plugin)** – Surge heatmaps and geospatial visualization.  
- **Twilio** – Automated SMS/WhatsApp alerts for predicted demand surges.  

---

## 📊 Features
✅ Predict **demand surges** with **30-60 min lead time**.  
✅ **Optimize driver repositioning** using the **Hungarian algorithm**.  
✅ Use **real-time traffic & weather data** for improved predictions.  
✅ **Dynamic micro-zones (H3 grid)** for demand pattern analysis.  
✅ **Interactive dashboard** to visualize predicted surge areas.  
✅ **Automated alerts (Twilio)** for extreme demand spikes.  
