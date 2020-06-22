from flaskblog import db
from flaskblog.models import Post , User ,Cluster ,Applog
from flaskblog import sparkScript
import json 


# cluster =  Cluster.query.get('j-100app2')

# allLogs = Applog.query.filter_by(cluster_app_id=cluster.id).all()

# for logs in allLogs:
#     print(logs)

# cluster =  Applog.query.get('j-100app2')
# print(cluster)
db.session.query(Cluster).delete()
db.session.query(Applog).delete()
db.session.commit()
# sparkScript.LaunchDebugger(cluster)

# with open("sample.json", "r") as read_file:
#     data = json.load(read_file)


# # ----Testing Purpose------
# specificErrors=data['SpecificError']
# for specificError in specificErrors:
#     for key in specificError.keys():
#         error = key 
#         pathdict  = specificError[key]

#         if pathdict.keys():
#             print('hello')
#             for key in pathdict.keys():
#                 errorPath = key
#                 description = pathdict[key]
#             print(error)   
#             print(errorPath) 
#             print(description[0][0:1000])
#             # applog = Applog(error=error,location = errorPath , description = description[0] , cluster_app = cluster)
#             # db.session.add(applog)
    
#         else :
#             pass

# db.session.commit()

# allLogs = Applog.query.filter_by(cluster_app_id=cluster.id).all()
# for log in allLogs:
#     print(log.id,log.error,log.description , log.location)  

# if not Cluster.query.get('efewfw') :
#     print(True)
# else : 
#     print(False)


# db.session.query(Applog).delete()
# db.session.commit()

# print('Lets see the new list ')
   



# for new in newlist:
#     if new['ErrorPresent']:
#         print('Yo')
#         for allMssg in new['Path']:
#             # print(allMssg['errorMessage'])

#             # tempList = allMssg['errorMessage']
#             # print((tempList[0]))

#             print(allMssg['errorMessage'][0])





# cluster = Cluster.query.get('j-100app3')
# applog = Applog(error='Lost',location = '/users/achintan' , description = 'stack Trace' , cluster_app = cluster)
# db.session.add(applog)
# db.session.commit()

# print('Hello')
# # test1 = Cluster.query.get(test.cluster_app)

# allLogs = Applog.query.all()
# for log in allLogs:
#     print(log.error)
#     print(log.id)

# print(test1.clusterId)
