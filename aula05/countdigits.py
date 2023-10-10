def countDigits(str):
   count = 0
   for char in str:
      if char.isdigit():
         count += 1
   return count 