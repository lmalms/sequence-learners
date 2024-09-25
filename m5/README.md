# Next steps
- Include category maps in dataset
- Cast fourier features + sell price to float16 in pre processing
- Also evaluate on train set
- Residual + SHAP analysis
- Data preprocessing with polars - WIP but cool to learn the API

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

# Resources
- https://www.sciencedirect.com/science/article/pii/S0169207021001874
- https://github.com/Mcompetitions/M5-methods/tree/master
- https://tsfresh.readthedocs.io/en/latest/index.html
- https://www.sciencedirect.com/science/article/abs/pii/S0169207016000315
- https://www.sciencedirect.com/science/article/abs/pii/S0169207019301359
- https://cienciadedatos.net/documentos/py39-forecasting-time-series-with-skforecast-xgboost-lightgbm-catboost.html
- https://scikit-learn.org/stable/auto_examples/linear_model/plot_tweedie_regression_insurance_claims.html
- https://scikit-learn.org/stable/auto_examples/linear_model/plot_poisson_regression_non_normal_loss.html


## Hierarchical Forecasting
- https://github.com/Nixtla/hierarchicalforecast
- https://github.com/rshyamsundar/gluonts-hierarchical-ICML-2021
- https://github.com/sktime/sktime-tutorial-pydata-berlin-2022