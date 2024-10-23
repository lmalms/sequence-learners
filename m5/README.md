# M5 Forecasting Accuracy

This section of the repo contains data visualisation, feature engineering and model training code for the [M5 Forecasting Accuracy](https://www.kaggle.com/competitions/m5-forecasting-accuracy/overview) competition. The key notebooks are:

- `m5-acc-eda.ipynb`: Data visualtion code of sales data. The plots produced by this notebook can be found unde `/plots`
- `m5-acc-feature-engineering.ipynb`: Feature engineering code to produce a feature rich training set for model training
- `m5-acc-global-lightgbm.ipynb`: Training code to train a single global non-recursive LightGBM model and output competition submission

## Learnings

### Data Processing

#### Memory Errors

- **Problem**
  - Preprocessing and feature engineering often resulted in Out-of-Memory errors.
  - The issue often came up when merging large dataframes together or concatenating dataframes across rows (i.e. `pd.concat(..., axis=1)`)
- **Solutions**
  - Cast columns to lower resolution datatypes before merging. For example, `pd.to_numeric()` was useful to casting numerical columns to smaller data types automatically. Casting columns to `categorical` variables also helps if the number of possible values is small.
  - Merge as early as possible and do feature engineering on the merged dataframe. Computing extra features that are not needed for the merge add memory overhead. Try and compute them on the dataframe after the merge.
  - Merge in chunks. Rather than trying to merge large dataframes in a single call, iterate over the larger dataframe in chucnks and merge the chunks iteratively with other dataframes. After iterating over the dataframe chunks concatenate them into the final dataframe.
  - During the merge only keep columns that are actually needed for the merge. Drop any unnecessary columns before the merge. After each chunk iteration only store the target column that is to be inserted into the original dataframe. Do not store columns that already exist in the original dataframe as this adds unnecessary overhead.
  - In the final concatenation try and avoid row-wise `(axis=1)` concats and try just inserting the column instead.

#### Next steps

- Migrate data processing code to [polars](https://pola.rs/)

### Modelling

#### Single Global Forecasting Model

- For a single global non-recursive LightGBM model the lowest average RMSE is limited to ~2.21 sales
- Best performing model scores 0.64283 on private leaderboard (~top 5%)
- **Features**
  - Non-recursive LightGBM model requires a lot of feature engineering to get good performance
  - Lagged and rolling features of target variable (i.e. sales) as well as exogenous features (e.g. price and events) are important for good performance
- **Modelling**
  - With large complex datasets a good philosophy for training gradient boosted models seems to be to aim for low learning rates and just train for a large number of iterations. Overfitting was limited even after > 1000 iterations.
  - Main limitation to achieve better performance using a single model seems to be available RAM which was limiting the number of features that can be included in the model.
  - RAM issues mainly occurred during dataset construction. Can use parameters like `max_bin` and `histogram_pool_size` to control memory consumption at the cost of lower accuracy

#### Next steps

- Train a store-level LightGBM.
  - This should reduce RAM consumption, and might be an easier pattern to learn that training a single global model

- Cluster similar timeseries together
  - It might be possible to use some unsupervised learning techniques to cluster similar timeseries together. One could then train a separate model for each of them. It might be easier to learn patterns in the timeseries if many similar series are trained together

## Resources

### Papers

- <https://www.sciencedirect.com/science/article/pii/S0169207021001874>
- <https://www.sciencedirect.com/science/article/abs/pii/S0169207016000315>
- <https://www.sciencedirect.com/science/article/abs/pii/S0169207019301359>

### Talks

- <https://www.youtube.com/watch?v=9QtL7m3YS9I>

### Tutorials

- <https://cienciadedatos.net/documentos/py39-forecasting-time-series-with-skforecast-xgboost-lightgbm-catboost.html>
- <https://github.com/rshyamsundar/gluonts-hierarchical-ICML-2021>
- <https://github.com/sktime/sktime-tutorial-pydata-berlin-2022>
- <https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html>
- <https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html>

### Repos

- <https://www.sktime.net/en/stable/>
- <https://unit8co.github.io/darts/>
- <https://tsfresh.readthedocs.io/en/latest/index.html>
- <https://github.com/Nixtla/hierarchicalforecast>
- <https://github.com/Mcompetitions/M5-methods/tree/master>
