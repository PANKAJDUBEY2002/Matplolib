# import pyplot
from matplotlib import pyplot as plt



#set graph prop
test=[1,2,3,4,5]
data=[14,35,76,32,87]
pankaj=[23,12,34,64,13]
plt.scatter(test,data,label='Data',c='b',marker='*')
plt.scatter(test,pankaj,label='Pankaj',c='r')
plt.legend()









#show graph
plt.show()
