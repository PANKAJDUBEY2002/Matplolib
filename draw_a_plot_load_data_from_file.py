# import pyplot and csv module
from matplotlib import pyplot as plt
import csv


test=[]
marks=[]

#load data from text file

with open('data.txt','r') as file:
    plots=csv.reader(file,delimiter=',')
    for row in plots:
        test.append(int(row[0]))
        marks.append(int(row[1]))

#show graph
plt.plot(test,marks)
plt.xlabel("test")
plt.ylabel("marks")
plt.title("test vs marks")
plt.show()
