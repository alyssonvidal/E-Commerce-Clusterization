Versão em  [português (BR)](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/references/README_PT.md)

# Customers Segmentation - Loyalty Program

<center><img src="/images/ecommerce2.jpg" alt="logo_ecommerce" width="800" height="400"/></center>

## Problem Statement

To increase the customer retention, the CEO of an E-commerce would like to start a new marketing campaign called "Insiders", this campaign aims to offer to potential loyal customers a special benefits plan. The CEO asked his team of data scientists at his company to identify the key customer segments the company has and which customers are most eligible for this campaign.

The study case refers to an online retail store based in UK, were collected invoices from approximately 5000 customers, for a period of one year (November 2016 to December 2017). Database can be found on [Kaggle](https://www.kaggle.com/datasets/carrie1/ecommerce-data).

## Objective
**Main:**
* Through machine learning algorithms, identify the most relevant customer segments that the company has.
* Identify which customers are most eligible to participate in the loyalty program.
* Publish the results into a dashboard that can be accessed from anywhere.

**Secundary:**

* Using the RFM metric (Recency, Frequency, Monetization), to compare the results of a statistical model and machine learning model.


## Development Stages
[**Data Preprocessing**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part01_preprocessing.ipynb)<br>
Dealing with missing, duplicated and bad values, fixing data types, feature engineering, data inputation...

[**Exploratory Data Analysis**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part02_eda.ipynb)<br>
Descriptive statistics, Cohort, Sales over time, Cancelations, Country of Customers, Rank of Customers, WorldCloud of Products...

[**Data Preparation**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part03_data_preparation.ipynb)<br>
Outliers Detection, Normalization, Standardization, Dimensionality Reduction (PCA, UMAP, t-SNE, Tree Embedding). 

[**Machine Learning Model**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>
Kmeans, Hierachical Clustering, Gaussian Mixture Model, DBScan

[**Deploy**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>
Metabase, AWS (RDS, EC2, S3), Crontab, Papermill, Postgres

<center><img src="/images/schema.png" alt="asasd" width="1190" height="794"/></center>

## Reports

[Business Report - Loyalty Program](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/reports/business_overall_report.md)<br>
[Comparison RFM - Machine Learning and Statistical](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/reports/comparison.md)<br>


## Tools
Languages: Python<br>
IDE: Visual Studio Code, Jupyter Notebook<br>
Libraries: Pandas, Matplotlib, Seaborn, Plotly, Sklearn, scipy, yellowbricks<br>
Dashboard: Metabase<br>
Deploy: AWS<br>
Methodology: CRISP-DM<br>
