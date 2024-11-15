import csv 
with open(r"C:\Users\adith\Desktop\_\BSC work\Week 1-2\testingdata.csv",'r') as csv_TrainingData: 
    csv_TestData = csv.reader(csv_TrainingData) 
    x = 0 
    y = 0 
    next(csv_TestData) 
    for line in csv_TestData: 
        if line[3] == line[4]: 
            x += 1 
        y += 1 
print(x) 
print(y) 
print(((x/y) * 100) , "%")