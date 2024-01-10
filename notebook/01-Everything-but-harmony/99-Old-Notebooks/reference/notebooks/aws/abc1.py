import pandas

df = pandas.read_csv('awsLink/workCopy.csv', sep=',')

n1 =  df.columns

subset = df[['Location', 'Instance Type', 'vCPU', 'Operating System', 'Instance Family', 'Tenancy', 'Memory', 'LeaseContractLength', 'Unit', 'PricePerUnit', 'TermType', 'Currency', 'PurchaseOption']] # subset multiple columns

print (subset.shape)

subset['Tenancy'].value_counts()

#pick_type = "t2.nano"
#pick_type = "t2.micro"
#pick_type = "t2.small"
pick_type = "t2.large"

pick_list = ['t2.nano', 't2.micro', 't2.small', 't2.large']

for pick in pick_list:
  print(pick)
  pick_type=pick

  print ("_______________________________________________________________")
  print ("PICK is", pick_type)
  t2_nano=subset[subset['Instance Type'] == pick_type]

  t2_nano[:6]

  t2_nano.columns

  t2_nano_jr = t2_nano[['Location', 'Operating System', 'LeaseContractLength', 'Unit', 'PricePerUnit', 'Currency','PurchaseOption']]

  t2_nano_1yr=t2_nano_jr[t2_nano_jr['LeaseContractLength'] == "1yr"]

  t2_nano_1yr_linux=t2_nano_1yr[t2_nano_1yr['Operating System'] == "Linux"]

  t2_nano_tony=t2_nano_1yr_linux[t2_nano_1yr_linux['Unit'] == "Quantity"]

  t2_s = t2_nano_tony.sort_values('Location')

  t2_a = t2_s[t2_s['PurchaseOption'] == "All Upfront"]

  t2_f = t2_a[['Location', 'PricePerUnit']]

  t2_cheap = t2_f.sort_values('PricePerUnit')

  print ("TABLE is ",t2_cheap)

