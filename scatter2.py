import matplotlib.pyplot as plt

hour = [1,2,3,4,5,6,7,8]
score1 = [10,20,30,25,15,35,45,40]
score2 = [20,30,10,25,15,40,35,45]

plt.scatter(hour, score1, color='red', marker='o', label='Class A')
plt.scatter(hour, score2, color='blue', marker='o', label='Class B')

plt.xlabel('Total hour')
plt.ylabel('Scores')
plt.title('Relationship between study time and scores')
plt.legend()
plt.grid()
plt.show()