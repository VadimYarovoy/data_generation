import matplotlib.pyplot as plt

values = list(range(1, 1001))
squares = [x ** 2 for x in values]

plt.style.use('seaborn')

fig, ax = plt.subplots()
#ax.plot(values, squares, linewidth=3)
#ax.scatter(2, 4, s=200)
ax.scatter(values, squares, c=squares, cmap=plt.cm.Blues, s=10)

ax.set_title("Diagram", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

ax.axis([0, 1100, 0, 1100000])

#plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')
