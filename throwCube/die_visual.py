from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


die = Die()
results = []

for throw_num in range(1000):
    result = die.throw()
    results.append(result)

d = dict()

for value in range(1, die.sides + 1):
    d[str(value)] = results.count(value)

print("Frequency:")
for k, v in d.items():
    print(f'{k} was {v} times')

x_values = list(range(1, die.sides + 1))
data = [Bar(x=x_values, y=list(d.values()))]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
