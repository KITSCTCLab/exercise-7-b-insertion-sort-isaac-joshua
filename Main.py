from typing import List


  # Write your code here
  for i in range(len(array)):
    u=array[i]
    j=i-1
    while(j>=0 and array[j]>u):
      array[j+1] = array[j]
      j=j-1
    array[j+1] = u
    

# data = [9, 5, 1, 4, 3]
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
insertionSort(data)
print(data)

