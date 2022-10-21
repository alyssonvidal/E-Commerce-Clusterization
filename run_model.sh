
#Take current dat
takedate=$(date +'%Y-%m-%d')

#path (root of project) 
path='/Users/Alysson/Documents/Projects/E-Commerce-Clusterization'

#PS C:\> Get-Command papermill
#CMD C:\> where papermill 

path_pm='/Users/Alysson/Documents/Projects/E-Commerce-Clusterization/.venv/scripts'


# path where papermill is installed on env (find: 'which papermill' on project root folder)
#path_to_envs='/Users/home/opt/anaconda3/envs/pa005_clustering/bin'

$path_pm/papermill.exe $path/src/models/model-deploy.ipynb $path/reports/output/model-deploy-$takedate.ipynb