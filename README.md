Versão em  [português (BR)](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/references/README_PT.md)

<center><img src="/images/ecommerce2.jpg" alt="logo_ecommerce" width="800" height="400"/></center>

## Problem Statement
A recurring problem in e-commerce is classifying customers according to their value to the company. One of the practices used in the business world to determine this is the RFM (Recence, Frequency, Monetization) table. The case study addressed is an E-commerce that has approximately 5 thousand customers in its database, it wants to identify the best ones to forward them to the loyalty program.

## Objective
**Main:**
* Create clusters according to the customer's RFM using some machine learning models.
* Indicate the best customers for the loyalty plan.
**Secundary:**
* Create clusters according to the customer's RFM without using any machine learning models, using only statistical theory.
* Compare the machine learning model with the statistical model.



## Development Stages
[**Data Preprocessing**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part01_preprocessing.ipynb)<br>
Dealing with missing, duplicated and bad values, fixing data types, feature engineering, data inputation...

[**Exploratory Data Analysis**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part02_eda.ipynb)<br>
Descriptive statistics.

[**Data preparation**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part03_data_preparation.ipynb)<br>
Normalization, Standardization, Dimensionality Reduction, Outlines.

[**Machine Learning Model**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>
* **Models:** Kmeans, Hierachical Clustering, Gaussian Mixture Model, DBScan.<br>
* **Metrics:** WCSS, Silhouette Score, AIC, BIC<br>
* **Support:** UMAP, t-SNE, Embedding Space<br>



## Reports
Business Report<br>
[Model Performace](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/report/model_performace.MD)<br>
[Comparison Machine Learning RFM with Statistical Quartile RFM](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/report/comparison.md)<br>

## Tools
Languages: Python<br>
IDE: Visual Studio Code, Jupyter Notebook<br>
Libraries: Pandas, Matplotlib, Seaborn, Plotly, Sklearn, scipy, yellowbricks<br>
Frameworks: Flask<br>
Deploy: Heroku<br>
Methodology: CRISP-DM<br>

## References

*** 

## Brefing 
