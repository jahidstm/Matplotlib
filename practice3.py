import matplotlib.pyplot as plt

months = [1, 2, 3, 4]
sales = [1000, 1500, 2500, 2000]

plt.plot(months, sales, color='red', linestyle='--', linewidth=2, marker='o', label='2025 sales data')
plt.xlabel("Months")
plt.ylabel("Sales data")
plt.legend(loc='upper left', fontsize=12)
plt.grid(color='gray', linestyle=':', linewidth=1)

plt.xlim(1,4)
plt.ylim(1,3000)
plt.xticks([1,2,3,4],['M1','M2','M3','M4',])
plt.yticks([1000, 1500, 2500, 2000],['S1','S2','S3','S4',])

plt.show()