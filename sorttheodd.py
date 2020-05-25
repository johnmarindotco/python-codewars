
def sort_array(source_array):
    final = []
    indexes4evens = []
    values4evens = []
      
    for index, value in enumerate(source_array):
      if value % 2 != 0:
        final.append(value)
        final.sort()
      elif value % 2 == 0:
        indexes4evens.append(index)
        values4evens.append(value)
    
    i = 0
    for element in indexes4evens:
      final.insert(indexes4evens[i], values4evens[i])
      i = i + 1
      
    return(final)

# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on their places.
# Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.
# Example
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
# User: fyvfyv