import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig("bar.png")
  plt.close()


def generate_pie_chard(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis("equal")
  plt.savefig("pie.png")
  plt.close()


if __name__ == "__main__":
  labels = ["p", "c", "k"]
  values = [98, 333, 109]
  generate_bar_chart(labels, values)
