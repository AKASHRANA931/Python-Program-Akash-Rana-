import matplotlib.pyplot as plt

x = [i for i in range(10)]
y = [i*i for i in range(10,20)]
z = [i**8 for i in range(10,20)]

plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2,1,2)
plt.plot(x,z)
plt.show()