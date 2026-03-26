[![Disease Outbreak Banner](https://via.placeholder.com/819x460.png?text=Disease+Outbreak+Prediction+%26+Prevention)](https://github.com/KRITHIN913/Disease_Outbreak_Prediction-Prevention)

# Disease Outbreak Prediction & Prevention
[![License](https://img.shields.io/github/license/KRITHIN913/Disease_Outbreak_Prediction-Prevention?color=2185d0&style=flat-square)](LICENSE)
[![Stars](https://img.shields.io/github/stars/KRITHIN913/Disease_Outbreak_Prediction-Prevention?color=2185d0&style=flat-square)](https://github.com/KRITHIN913/Disease_Outbreak_Prediction-Prevention/stargazers)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square)](https://www.python.org/downloads/)

Established in 2024 at IIIT Nagpur.

Predictive public health modeling made simple for governments and organizations.

Robust, highly interpretable, and localized spatiotemporal forecasting framework for disease outbreaks using a hybrid machine learning approach.

## Table of Contents

* [About](#about)
* [Features](#features)
* [Get Started](#get-started)
* [Flavors](#flavors)
* [Citation](#citation)
* [References](#references)
* [Showcase](#showcase)
* [Community](#community)
* [Author and Contributors](#author-and-contributors)
* [Changelog](#changelog)
* [Special Thanks](#special-thanks)
* [License](#license)

## About

[Disease Outbreak Prediction-Prevention](https://github.com/KRITHIN913/Disease_Outbreak_Prediction-Prevention) is a state-of-the-art framework that bridges the gap between geospatial data science and predictive machine learning. You can use it to build dynamic public health response systems, allocate medical resources, and deploy mobile health units proactively.

In our research paper [Spatiotemporal Forecasting of Disease Outbreaks: A Hybrid DBSCAN and Random Forest Approach](#), we present a 3-phase methodology tracking epidemiological data. We study geographic variance, comment on the structural advantages of Random Forest over "black-box" Neural Networks in public health policymaking, and compare our density-based spatial bounds against KMeans.

To see the system in action, run the localized spatial clustering algorithms locally to generate interactive Folium maps!

## Features

* **Phase 1: Spatial Outbreak Detection** using localized DBSCAN anomaly filtering.
* **Phase 2: Spatiotemporal Feature Engineering** incorporating historic transmission and meteorology.
* **Phase 3: Predictive Modeling** via Random Forest for high risk forecasting.
* Highly interpretable "Feature Importance" matrix for policy interventions.
* Automatic centroid risk calculation for the deployment of Mobile Health Units.
* Generation of real-time Interactive HTML maps using `folium`.
* Comparison metrics dynamically handling `KMeans` and `Agglomerative` clustering architectures.

## Get Started

You have a few options to get started with the Disease Outbreak Prediction framework:
1. Clone the repository and run the spatial algorithms locally.
2. Adapt the scripts to inject your own localized epidemiological `.geojson` databases.

Integrating the clustering into your workflow is easy. Simply use the Python pipelines provided.

### Installation & Run
```bash
# Clone the repository
git clone https://github.com/KRITHIN913/Disease_Outbreak_Prediction-Prevention.git
cd Disease_Outbreak_Prediction-Prevention

# Provide a virtual environment
python -m venv venv
source venv/Scripts/activate

# Install required packages
pip install geopandas pandas numpy scikit-learn shapely folium

# Extract spatial map
python dbscan_algo.py
```

### Random Forest Pipeline
```python
# Coming soon / Phase 3 architecture
from sklearn.ensemble import RandomForestRegressor
# Train RF on each DBSCAN isolated zone for predictive modeling
```

## Flavors

The current spatiotemporal repository comes in three algorithms (flavors): **DBSCAN** `dbscan_algo.py`, **KMeans** `Kmean_algo.py`, and **Agglomerative** `Aglomerative_algo.py`. They differ primarily in how they draw spatial boundaries around epidemiological hotspots.

You will find the core anomaly filtering (noise point removal -1) strictly within the DBSCAN implementation.

## Citation

Please cite us if you use this framework or spatial forecasting algorithm in your research:

```bibtex
@INPROCEEDINGS{disease-outbreak-prediction,
  author={IIIT Nagpur Researchers},
  title={Spatiotemporal Forecasting of Disease Outbreaks: A Hybrid DBSCAN and Random Forest Approach},
  year={2024},
  keywords={Epidemiology; Machine Learning; Spatial Clustering; DBSCAN; Random Forest; Public Health}
}
```

## References

### Academia
These scientific articles ground the algorithmic components of this repository:

* Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A Density-Based Algorithm for Discovering Clusters in Large Spatial Databases with Noise.
* Francisco, M. E., Carvajal, T. M., & Watanabe, K. (2024). Hybrid Machine Learning Approach to Zero-Inflated Data Improves Accuracy of Dengue Prediction.
* Zhang, L., Zhao, Y ., & He, J. (2022). Geospatial Flu Outbreak Detection using DBSCAN.
* Liu, W., & Wang, Z. (2020). Clustering and Forecasting COVID-19 Data Using KMeans and Time Series Models.
* Jayaweera, P. M., et al. (2021). Hybrid Predictive Modeling of Dengue Outbreaks using Machine Learning and Clustering.
* Shaikh, R., Das, A., & Ghosh, P. (2023). Mapping the COVID-19 Outbreak in India: A Folium-Based Approach.

## Showcase

These analytical maps and models are utilized as proof of concepts from the repository.

* `dbscan_clusters_map.html` - Noise-filtered centroid forecasting.
* `kmeans_clusters_map.html` - Basic 5-cluster categorization map.
* `Agglomerative _clusters_map.html` - Hierarchical outbreak categorization.

## Community

Join our ongoing effort to build highly predictive, non-opaque epidemiological forecasting tools!

* Report an issue through GitHub.
* Formulate Pull Requests for Phase 3 integration (Random Forest backend).

## Author and Contributors

This specialized spatiotemporal platform was initiated by researchers at IIIT Nagpur and maintained by **KRITHIN913**.

Thanks to all contributors for contributing to this epidemiological initiative.

## Changelog

You can find the detailed specification of algorithm updates in our commit history.

## Special Thanks

Special thanks to open-source geo-science data projects without whom this research wouldn't exist: [Geopandas](https://geopandas.org/), [Scikit-learn](https://scikit-learn.org/), and [Folium](https://python-visualization.github.io/folium/).

## License

This software is heavily oriented for public-health response and is distributed under the [MIT License](LICENSE).