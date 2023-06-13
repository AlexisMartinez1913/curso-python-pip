import matplotlib.pyplot as plt

def generate_var_chart(name, labels, values):
  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'app/imgs/{name}.png')
  plt.close()

def generate_pie_chart(labels,values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig('./app/pie.png')
  plt.close()
  

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [100,40,90]
  generate_var_chart(labels, values)
  #generate_pie_chart(labels,values)