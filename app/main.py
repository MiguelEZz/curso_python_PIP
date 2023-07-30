import mod

data = [{
  "country": "colombia",
   "population": 500
  }, {
   "country": "peru",
   "pupulation": 23
 }]
def run():
  keys, values = mod.get_population()
  print(keys, values)
  print("caca")
 
  
  result = mod.populartion_country(data, "colombia")
  print(result)
  
  