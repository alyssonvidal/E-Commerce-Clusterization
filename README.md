Versão em  [português (BR)](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/references/README_PT.md)

<center><img src="/images/ecommerce2.jpg" alt="logo_ecommerce" width="800" height="400"/></center>

## Problem Statement
A recurring problem in e-commerce is classifying customers according to their value to the company, a problem also known as customer segmentation. One of the practices used in the business world to determine this is the RFM table (Recence, Frequency, Monetization), to obtain this table there are statistical methods and clustering algorithms that manage to reproduce practically the same results.

The case study addressed is an E-commerce that has approximately 5 thousand customers in its database, it wants to identify the best ones to refer them to the loyalty program.

## Objective
**Main:**
* Create clusters according to the customer's RFM using some machine learning models.
* Indicate the best customers for the loyalty plan called "insiders".
* Create a dashboard on metabase
* Deploy Model on AWS.

**Secundary:**

* Compare RFM Machine Learning model with RFM Statistical model.


## Development Stages
[**Data Preprocessing**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part01_preprocessing.ipynb)<br>
Dealing with missing, duplicated and bad values, fixing data types, feature engineering, data inputation...

[**Exploratory Data Analysis**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part02_eda.ipynb)<br>
Descriptive statistics, Cohort, Sales over time, Cancelations, Country of Customers, Rank of Customers, WorldCloud of Products...

[**Data preparation**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part03_data_preparation.ipynb)<br>
Outliers Detection, Normalization, Standardization, Dimensionality Reduction (PCA, UMAP, t-SNE, Tree Embedding). 

[**Machine Learning Model**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>
Kmeans, Hierachical Clustering, Gaussian Mixture Model, DBScan

[**Deploy**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>

<center><img src="/images/schema.png" alt="asasd" width="1190" height="794"/></center>




## Reports

[Business Report](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/reports/business_overall_report.md)<br>
[Model Performace](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/reports/model_performace.MD)<br>
[Comparison Machine Learning RFM with Statistical Quartile RFM](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/reports/comparison.md)<br>


## Tools
Languages: Python<br>
IDE: Visual Studio Code, Jupyter Notebook<br>
Libraries: Pandas, Matplotlib, Seaborn, Plotly, Sklearn, scipy, yellowbricks<br>
Dashboard: Metabase<br>
Deploy: AWS (S3,EC2,RDS)<br>
Methodology: CRISP-DM<br>

*** 
## Resume

After developing the clustering model, we arrived at a solution for ten customer groups, one of which being nominated for the "Insiders" loyalty program. The basic strategy of the action plan is to make good customers even better through discounts and special offers starting from a certain amount of purchases.

<center>
  
Rank | CustomerID | Sales($)
:--------- | :------: | :-------:
1| 5749	| 14844.77
2| 15098	| 13305.50
3| 12357	| 6207.67
4| 12415	| 5948.31	
5| 12590	| 4932.13	
6| 12688	| 4873.81	
7| 12752	| 4366.78	
8| 18102 | 4327.62	
9| 18251	| 4314.72
10| 17450	| 4229.36	  
</center>

### Cohort 
<center><img src="../images/cohort_percentage.png" alt="rfm_ml"/></center><br>
### Metabase Dashboard
<center><img src="/images/metabase.png" alt="asdgg" width="1287" height="842"/></center>

