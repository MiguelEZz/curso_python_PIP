import csv

def read_csv(path):
  with open(path,"r") as csvfile:
    reader = csv.reader(csvfile, delimiter =",")
    header = next(reader)
    data = []
    for row in reader:
      iterable = zip(header, row)
      coutry_dict = {key: value for key, value in iterable}
      print(coutry_dict)
      data.append(coutry_dict)

if __name__ == "__main__":
  read_csv("data.csv")