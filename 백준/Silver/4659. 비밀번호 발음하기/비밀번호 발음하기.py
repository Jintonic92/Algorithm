while True :
  word = input()

  if word == 'end':
    break 
  
  has_v = False
  is_v = 0
  is_c = 0 
  is_valid = True 
  
  for i in range(len(word)):
    w = word[i]

    if w in 'aeiou':
      has_v = True
      is_v += 1
      is_c = 0 
    
    else :
      is_v = 0
      is_c += 1
    
    if is_c > 2 or is_v > 2:
      is_valid = False
    
    if i > 0 and word[i-1] == word[i]:
      if w not in 'eo':
        is_valid = False
  
  if has_v == False:
    is_valid = False
  
  if is_valid == True:
    print(f"<{word}> is acceptable.")
  
  else :
    print(f"<{word}> is not acceptable.")
