
while True:
  word = input()
  v_cnt = 0
  c_cnt = 0
  is_good = True
  has_v = False

  if word == 'end':
    break

  for i in range(len(word)):
    
    w = word[i]
  
    if w in 'aeiou':
      has_v = True
      c_cnt += 1
      v_cnt = 0
    
    else:
      c_cnt = 0
      v_cnt += 1
    
    if c_cnt > 2 or v_cnt > 2:
      is_good = False
      break
    
    if i > 0 and word[i-1] == word[i]:
      if word[i] not in 'eo':
        is_good = False
        break
    
  if has_v == False:
    is_good = False

  if is_good != True:
    print(f"<{word}> is not acceptable.")
  else:
    print(f"<{word}> is acceptable.")
    


        