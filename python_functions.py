def sum_to(n):
  x = 0
  total = 0
  while x < n:
    x +=1
    total += x
  print(total)

sum_to(6)
sum_to(10)

def largest(nums):
  largest =0 
  for num in nums:
    if num > largest:
      largest = num
  print(largest)

largest([1, 2, 3, 4, 0])
largest([10, 4, 2, 231, 91, 54]) 

def occurrences(str1, str2):
  print(str1.count(str2))

occurrences('fleep floop', 'e')   # returns 2
occurrences('fleep floop', 'p')   # returns 2
occurrences('fleep floop', 'ee')  # returns 1
occurrences('fleep floop', 'fe')  # returns 0