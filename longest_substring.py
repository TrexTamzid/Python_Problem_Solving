
def longest_unique_substring(s):
  seen =set()
  left = 0
  max_length =0
  start_index =0

  for right in range(len(s)):
    while s[right] in seen:
      seen.remove(s[left])
      left +=1

    seen.add(s[right])

    if right -left +1 > max_length:
        max_length = right -left +1
        start_index = left

  return s[start_index:start_index+max_length]

if __name__ == "__main__":
   s = input("Enter a string")
   result = longest_unique_substring(s)
   print("Longest substring without repeating characters:",result)
   print("length:",len(result))