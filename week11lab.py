# takes list of numbers
# prints each number and the double of their value
def print_doubles(nums):
  for n in nums:
    print(f"Double of {n} is {n*2})
          
print_doubles([1,2,3,4,5])
          
        
# takes a string
# returns dictionary of frequencies of each letter
def get_freq(str):
  letter_freq = {}
  for letter in str:
    letter_freq[letter] = letter_freq[letter] + 1
  return letter_freq
          
str = "The quick brown fox jumped over the slow lazy dog"
freq = get_freq(str)
print(freq)
  
# takes a dictionary of file sizes
# prints sum of total size
def total_size(filesizes):
   for f in filesizes:
     totalsize = 0
     totalsize += filesizes[f]

filesizes = {"text.txt" : 45, "ps4.py": 70, "hw9.pdf": 32}
tot_size = total_size(filesizes)
print(tot_size)
         
