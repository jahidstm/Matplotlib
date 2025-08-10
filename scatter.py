import matplotlib.pyplot as plt

hour = [1,2,3,4,5,6,7,8,9]
score = [10,20,30,25,15,35,45,40,50]

plt.scatter(hour, score, color='red', marker='o', label='Student Data')
plt.xlabel('Total hour')
plt.ylabel('Scores')
plt.title('Relationship between study time and scores')
plt.legend()
plt.grid()
plt.show()