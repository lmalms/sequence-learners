# ASHRAE III

## Overview

This directory contains the code and notebooks for the ASHRAE III project. All code was run in Jupyter notebooks on Kaggle. The most important notebooks are:

- [`ashrae-eda.ipynb`](./ashrae-eda.ipynb): Exploratory data analysis.
- [`ashrae-feature-engineering.ipynb`](./ashrae-feature-engineering.ipynb): Prepares the dataset for model training. Writes datasets to disk.
- [`ashrae-global-lightgbm.ipynb`](./ashrae-global-lightgbm.ipynb): Trains the best performing LightGBM model. Assumes data was prepared by `ashrae-feature-engineering.ipynb`.
- [`ashrae-meter-level-lightgbm.ipynb`](./ashrae-meter-level-lightgbm.ipynb): Trains a LightGBM model at the meter level. Assumes data was prepared by `ashrae-feature-engineering.ipynb`.

## Resources

### Papers

- <https://arxiv.org/pdf/2007.06933>
- <https://arxiv.org/pdf/2106.13475>
- <https://dl.acm.org/doi/10.1145/507533.507538>
- <https://link.springer.com/article/10.1007/s00180-022-01207-6>

### Blogs

- <https://www.kaggle.com/code/selfishgene/filtering-and-auto-correlation-tutorial>
