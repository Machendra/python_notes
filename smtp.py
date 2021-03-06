#!/usr/bin/python
#Reference Website https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/
#https://myaccount.google.com/lesssecureapps
#https://accounts.google.com/DisplayUnlockCaptcha

import json,getpass
from pprint import pprint
import datetime
import os,subprocess,shlex,json,re,smtplib,ssl,base64
from datetime import date
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Declaring variables   
today = date.today()
current_date=today.strftime("%Y.%m.%d")
FILENAME="/root/my_server_info.txt-"+current_date+".txt"
RECIEVER_EMAIL= ['machendra.surya@gmail.com']
print FILENAME

def collecting_volumedata(filename):

#Reading the volume information
    vol_output = os.popen("aws ec2 describe-volumes").read()
#Converting json to dictionary
    dict_output=json.loads(str(vol_output))
#Creating volumes file to write the volume data
    myvol_data=open(filename,"w")
    myvol_data.writelines("S.No \tVolumeId\t\tSize\n")
#Collecting volume information from the dict_output
    for vol in range(len(dict_output["Volumes"])):
        print >> myvol_data, vol+1,"\t",dict_output["Volumes"][vol]["VolumeId"],"\t",dict_output["Volumes"][vol]["Size"]

#File closing
    myvol_data.close()
    sendmail("testingmail",FILENAME)

def sendmail(message,filename):
    port = 587
    smtp_server = "smtp.gmail.com"
    fromaddr = 'machendra.surya@gmail.com'
    password=getpass.getpass()
    toaddr = ','.join(RECIEVER_EMAIL)
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ebs_volumes_report-"+current_date
    body = "Aws Volume Information"+"\n\n"+message
    msg.attach(MIMEText(body, 'plain'))
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server=smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login("machendra.surya@gmail.com", password)
    text = msg.as_string()
    server.sendmail(fromaddr, RECIEVER_EMAIL, text)

collecting_volumedata(FILENAME)
