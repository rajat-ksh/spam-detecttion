import os
import pdb
import re
import csv

#path declartion
path = 'C:\\Users\\Rajat kushwaha\\Downloads\\enron1\\spam'

#List of spam keywords
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
files = []

csv_data=['STATUS','EMAIL_CTR','URL_CTR','IP_CTR','SP_CTR']

#r=root, d=directories, f = files

# with open('spamDataset.csv', 'w') as csvFile:
#     writer = csv.writer(csvFile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(csv_data)
# csvFile.close()

i=0
for r, d, f in os.walk(path):
        for file in f:

            Li_RD = []
            SP_CTR= 0
            EM_CTR=0
            IP_CTR=0
            URL_CTR=0
            filename = "{}\{}".format(path, file)
            file_h =open(filename, 'r', encoding='utf-8', errors='ignore')
            text=file_h.read()


            if len(re.findall(r'[\w\.-]@[\w\.-]+',text))!=0:

                EM_CTR=EM_CTR+len(re.findall(r'[\w\.-]@[\w\.-]+',text))
                #print(re.findall(r'[\w\.-]@[\w\.-]+',text))

            if len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',text))!=0:
                URL_CTR+=len(re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+',text))


            if len(re.findall(r'[0-9]+(?:\.[0-9]+){3}',text))!=0:
                IP_CTR+=len(re.findall(r'[0-9]+(?:\.[0-9]+){3}',text))


            file_h.seek(0)
            for line in file_h:
                for word in line.split(" "):
                    if word in L_Spam:
                        #print(word)
                        SP_CTR+=1


            Li_RD.append(1)
            Li_RD.append(EM_CTR)
            Li_RD.append(URL_CTR)
            Li_RD.append(IP_CTR)
            Li_RD.append(SP_CTR)
            i+=1
            print(i)

            file_h.close()

            #input()
            with open('spamDataset.csv', 'a') as csvFile:
                writer = csv.writer(csvFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                writer.writerow(Li_RD)
            csvFile.close()
            file_h.close()


