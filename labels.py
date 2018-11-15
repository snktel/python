
num = []
for i in range(1, 10):
    num.append(input('Scan the label: '))

print(num)

with open("labels.txt","w+") as f:
    for s in num:
        f.write(str(s) +"\n")
f.close()




#label1 = input("Scan label1: ")
#label2 = input("Scan label2: ")
from typing import TextIO



#f.write(input("Scan Label: ") + '\n')
#f.write(label2 + '\n')
#f.close()



