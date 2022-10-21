from copy import copy
import schedule
import time
import datetime
import papermill as pm
from shutil import copyfile
import socket

hostname = socket.gethostname()
timenow = datetime.datetime.now().strftime('%Y/%m/%d/%H:%M:%S')

record = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
path_model_report_initial ='/Users/Alysson/Documents/Projects/E-Commerce-Clusterization/reports/output/model-test.ipynb'
path_model_report_last = f'/Users/Alysson/Documents/Projects/E-Commerce-Clusterization/reports/output/{record}-model-test.ipynb'
path_model_deploy='/Users/Alysson/Documents/Projects/E-Commerce-Clusterization/scr/models/model-deploy.ipynb'


def job():
    
    print(f"Executing model-deploy using papermill... {timenow} \n")
    pm.execute_notebook(f"{path_model_deploy}", f"{path_model_report_last}", 
                                                                            {'papermill_record': f'{timenow}',
                                                                             'papermill_hostname': f'{hostname}'
                                                                            })
    #copyfile(f"{path_model_report_initial}", f"{path_model_report_last}")
    print(f"\nReturing {record}-model-test... {timenow}")


schedule.every(10).seconds.do(job)
schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job) 
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(3)