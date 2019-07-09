import pandas as pd
import numpy as np
import re
import os
data=pd.read_csv('hamDatasetedited1.csv')
#print(data)
L_Spam=['bank','beneficiary','bonus','big sale','bounty','big','credit','card','coupon','cash','contact','bonus','casino','celebrity','click','click','collect',
        'deal','double','today','earn','extra','easy term','email','marketing',
        'free','for you','free access','full refund','get','guarantee','guaranteed','home based','hire','hiring','huge'
        'income','increase sale','instant','insurance','invest','lose','life','insuarance','make','million','money','miracle'
        'no claim','no fees','no hidden','notspam','now only','obligation','offer','offer expires','one time','order now',
        'open','opportunity','passwords','per week','prize','problem','profit','promise you','sale','sales',
        'satisfaction','subscribe','success','TnC','term','condition',
        'rate',"spam",'trial','unlimited','US','dollars','$','unsubscribe','vacation','visit our website',
        'weight','wait','warranty',
        '<html>','img','jpg','order']

independent_var=data.columns
independent_var=independent_var.delete(0)
x=data[independent_var]
#print(independent_var)
y=data['STATUS']
#print(y)
from sklearn.linear_model import LogisticRegression
import sklearn
#print("sklearn:%s"% sklearn.__version__)
LR=LogisticRegression()
LR.fit(x,y)
choice='yes'

file=[]



# for r, d, f in os.walk(path):
#     for file in f:
#         filename = "{}\{}".format(path, file)

while choice=='yes' or choice=="YES":
    path = input("Enter the path of the file")
    f=open(path, 'r', encoding='utf-8', errors='ignore')
    e_ctr=0
    u_ctr=0
    i_ctr=0
    s_ctr=0
    text=f.read()
    print()
    print("------------------------------------------------------------------------------"
          "\n\t\t\t\tMail")
    print(text)

    if len(re.findall(r'[\w\.-]@[\w\.-]+', text)) != 0:
      e_ctr=e_ctr + len(re.findall(r'[\w\.-]@[\w\.-]+', text))
        # print(re.findall(r'[\w\.-]@[\w\.-]+',text))

    if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)) != 0:
        u_ctr += len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text))

    if len(re.findall(r'[0-9]+(?:\.[0-9]+){3}', text)) != 0:
        i_ctr += len(re.findall(r'[0-9]+(?:\.[0-9]+){3}', text))

    f.seek(0)
    for line in f:
        for word in line.split(" "):
            if word in L_Spam:
            #print(word)
                s_ctr+=1


    Li_RD=[]
    #print(e_ctr)

    if e_ctr<9:
        e_ctr=8
        Li_RD.append(e_ctr)

    elif e_ctr>9 and e_ctr<16:
        e_ctr=16
        Li_RD.append(e_ctr)
    else:
        Li_RD.append(e_ctr)


    f.close()


    Li_RD.append(u_ctr)
    Li_RD.append(i_ctr)
    Li_RD.append(s_ctr)
    i=0
    email={}
    for feature in independent_var:
        #temp=int(input("Enter "+feature+":-"))
        #email[feature]=temp
        email[feature]=Li_RD[i]
        i+=1
    email_df=pd.DataFrame(email,index=[0],columns=independent_var)
    # print(email)
    print(email_df)
    status=LR.predict(email_df)
    if status[0]==0:
        print('-----------------------------------------------------------------------'
              '\nMail Status:- HAM')
    elif status[0]==1:
         print('-----------------------------------------------------------------------'
               '\nMail Status:- SPAM')

    choice=input("---------------------------------------------------------------------"
                 "\nWant to check for more mails press.? yes..")

    print("\n\n\n-----------------------------------------------------------------\n")