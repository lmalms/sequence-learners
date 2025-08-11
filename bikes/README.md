# Auckland Bikes

_Auckland Bikes_ is a hands-on project for learning time series forecasting techniques by predicting daily bicycle traffic across various Auckland monitoring sites. The project covers both classical methods (e.g. Exponential Smoothing, SARIMAX) and modern deep learning approaches (e.g. LSTMs, DeepAR).

The goal is educational: to gain practical experience with data preprocessing and modeling workflows across different forecasting techniques, rather than to optimize prediction accuracy or to conduct a comprehensive benchmarking study.

## Installation

The project uses [uv](https://docs.astral.sh/uv/) as a dependency manager. To install the project dependencies the following in the root directory of the project.

```bash
uv sync
```

## Data

Daily bicycle movement data is available at [AT Monthly Cycle Monitoring](https://at.govt.nz/cycling-walking/research-monitoring/monthly-cycle-monitoring). The project provides the [bikes.data.load_cycle_counts()](./src/bikes/data/__init__.py) utility function to load cycle movement data from January 2022 to December 2024. The [01_data.ipynb](./01_data.ipynb) notebook can be used to load the data and run some basic exploratory analysis.

## Models

The project builds a series of time series models to forecast daily bicycle traffic across various Auckland locations. The models are trained using jupyter notebooks. The notebook titles are self-explanatory but for quicker referencing:

- [Exponential Smoothing](./02_ets.ipynb)
- [SARIMAX](./03_sarimax.ipynb)
- [Theta](./04_theta.ipynb)
- [Prophet](./05_prophet.ipynb)
- [RNN](./06_rnn.ipynb)
- [LSTM](./07_lstm.ipynb)
- [DeepAR](./08_deepar.ipynb)

The project also contains a few study notebooks for a subset of the models above. These can be found in the [study_notebooks](./study_notebooks/) folder.

## Evaluation

Although the primary objective of the project was not predictive performance or benchmarking, the project includes a basic comparison of predictive performance across models. Forecasts are compared across 19 sites for the period 1 Oct 2024 - 1 Jan 2025 using [MAPE](https://en.wikipedia.org/wiki/Mean_absolute_percentage_error) and [MASE](https://en.wikipedia.org/wiki/Mean_absolute_scaled_error) metrics. The [09_evaluate.ipynb](./09_evaluate.ipynb) notebook can be used to plot and compare forecasts from each model.

## Resources

- [AT Monthly Cycle Monitoring](https://at.govt.nz/cycling-walking/research-monitoring/monthly-cycle-monitoring)
- [Forecasting: Principles and Practice](https://otexts.com/fpp3/)
- [neuralforecast DeepAR Implementation](https://github.com/Nixtla/neuralforecast/blob/main/nbs/models.deepar.ipynb)
- [neuralforecast Distribution Losses](https://github.com/Nixtla/neuralforecast/blob/main/nbs/losses.pytorch.ipynb)
