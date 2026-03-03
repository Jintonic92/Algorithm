while True :
  word = input()

  if word == 'end':
    break
  
  v_cnt = 0
  has_v = False
  c_cnt = 0
  is_good = True

  for idx, w in enumerate(word):
    if w in 'aeiou':
      has_v = True
      v_cnt += 1
      c_cnt = 0
    
    else:
      c_cnt += 1
      v_cnt = 0
    
    if c_cnt > 2 or v_cnt > 2:
      is_good = False
      break
    
    if idx > 0 and word[idx] == word[idx -1]:
      if word[idx] not in 'eo':
        is_good = False 
        break
  
  if has_v == False:
    is_good = False
  
  if is_good == False:
    print(f"<{word}> is not acceptable.")
  
  else :
    print(f"<{word}> is acceptable.")
