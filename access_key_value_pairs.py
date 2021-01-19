def key_value_accessing():
  # car is a dict and we need to access to each key and the value of this dictionary
  car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  
  # First, get the dict_values class to see what are values of the dict and to understand what values() method will return
  # dict_value class will be as: dict_values(['Ford', 'Mustang', 1964])
  x = car.values()
  print(x)
  # you can see the type of x --> "class"
  print(type(x))
  y = car.keys()
  print(y)
  print(list(car.items())[0])
  print((list(car.items())[0])[1])

if __name__ == '__main__':
  call_func = key_value_accessing()
  call_func.run()
