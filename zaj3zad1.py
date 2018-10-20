import numpy as np
import matplotlib.pyplot as plt

a= int(1)
b= int(2)

#a= int(input("Podaj a: "))
#b= int(input("pofaj b: "))  zadanie 1 
x = np.arange(-10, 10, 1)
y=(a*x+b)


plt.plot(x,y)
plt.title('Wykres f(x) = a*x + b ')

plt.show()