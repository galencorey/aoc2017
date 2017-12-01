input_file = open('day1input.txt', 'r')
input = input_file.read()

def addAllIfDuplicate(list, frac = None):
  #take a list of ints and sum the ones that are equal to the next one
  sum = 0
  length = len(list)
  step = length / frac if frac else 1

  for i in range(length):
    if list[i] == list[(i+step)%length]:
      sum += list[i]
  return sum

def splitStringByDigit(str):
  #turn a string of numbers into a list of each digit as an int
  digits = []
  for d in str: 
    digits.append(int(d))
  return digits

# print(addAllIfDuplicate(splitStringByDigit('1122')))
# print(addAllIfDuplicate(splitStringByDigit('1111')))
# print(addAllIfDuplicate(splitStringByDigit('1234')))
# print(addAllIfDuplicate(splitStringByDigit('91212129')))

print(addAllIfDuplicate(splitStringByDigit(input), 2))