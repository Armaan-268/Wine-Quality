import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing Data
data = pd.read_csv('dataset.csv')
# Plot_1
y = data.iloc[:,0].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Fixed Acidity')
plt.show()

# Plot_2
y = data.iloc[:,1].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Volatile Acidity')
plt.show()

# Plot_3
y = data.iloc[:,2].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Citric Acid')
plt.show()

# Plot_4
y = data.iloc[:,3].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Residual Sugar')
plt.show()

# Plot_5
y = data.iloc[:,4].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Chlorides')
plt.show()

# Plot_6
y = data.iloc[:,5].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Free Sulphur-dioxide')
plt.show()

# Plot_7
y = data.iloc[:,6].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Total Sulphur-dioxide')
plt.show()

# Plot_8 
y = data.iloc[:,7].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Density')
plt.show()

# Plot _9
y = data.iloc[:,8].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. pH')
plt.show()

# Plot_10
y = data.iloc[:,9].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Sulphates')
plt.show()

# Plot_11
y = data.iloc[:,10].values
x = data.iloc[:,-1].values
avg = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(y)):
        if x[i] == j:
            temp.append(y[i])
    average = sum(temp)/len(temp)
    avg.append(average)
plt.plot(l,avg)
plt.xlabel('Wine Quality')
plt.ylabel('Avg. Alcohol')
plt.show()


# Plot_12
x = data.iloc[:,-1].values
slices = []
s = set(x)
l = list(s)
for j in l:
    temp = []
    for  i in range (1,len(x)):
        if x[i] == j:
            temp.append(y[i])
    #total = sum(temp)
    slices.append(len(temp))
quality = s
color= ['y','b','c','r','g','c']
plt.pie(slices,labels=quality,colors=color,shadow=False,explode=(0,0,0,0.1,0,0),autopct='%1.1f%%',radius=1,startangle=90)
plt.title('Pie Chart')
plt.show()