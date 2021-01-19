def key_value_accessing():
  # car is a dict and we need to access to each key and the value of this dictionary
  car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "color": {
        "blue": "Dark",
        "green": "Dark","Leight",
        "pink": "Dark","Leight", "Bright"
     }
  }
  
  # First, get the dict_values class which includes keys of the dictionary to understand what values() method will return
  # dict_value class will be as: dict_values(['Ford', 'Mustang', 1964])
  x = car.values()
  print(x)
  # you can see the type of x --> "class"
  print(type(x))
  
  # Then, get the dict_keys class to see what are values of the dict and to understand what values() method will return
  # dict_value class will be as: dict_keys(['brand', 'model', 'year'])
  y = car.keys()
  print(y)
  # you can see the type of x --> "class"
  print(type(y))
  
  # Now we can find each key-value pairs as elements of a tuple
  
  # For the first key-value pair:
  print(list(car.items())[0])  # this print returns ('brand', 'Ford')
  print((list(car.items())[0])[1]) # this print returns 'Ford'
  
  # For the second key-value pair:
  print(list(car.items())[1])  # this print returns ('model', 'Mustang')
  print((list(car.items())[1])[1]) # this print returns 'Mustang'
  
  # For the last key-value pair:
  print(list(car.items())[2])  # this print returns ('year', '1964')
  print((list(car.items())[2])[1])  # this print returns '1964'
  
  # Sometimes there will be nested dictionaries which include a dictionary inside of the another dictionary
  nested_dict = list(car.items())[3]  # this print returns the dictionary called "color"

if __name__ == '__main__':
  call_func = key_value_accessing()
  call_func.run()
