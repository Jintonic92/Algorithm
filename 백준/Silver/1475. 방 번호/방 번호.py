word = int(input())

all_list = [0] * 11

word_str = str(word)

for w in word_str:
  n = int(w)

  if n == 6 or n == 9:
    if all_list[6] < all_list[9]:
      all_list[6] += 1
    else: all_list[9] += 1
  
  else:
    all_list[n] += 1

print(max(all_list))