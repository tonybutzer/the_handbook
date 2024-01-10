import boto3
import pickle
import pandas as pd
import sys

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

person='butz'
try:
    person=sys.argv[1]
except:
    pass

print(sys.argv)
print(person)

ec2 = boto3.client('ec2',  region_name='us-west-2')
response = ec2.describe_instances()


filename='price_prune.pickle'
infile = open(filename,'rb')
df = pickle.load(infile)
infile.close()


def return_price(data_frame, instance_type):
    wdf = data_frame[(data_frame['Instance Type'] == instance_type)]
    #print(wdf)
    instance_price = wdf.iloc[0].PricePerUnit
    return(instance_price)


instance_list=[]
for i in range(len(response["Reservations"])):
    #print(i)
    try:
        tags = response['Reservations'][i]['Instances'][0]['Tags']
        #print(tags)
    except:
        pass
    name='BOGUS_NILL'
    for j in range(0,len(tags)):
        key = tags[j]['Key']
        if (key == 'Name'):
            value_name = tags[j]['Value']
            #print(key)
            #print(value_name)
            name=value_name
            break
    if name.startswith(person):
        ip='x.x.x.x'
        try:
            ip = response['Reservations'][i]['Instances'][0]['PrivateIpAddress']
        except:
            pass
        i_type = response['Reservations'][i]['Instances'][0]['InstanceType']
        hr_cost = return_price(df, i_type)
        state=response['Reservations'][i]['Instances'][0]['State']['Name']
        monthly_cost = hr_cost * 365 * 24 / 12


        item={
            'state': state,
            'name': name,
            'ip': ip,
            'i_type': i_type,
            'monthly_cost': monthly_cost
        }
        instance_list.append(item)

cdf = pd.DataFrame(instance_list)

print(cdf)

print('==='*30)
print('==='*30)

rdf=cdf[(cdf['state'] == 'running')]

print(rdf)
print('==='*40)
print('==='*40)
