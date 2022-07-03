inputs = [1, 2, 3]

output = [[]]

for input in inputs:
  output.append([input])

for first_ind in range(len(inputs)):
  growing_thing = inputs[first_ind]
  for ii in range(len(inputs)):
    if ii != first_ind:
      [num_1, inputs[ii]]
      output.append()

growing_thing = inputs[0]
leftovers = inputs[1:]

while len(leftovers) > 0:
  for leftover in leftovers:
    growing_thing.append(leftover)
  


print(output)