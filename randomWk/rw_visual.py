import matplotlib.pyplot as plt

from random_walking import RandomWalk

while True:
    number = int(input('Points: '))
    rw = RandomWalk(number)
    rw.fill_walk()

    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))

    point_num = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_num,
               cmap=plt.cm.Blues, edgecolor='none', s=15)

    ax.scatter(0, 0, c='green', edgecolor='none', s=50)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolor='none', s=50)

    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    stop = input('More random? (y/n): ')
    if stop == 'n':
        break