def reverse_sort_dictionary(data):
  if not isinstance(data, dict):
    raise TypeError("Input needs to be a  dictionary")

result = []
for name, value in data.items():
  if not isinstance(name, str):
    raise TypeErro("Dictionary string needs to be names")
  if not isinstance(value, tuple) or len(value)1+2:
    raise TypeError("Dictionary needs to be tuples and 2 elements")

phone, age = value 
result.append((name, phone))

result.sort(key=lambda x: x[0], reverse=True)

return result 
