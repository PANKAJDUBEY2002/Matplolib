# import pyplot
from matplotlib import pyplot as plt



# set graph prop
days=[1,2,3,4,5,6,7]
study=[5,10,15,20,6,9,22]
phone=[4,8,3,2,1,3,1]
sleep=[1,2,2,1,3,3,1]
other=[14,4,4,1,14,9,0]
lbs=['study','phone','sleep','other']
plt.stackplot(days,study,phone,sleep,other,labels=lbs)
plt.xlabel('Days')
plt.ylabel('Activities')
plt.title('Your Performance')
plt.legend()




#show graph

plt.show()
