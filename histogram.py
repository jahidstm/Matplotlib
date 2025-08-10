import matplotlib.pyplot as plt

scores = [54, 86, 48, 63, 77, 50, 99, 59, 52, 96, 52, 46, 88, 68, 67, 92]

plt.hist(scores, bins=5, color='lightgreen', edgecolor='black')
plt.xlabel('Score Range')
plt.ylabel('Number of students')
plt.title('Score distribution of students')
plt.show()