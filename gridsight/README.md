# GridSight

Reproducible electricity load forecasting notebooks, from data preparation through model training and evaluation.

## [UCI](./notebooks/uci/)

**Data:**

- https://archive.ics.uci.edu/dataset/321/electricityloaddiagrams20112014
- [Load](./notebooks/uci/1.0_load.ipynb)
- [Preprocess](./notebooks/uci/2.0_preprocess.ipynb)

**Models:**

- [Naive](./notebooks/uci/4.0_naive.ipynb)
- [ETS](./notebooks/uci/5.0_ets.ipynb)
- [TCN](./notebooks/uci/3.1_tcn_kaggle.ipynb)

## [PJM](./notebooks/pjm/)

**Data:**

- https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption
- [Load](./notebooks/pjm/1.0_load.ipynb)

**Models:**

- [Dynamic Regression Model](./notebooks/pjm/5.1_sarimax.ipynb) (Fourier Features + ARIMA Errors)
- [LSTNet](./notebooks/pjm/2.0_lstnet.ipynb)
- [TCN](./notebooks/pjm/3.0_tcn_kaggle.ipynb)

**Resources:**

- LSTNet:
  - https://github.com/laiguokun/LSTNet/tree/master?tab=readme-ov-file
  - https://github.com/laiguokun/LSTNet/tree/master

## Other resources

- ES-RNN:
  - https://medium.com/analytics-vidhya/forecasting-in-python-with-esrnn-model-75f7fae1d242
  - https://github.com/kdgutier/esrnn_torch?tab=readme-ov-file
  - https://arxiv.org/abs/2112.02663
  - https://proceedings.neurips.cc/paper_files/paper/2017/file/32bb90e8976aab5298d5da10fe66f21d-Paper.pdf
