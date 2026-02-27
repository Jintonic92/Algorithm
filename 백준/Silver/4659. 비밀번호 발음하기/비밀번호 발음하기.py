while True:
  word = input()

  if word == 'end':
    break
  
  has_v = False
  cnt_v = 0
  cnt_c = 0
  is_valid = True

  for i, w in enumerate(word):
    if w in 'aeiou':
      has_v = True
      cnt_v += 1
      cnt_c = 0
    
    else:
      cnt_c += 1
      cnt_v = 0
    
    if cnt_c > 2 or cnt_v > 2:
      is_valid = False
    
    if i > 0 and word[i-1] == word[i]:
      if w not in 'oe':
        is_valid = False

  if has_v == False:
    is_valid = False
  
  if is_valid :
    print(f"<{word}> is acceptable.")
  else:
    print(f"<{word}> is not acceptable.")
