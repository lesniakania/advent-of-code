import re

def distance(list1, list2):
  sum = 0

  list1.sort()
  list2.sort()

  for i in range(0,len(list1)):
    sum += abs(list1[i]-list2[i])

  return sum

def similarity(list1, list2):
  map = {}

  sum = 0
  for i in range(0,len(list2)):
    if list2[i] in map:
      map[list2[i]] += 1
    else:
      map[list2[i]] = 1

  for i in range(0,len(list1)):
    number = list1[i]
    sum += number * map.get(number, 0)

  return sum

def read_input(file_name = 'input.txt'):
  list1 = []
  list2 = []
  
  with open(file_name, 'r') as file:
    for line in file:
      element1, element2 = re.split(r"\s+", line.strip())
      list1.append(int(element1))
      list2.append(int(element2))
      
  return (list1, list2)

list1, list2 = read_input()
print(distance(list1, list2))
print(similarity(list1, list2))
