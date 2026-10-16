import matplotlib.pyplot as plt

labels = ["Apple", "Banana", "Orange", "Grape"]
sizes = [30, 25, 20, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Fruit Distribution")
plt.show()
