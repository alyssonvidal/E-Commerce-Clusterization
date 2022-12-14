# Model Performace

## Chosen Model: Hierachical Cluster
**Date:** 18/10/2022
<center><img src="../images/HierarchicalCluster.png" alt="rfm_ml" width="480" height="320"/></center><br>



**Total Features** 3<br>
**Number of Features Used:** 3<br>
**Features:** GrossRevenueTotal, RecencyDays, Frequency<br>
**Framework:** scipy<br>
**Parameters>**<br>
- Method: ward<br>
- Metric(distance): Euclidean<br>
- Criterion: Maxclust  <br>

**Estimator:**  
scipy.cluster.hierarchy.linkage(X, 'ward', metric='euclidean') , <br>
scipy.cluster.hierarchy.fcluster(model, k, criterion='maxclust') <br>                     

**Evaluating Metrics:** Dendogram, Silhouette Score<br>
**Dimensionality Reduction:** UMAP, 2<br>
**Embedding:** No<br>

**Number of Clusters:** 10<br>
<sub>The choice of this number is due much more to adapting to the already known RFM table than the number of clusters that the algorithm performed better.</sub><br>



<center><img src="../images/rfm_ml_table.png" alt="rfm_ml" width="420" height="280"/></center><br>

***



### Analysis

The hierarchical Clustering model performed especially well at the extremes of the RFM metrics, it segmented the "good outliers" well and these are critical points in the business world as the most difficult decisions are made on top of them.

The points considered critical were "Champions", "New Customers", "Cannot Lose Them". 

"Champions" must be a special group of customers who buy much more than other customers, this cluster could not be too generic to the point of grouping many customers, nor too specific to the point of not being replicable for new aspirants in the future or being exclusive too much for these customers.


 Most of a company's action plans are in relation to new customers, so it is essential that the machine learning model identifies this group, the hierarchical cluster did this very well considering users who performed approximately one to two purchases within a week from a new customer.

 "Can not Lose Them" are those who have already purchased a lot from the company but have not purchased anything for sometime. This is also another group that has a constant action plan from the business team because they want to know how to identify the reasons that lead this customer to leave and bring him back. "The hierarchical cluster possibly performed worse here because it has a lot of similarity with the "At Risk" and "Loyal Customers" those cluster are very close to each other.
