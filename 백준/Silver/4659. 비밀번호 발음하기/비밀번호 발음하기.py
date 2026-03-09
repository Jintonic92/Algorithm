while True:
  word = input()
  has_v = False
  is_v = 0
  is_c = 0 
  is_valid = True 

  if word == 'end':
    break 
  
  for i in range(len(word)):
    w = word[i]

    if w in 'aeiou':
      has_v = True
      is_v += 1
      is_c = 0 
    
    else:
      is_c += 1
      is_v = 0 
    
    if is_v > 2 or is_c > 2:
      is_valid = False
    
    if i > 0 and is_v >= 2 or is_c >= 2:
      if word[i] == word[i-1]:
        if word[i] not in 'eo':
          is_valid = False

  if not has_v:
    is_valid = False
  
  if is_valid == False:
    print(f"<{word}> is not acceptable.")
  else:
    print(f"<{word}> is acceptable.")
