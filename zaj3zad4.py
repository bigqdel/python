import numpy as np
import matplotlib.pyplot as plt


#a= int(input("Podaj a: "))
a=int (1)
b=int (-3)
c= int(1)
x = np.arange(-10, 10, 1)
#x2 =np.arange (0,10,0.5)


y=(a*x*x + b*x + c)
#y2=(x2*x2/3)


plt.plot(x,y)
plt.title('f(x) = a*x^2 + b*x + c')
plt.xlabel ('x')
plt.ylabel ('y')

plt.show()