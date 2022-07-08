import pandas as pd

pd.options.display.max_rows = 9999

df = pd.read_csv('data.csv')
df = pd.DataFrame(df)

table = '`game_list`'
type_ = '1'
provider_id = '33'
provider_name = 'QS'
lang_code = 'G00100'
status = '1'
created = '2021-08-26 12:39:14'
img = 'abc.jpg'
sym = "'"
a = "` ( `"

def game(name,code):

  
  print('INSERT INTO',table,'(','`id`',',','`name`',',','`code`',',','`type`',',','`provider_id`',',','`provider_name`',',','`lang_code`',',','`status`',',','`created`',',','`img`',')','VALUES',
'(','NULL',',',repr(name),',',repr(code),',',repr(type_),',',repr(provider_id),',',repr(provider_name),',',repr(lang_code),',',repr(status),',',repr(created),',',repr(img),')',';')
 
  # print(',',repr(name),',')

for row in df.itertuples():
    game(row.name,row.code)
    
    # print(row.name,row.code)
   
# print(df) 
# isinstance([df], list)

f = open("test.txt", "w")
f.write(row.name)
f.close()

a = '222'
b = '333'



# game("122","2")
# game("77","6")


