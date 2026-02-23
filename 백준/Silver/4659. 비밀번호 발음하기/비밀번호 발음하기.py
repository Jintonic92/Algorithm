while True:
  word = input()

  if word == 'end':
    break

  vowels = ['a', 'e', 'i', 'o', 'u']
  has_vowel = False
  v_cnt = 0
  c_cnt = 0 
  accept = True

  for i in range(len(word)):

    if word[i] in vowels:
      has_vowel = True
      v_cnt += 1
      c_cnt = 0 
    
    else:
      v_cnt = 0
      c_cnt += 1

    
    if v_cnt > 2 or c_cnt > 2:
      accept = False
      break
    
    
    if i > 0 and word[i-1] == word[i]:
      if word[i] not in 'eo':
        accept = False
        break 

  if has_vowel == False:
    accept = False 

  if accept == False:
    print(f"<{word}> is not acceptable.")
  else:
    print(f"<{word}> is acceptable.")


      


    