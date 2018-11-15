
rack = input("Scan barcode on working Rack: ")

print(rack)

n = int(input("How many boxes are you going to deploy? "))

labels = []
for i in range(0, n):
    labels.append(input('Scan the label: '))

print(labels)

with open("labels.txt","w+") as f:
    for s in labels:
        f.write(str(s) +"\n" "\n")

f.close()




#label1 = input("Scan label1: ")
#label2 = input("Scan label2: ")
from typing import TextIO



#f.write(input("Scan Label: ") + '\n')
#f.write(label2 + '\n')
#f.close()



