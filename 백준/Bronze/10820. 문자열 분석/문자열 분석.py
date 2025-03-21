while True :
  try : 
    sent =  input()
    is_lower, is_upper, is_digit, is_space = 0, 0, 0, 0
    for each in sent:
      if each.islower(): is_lower += 1
      elif each.isupper() : is_upper += 1
      elif each.isdigit() : is_digit += 1
      else : is_space += 1

    print(is_lower, is_upper, is_digit, is_space)
  except EOFError:
    break