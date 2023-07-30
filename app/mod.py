def get_population():
  keys = ["colombia", "bol"]
  values = [300, 400]
  return keys,values

def populartion_country(data, country):
  result = list(filter(lambda item: item["country"] == country, data))
  return result