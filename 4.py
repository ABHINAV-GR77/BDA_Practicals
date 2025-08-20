#Create a List of Lists
dataset=[["Cars","BMW","GTR","MClaren"],
         ["Colors","Black","Grey","Orange"],
         ["Models","M5","Nissan","P100"]]

#convert list into Dictionary
new={item[0]:item[1:] for item in dataset}
print("Converted Dictionary : ",new)