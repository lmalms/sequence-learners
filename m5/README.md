# Next steps -- Path to Completion
- Documentation for feature engineering functions
- Residual + SHAP analysis of best performing global LightGBM model
- Develop baseline models e.g. exponential smoothing with Darts
- Train models at store level
- Cluster time series and train similar clusters together
- Data preprocessing with polars

# Learnings
## Data Processing
### Memory Errors
- **Problem**
    - Preprocessing and feature engineering often resulted in Out-of-Memory errors.
    - The issue often came up when merging large dataframes together or concatenating dataframes across rows (i.e. `pd.concat(..., axis=1)`)
- **Solutions**
    - Cast columns to lower resolution datatypes before merging. For example, `pd.to_numeric()` was useful to casting numerical columns to smaller data types automatically. Casting columns to `categorical` variables also helps if the number of possible values is small.
    - Merge as early as possible and do feature engineering on the merged dataframe. Computing extra features that are not needed for the merge add memory overhead. Try and compute them on the dataframe after the merge.
    - Merge in chunks. Rather than trying to merge large dataframes in a single call, iterate over the larger dataframe in chucnks and merge the chunks iteratively with other dataframes. After iterating over the dataframe chunks concatenate them into the final dataframe.
    - During the merge only keep columns that are actually needed for the merge. Drop any unnecessary columns before the merge. After each chunk iteration only store the target column that is to be inserted into the original dataframe. Do not store columns that already exist in the original dataframe as this adds unnecessary overhead.
    - In the final concatenation try and avoid row-wise `(axis=1)` concats and try just inserting the column instead.

## Modelling
### Single Global Forecasting Model
- For a single global LightGBM model the lowest average RMSE is limited to ~2.7 sales
- Main limitation seems to be available RAM which limits the number of features that can be included in the model
- Can use parameters like `num_leaves`, `max_bin` and `histogram_pool_size` to control memory consumption at the cost of lower accuracy
- Next steps to unlock further improvements:
    - Residual and Shaply value analysis of best performing model
    - Train store-level LightGBM. This should reduce RAM consumption, and might be an easier pattern to learn


# Resources
- https://www.sciencedirect.com/science/article/pii/S0169207021001874
- https://www.sciencedirect.com/science/article/abs/pii/S0169207016000315
- https://www.sciencedirect.com/science/article/abs/pii/S0169207019301359
- https://cienciadedatos.net/documentos/py39-forecasting-time-series-with-skforecast-xgboost-lightgbm-catboost.html
- https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html
- https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html

## Talks
- https://www.youtube.com/watch?v=9QtL7m3YS9I

## Repos
- https://www.sktime.net/en/stable/
- https://unit8co.github.io/darts/
- https://tsfresh.readthedocs.io/en/latest/index.html
- https://github.com/Nixtla/hierarchicalforecast
- https://github.com/Mcompetitions/M5-methods/tree/master

## Tutorials
- https://github.com/rshyamsundar/gluonts-hierarchical-ICML-2021
- https://github.com/sktime/sktime-tutorial-pydata-berlin-2022