
def move_zeros(array):
    final = []

    counter = 0
    for element in array:
      if element == 0 and element is not False:
        counter = counter + 1
      else:
        final.append(element)

    zeros = [0] * counter
    final.extend(zeros)
    return(final)

# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.
# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
# User: xcthulhu