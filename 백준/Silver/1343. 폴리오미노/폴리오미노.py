# all_list = input().split('.')
# all_list = [x for x in all_list if x != '']
all_list = input()
all_list = all_list.replace('XXXX', 'AAAA')
all_list = all_list.replace('XX', 'BB')

if 'X' in all_list:
  print(-1)
else:
  print(all_list)
