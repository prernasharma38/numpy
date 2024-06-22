import numpy as np
import matplotlib.pyplot as plt

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# x = np.mean(speed)
# print(x)

x = np.median(speed)
# print(x)

speed = [86,87,88,86,87,85,86]
y = np.std(speed)
print(y)

print("hello world")

# print(y)

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

x = np.percentile(ages, 55)
# print(x)

x = np.random.uniform(0.0, 5.0, 250)
# print(x)

# histogram***
x = np.random.uniform(0.0, 5.0, 250)
# plt.hist(x, 5)
# plt.show()

x = np.random.uniform(0.0, 5.0, 100000)
# plt.hist(x, 100)
# plt.show()

x = np.random.normal(5.0, 1.0, 100000)

# plt.hist(x, 100)
# plt.show()

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# plt.xlabel("Age of cars")
# plt.ylabel("speed of cars")

# plt.scatter(x, y)
# plt.show()

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

plt.xlabel("x= /mean value 5.0, sd= 1.0")
plt.ylabel("y= /mean value 10.0, sd= 2.0")
plt.scatter(x, y)
plt.show()
