import csv 
with open(r"C:\Users\adith\Desktop\_\BSC work\Week 1-2\testingdata.csv",'r') as csv_TestData:
    csv_TestData = csv.reader(csv_TestData)
    x=0
    y=0
    next(csv_TestData)
    for line in csv_TestData:
            if line[3] == line[4]:
                x=x+1
            else:
                x=x
    y=y+1          
        
print(x)
print(y)
print((x/y) * 100 ,"%")

