import csv
import math
with open("new.csv",newline='')as dew:
    reader=csv.reader(dew)
    file_data=list(reader)
data=file_data[0]

def mean(data):
    n=len(data)
    sum=0
    for i in data:
        sum=sum+int(i)
    mean= sum/n 
    return mean
squarelist=[]    
for t in data:
    a=int(t)-mean(data)
    a=a**2  
    squarelist.append(a)
total=0    
for d in squarelist:
    total=total+d
result=total/(len(data)-1)
std_dev=math.sqrt(result)
print("the stabdard deviation of the data items is"+str(std_dev))






