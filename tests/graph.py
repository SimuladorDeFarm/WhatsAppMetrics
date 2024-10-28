import matplotlib.pyplot as plt

# data array for axis y
y = [10, 20, 15, 30, 25]

# x axis will be index of each element of y array
x = range(len(y))

# Create Graph
plt.plot(x, y, marker='o')

# labels of axis
plt.xlabel('Posiciones (índice)')
plt.ylabel('Valores (eje Y)')

# Graph title
plt.title('Gráfico de X vs Y')

# print Graph
plt.show()