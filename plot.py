# import pyplot
from matplotlib import pyplot as plt


#set graph prop
x=[1,2,3,4,5]
y1=[23,13,56,45,100]
y2=[13,76,23,97,54]
plt.plot(x,y1,label='Data')
plt.plot(x,y2,label='Pankaj')
plt.xlabel("Test")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.legend()




#show graph
plt.show()
