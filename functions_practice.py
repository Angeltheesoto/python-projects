def hello():
 return 'How are you?'

def pack(one, two, three):
 return [one, two, three]

def eat_lunch(my_list):
 if len(my_list) == 0:
  return ('My lunchbox is empty')
 if len(my_list) > 0:
  return (f'First I eat {my_list[0]}')
 else:
  return (f'Next I eat {my_list[1]}')
  

print(hello())
print(pack('apple', 'banana', 'strawberry'))
print(eat_lunch(['Cookie', 'ice cream']))