
## Welcome to Apache Spark - Debugger Tool. 

Here we discuss various optimisation and troubleshooting Error scerios for Spark Application. We focus on community resources to help write better ETL pipelines. If you have an interesting approach that helped improve performance feel free to head to live demo site and post it up for other's benefits. 

### _Further you can use this to tool analyse your spark application logs._

```python
git clone https://github.com/chintanagrawal97/sparkLogDebugger.git
python3 -m venv spark 
source spark/bin/activate 
python install -r requirements.txt 
python run.py
```

After starting the app. Create a profile.
Go to Spark Logs --> Feed in your applicationId and ClusterId details for eg. 

Refer to the screenshots. 

The Application expects the container files to be present as follows : 

```bash
<User_provided_Log_Path>/<Cluster_Id>/containers/<application_id>/..
```

Refer to code line 464 in SparScript.py
 ```python
data=getListOfFiles(LOGPATH+'/'+CLUSTER_ID+'/containers/'+APPLICATION_ID)
```

### _Future Enhancements_ 

1. Decouple FrontEnd and Backend . 
2. Incorporate other application such as HIVE , PRESTO . 
