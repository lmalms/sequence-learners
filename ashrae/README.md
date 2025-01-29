# ASHRAE III

## Next steps

- Outlier removal:
  - Run feature engineering with first round of outlier removal for electricity + score models.
  - Remove periods of constant electricity readings, run feature eng. and score models.
  - <https://www.kaggle.com/competitions/ashrae-energy-prediction/discussion/122471>
  - <https://www.kaggle.com/code/gunesevitan/ashrae-lightgbm-1-048-no-leak>
  - <https://www.kaggle.com/code/aitude/ashrae-kfold-lightgbm-without-leak-1-08>

- Read: <https://scikit-learn.org/stable/modules/cross_validation.html>
- sklearn Pipelines: Build prediction pipeline using HistGradientBoostingRegressor

## Notes

## Learnings

### Data (exploration, cleaning, feature engineering, etc)

- It pays off to plot energy demand for individual buildings.
  - In the initial EDA I primarily focused on energy demand at an aggregate level e.g What is the distribution of electricity consumption across all buildings and timestamps? What is the timeseries of average electricity consumption across all buildings. However, this hides potential data issues with individual buildings e.g. outliers, long periods of zero or constant consumption which do not match typical consumption patterns.

### Modelling

## Resources

### Papers

- <https://arxiv.org/pdf/2007.06933>
- <https://arxiv.org/pdf/2106.13475>
- <https://dl.acm.org/doi/10.1145/507533.507538>
- <https://link.springer.com/article/10.1007/s00180-022-01207-6>

### Blogs

- <https://www.kaggle.com/code/selfishgene/filtering-and-auto-correlation-tutorial>
