import csv
import matplotlib.pyplot as plt


def encontrar(path, name):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    capish = filter(lambda x: x[2] == name, reader)
    capish = next(capish)
  print(capish)
  label = ["70", "80", "90", "2000", "2010", "2020"]
  val = []
  
  for i in range(12,6,-1):
    val.append(int(capish[i])/1000000)
      
  print(val)
  return label,val


if __name__ == "__main__":
  label, val = encontrar("data.csv", "China")

  def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig("countryChard.png")

  generate_bar_chart(label, val)






