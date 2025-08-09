import matplotlib.pyplot as plt

product = ['A', 'B', 'C', 'D']
sales = [1000, 2000, 1500, 2200]

plt.bar(product, sales, color = 'orange', label = 'sales 2025')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.title('Product sales comparision')
plt.legend()
plt.show()