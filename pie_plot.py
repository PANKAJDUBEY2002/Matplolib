# import pyplot
from matplotlib import pyplot as plt



#defiine a function which return the average of list


def avg(l):
    s=0
    for i in l:
        s=s+i
    a=s/len(l)
    return a



# set graph prop
days=[1,2,3,4,5,6,7]
study=[5,10,15,20,6,9,22]
phone=[4,8,3,2,1,3,1]
sleep=[1,2,2,1,3,3,1]
other=[14,4,4,1,14,9,0]
hrs=[avg(study),avg(phone),avg(sleep),avg(other)]
lbs=['study','phone','sleep','other']
plt.pie(hrs,labels=lbs,explode=(0,0.1,0,0))

plt.title('Pie chart')





#show graph

plt.show()
