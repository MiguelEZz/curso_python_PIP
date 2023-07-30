
import matplotlib.pyplot as plt

def generate_pie_chards():
    labels = ["a","b","c"]
    values = [1,2,3]

    fig, ax = plt.subplots()
    ax.pie(values, labels)
    plt.savefig("pie.png")
    plt.close()