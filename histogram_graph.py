# import pyplot
from matplotlib import pyplot as plt



#set graph prop
test=[1,2,3,4,5,6,7,8,9,10]
marks1=[10,20,30,40,50,60,65,70,95,100]
bins=[0,30,70,100]
plt.hist(marks1,bins,histtype='bar',rwidth=1)
plt.legend()






#show graph

plt.show()
