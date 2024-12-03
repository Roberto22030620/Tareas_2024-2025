import random, math
import matplotlib.pyplot as plt

x=[]
y=[]
for i in range(50):
    x.append(random.randint(1,10))
    y.append(random.randint(1,10))

cx=random.randint(1,10)
cy=random.randint(1,10)
print(f"Centro x: {cx} Centro y: {cy}")
plt.scatter(cx,cy,marker='X',color='red')
for j in range (50):
    xr=cx-x[j]
    yr=cy-y[j]
    e=math.sqrt((xr**2)+(yr**2))
    if (e<=3):
        print(f"Valores de euclides: {e}")
        plt.scatter(x[j],y[j],color='blue')
plt.show()