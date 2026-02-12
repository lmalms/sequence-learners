# UCI Electricity Load Forecasts

This project builds and evaluates various electricity load forecasts on the [UCI Electricity Load Diagrams 2011–2014](https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014) dataset. The project covers data download, exploration, and preprocessing and builds different forecasting models (seasonal naive, ETS, and a Temporal Convolutional Network) to predict electricity loads across several client sites and validation folds.

Shared configuration (validation windows, client-site lists, etc.) lives in `constants.py`. Run the notebooks in numerical order for a full reproduction.

---

## Notebooks

| Notebook           | Description                                                                                                                                                                                                                                      |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1.0_load**       | Downloads the UCI dataset from the archive, loads it as a Polars dataframe, and performs exploratory data analysis                                                                                                                               |
| **2.0_preprocess** | Preprocesses the raw UCI data: drops low-quality client sites, filters problematic time ranges, and interpolates missing timesteps to produce a clean long-format dataset saved as `preprocessed.pq`.                                            |
| **3.0_tcn**        | Introduces the Temporal Convolutional Network (TCN) used for load forecasting: defines the architecture (dilated causal convolutions, weight norm, encoder–decoder), dataset preparation utilities, and demonstrates training on synthetic data. |
| **3.1_tcn_kaggle** | Same TCN model and training setup as 3.0, structured for batch execution on Kaggle. Trains on the preprocessed UCI data and writes forecasts per client site and validation fold to `results/uci/tcn/`.                                          |
| **4.0_naive**      | Implements a seasonal naive baseline model. Saves results to `results/uci/naive`.                                                                                                                                                                |
| **5.0_ets**        | Fits an Exponential Smoothing (Holt–Winters) baseline per client using `statsmodels`. Produces forecasts for the same validation windows as the other models and saves them under `results/uci/ets/`.                                            |
| **6.0_evaluate**   | Loads forecasts from the naive, ETS, and TCN runs and evaluates them against ground truth data. Computes MAE, WAPE, and MSSE per site and fold, and summarises results for comparison.                                                           |
