import matplotlib.pyplot as plt

scores = [59, 52, 96, 87, 46, 65, 68, 54, 86, 48, 63, 77]

plt.hist(scores, bins=5, color='skyblue', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of students')
plt.title('Score distribution of students')
plt.show()