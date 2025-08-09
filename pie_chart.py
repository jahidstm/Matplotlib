import matplotlib.pyplot as plt

department = ['CSE', 'SWE', 'MCT', 'CIS']
students = [900, 1200, 600, 480]

plt.pie(students, labels = department, autopct='%1.1f%%', colors=['orange', 'lightgreen', 'skyblue', 'coral'])
plt.title('Percentage by department')
plt.show()