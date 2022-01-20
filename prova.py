import numpy as np
import matplotlib.pyplot as plt

alfa=1
beta=0.02
delta=0.01
gamma=1


x, y = np.meshgrid(np.arange(0,1000, 0.1), np.arange(0, 225, 0.1))
xdot = alfa*x - beta*x*y
ydot = delta*x - gamma*y

plt.streamplot(x, y, xdot, ydot)
#plt.plot(0,0,marker="o", color="red")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sistema non linearizzato")
plt.grid()
plt.show()