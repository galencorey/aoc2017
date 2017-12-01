input_file = open('day1input.txt', 'r')
input = input_file.read()

def addAllIfDuplicate(list):
  #take a list of ints and sum the ones that are equal to the next one
  sum = 0
  length = len(list)
  for i in range(length):
    if list[i] == list[(i+1)%length]:
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

print(addAllIfDuplicate(splitStringByDigit(input)))