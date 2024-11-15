import csv 
from matplotlib import pyplot as plt

n = 0
h = 0
fu = 0
fe = 0
s = 0
an = 0
dis = 0

with open(r"C:\Users\adith\Desktop\_\BSC work\Week 1-2\RawData.csv",'r', encoding='utf-8') as csv_TestingData:
    csv_Rawdata= csv.reader(csv_TestingData)

    next(csv_Rawdata)
    for line in csv_Rawdata:
        line2 = int(line[2].strip())
        if line2 == 0:
            n += 1
        elif line2 == 1:
            h += 1
        elif line2 == 2:
            fu += 1
        elif line2 == 3:
            fe += 1
        elif line2 == 4:
            s += 1
        elif line2 == 5: 
            an += 1
        elif line2 == 6: 
            dis += 1


slices = [n, h, fu, fe, s, an, dis]
labels = ['Neutral', 'happy/pleased', 'funny', 'fear', 'sadness', 'anger', 'disguist']

plt.pie(slices, labels=labels, startangle=90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title("Proportion of sentiments")
plt.tight_layout()
plt.show()
