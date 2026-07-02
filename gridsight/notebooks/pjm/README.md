# PJM Electricity Load Forecasts

This project builds and evaluates various electricity load forecasts on the [PJM Hourly Energy Consumption](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption) dataset. The project covers data loading, exploration, and preprocessing and builds different forecasting models (seasonal naive, dynamic regression with Fourier features and ARIMA errors, LSTNet, and a Temporal Convolutional Network) to predict hourly demand across eleven PJM balancing authority areas and validation folds.

Shared configuration (validation windows, site lists, etc.) lives in `constants.py`. Run the notebooks in numerical order for a full reproduction.

---

## Notebooks

| Notebook               | Description                                                                                                                                                                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1.0_load**           | Loads the PJM dataset, performs exploratory data analysis (timestamp coverage, missing values, seasonality, FFT spectra), and interpolates missing timestamps to produce per-site processed datasets saved as `{site}_hourly_processed.pq`.   |
| **2.0_lstnet**         | Introduces the LSTNet architecture used for load forecasting (CNN, GRU, skip GRU, and autoregressive components), dataset preparation utilities, and demonstrates training on synthetic data.                                                      |
| **2.1_lstnet_kaggle**  | Same LSTNet model and training setup as 2.0, structured for batch execution on Kaggle. Trains on the processed PJM data and writes forecasts per site and validation fold to `results/pjm/lstnet/`.                                              |
| **3.0_tcn_kaggle**     | Defines the Temporal Convolutional Network (TCN) architecture (dilated causal convolutions, weight norm, encoder–decoder) and trains on PJM data structured for Kaggle batch execution. Writes forecasts to `results/pjm/tcn/`.                 |
| **4.0_naive**          | Implements a seasonal naive baseline model. Saves results to `results/pjm/naive/`.                                                                                                                                                               |
| **5.0_sarimax_study_nb** | Exploratory notebook for the dynamic regression baseline (Fourier features + ARIMA errors): fits models, inspects residuals, and visualises forecasts for a single site.                                                                      |
| **5.1_sarimax**        | Full run of the dynamic regression model (Fourier features + ARIMA errors) across validation folds. Produces forecasts for the same validation windows as the other models and saves them under `results/pjm/sarimax/`.                        |
| **6.0_evaluate**       | Loads forecasts from the naive, SARIMAX, LSTNet, and TCN runs and evaluates them against ground truth data. Computes MAE, WAPE, and MSSE per site and fold, and summarises results for comparison.                                               |
