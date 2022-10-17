[English version](https://github.com/alyssonvidal/E-Commerce-Clusterization)

<center><img src="/images/ecommerce2.jpg" alt="logo_ecommerce" width="800" height="400"/></center>

## Descrição do Problema
Um problema recorrente no e-commerce é classificar os clientes de acordo com seu valor para a empresa. Uma das práticas utilizadas no mundo dos negócios para determinar isso é a tabela RFM (Recência, Frequência, Monetização). O estudo de caso abordado é um E-commerce que possui aproximadamente 5 mil clientes em seu banco de dados, que deseja identificar os melhores para encaminhá-los ao programa de fidelidade.

## Objetivo
**Principal:**
* Criar clusters de acordo com o RFM do cliente sem usar nenhum modelo de aprendizado de máquina, usando apenas teoria estatística.
* Criar clusters de acordo com o RFM do cliente usando alguns modelos de aprendizado de máquina.
* Comparar o modelo estatistico de quartis com o modelo de machine learning.
* Indicar os melhores clientes para um plano de fidelidade.


## Development Stages
[**Data Preprocessing**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part01_preprocessing.ipynb)<br>
Lidando com valores ausentes, duplicados e ruins, corrigindo tipos de dados, engenharia de dados, entrada de dados...

[**Exploratory Data Analysis**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part02_eda.ipynb)<br>
Estatistica Descritiva.

[**Data preparation**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part03_data_preparation.ipynb)<br>
Normalização, Padronização, Redução de Dimensionalidade, Outliers.

[**Machine Learning Model**](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/notebooks/part04_rfm_with_ml.ipynb)<br>
* **Modelos:** Kmeans, Hierachical Clustering, Gaussian Mixture Model, DBScan.<br>
* **Metricas:** WCSS, Silhouette Score, AIC, BIC<br>
* **Espaço de Estados:** UMAP, t-SNE, Embedding Space<br>



## Relatórios
[Relatório de Negócios](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/report/model_performace.MD)<br>
[Performace do Modelo de Machine Learning](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/report/model_performace.MD)<br>
[Comparação do Modelo de Machine Learning com o Modelo RFM Estatistico de Quartis](https://github.com/alyssonvidal/E-Commerce-Clusterization/blob/main/report/comparison.md)<br>

## Ferramentas
Linguagens: Python<br>
IDE: Visual Studio Code, Jupyter Notebook<br>
Bibliotecas: Pandas, Matplotlib, Seaborn, Plotly, Sklearn, scipy, yellowbricks<br>
Frameworks: Flask<br>
Produção: Heroku<br>
Metodologia: CRISP-DM<br>

## Referencias

*** 

## Resumo 
