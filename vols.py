import os
import json
import sys
#collecting json data
json_data=os.popen("aws ec2 describe-volumes").read()
#converrting json data into dict
dict_data=json.loads(str(json_data))
#opening a file
myfile=open("my_server_info.txt","w")
myfile.writelines("s.no\tvol_id\tsize\n")
myfile.close()
#Appending volume data in to file 
sys.stdout=open("my_server_info.txt","a")
for i in range(len(dict_data["Volumes"])):
#	print >> myfile,i+1,"\t",dict_data["Volumes"][i]['VolumeId'],dict_data["Volumes"][i]['Size']
    print (i+1,"\t",dict_data["Volumes"][i]['VolumeId'],dict_data["Volumes"][i]['Size'])
#	print (i+1\tdict_data["Volumes"][i]['VolumeId']\t\tdict_data["Volumes"][i]['Size'])
sys.stdout.close()
