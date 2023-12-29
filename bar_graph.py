# import pyplot
from matplotlib import pyplot as plt



#set graph prop
test=[1,2,3,4,5]
marks1=[13,42,12,67,430]
marks2=[124,23,56,345,789]
plt.bar([i+0.1 for i in test],marks1,width=0.2,label='data')
plt.bar([i-0.1 for i in test],marks2,width=0.2,label='pankaj')
plt.legend()






#show graph

plt.show()
