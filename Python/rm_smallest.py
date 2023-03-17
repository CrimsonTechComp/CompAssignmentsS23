# Define a function that takes a dictionary as a parameter and returns a modified dictionary
def remove_smallest(dict):
  # If the dictionary is empty, return it as it is
  if not dict:
    return dict
  # Find the minimum value in the dictionary
  min_value = min(dict.values())
  # Find the key that corresponds to the minimum value
  min_key = None
  for k, v in dict.items():
    if v == min_value:
      min_key = k
      break
  # Remove the key-value pair from the dictionary
  dict.pop(min_key)
  # Return the modified dictionary
  return dict

# Sample dictionary
sampleDict = { 'Physics': 82, 'Math': 65, 'history': 75 }

result = remove_smallest(sampleDict)
print(result)