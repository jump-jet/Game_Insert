import pandas as pd
import sys
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

pd.options.display.max_rows = 999

df = pd.read_csv('data.csv')
df = pd.DataFrame(df)

table = '`game_list`'
type_ = '1'
provider_id = '33'
provider_name = 'QS'
lang_code = 'G00100'
status = '1'
img = 'abc.jpg'
sym = "'"
a = "` ( `"

def game(name,code):

  print('INSERT INTO',table,'(','`id`',',','`name`',',','`code`',',','`type`',',','`provider_id`',',','`provider_name`',',','`lang_code`',',','`status`',',','`created`',',','`img`',')','VALUES',
  '(','NULL',',',repr(name),',',repr(code),',',repr(type_),',',repr(provider_id),',',repr(provider_name),',',repr(lang_code),',',repr(status),',',repr(current_time),',',repr(img),')',';')
  
for row in df.itertuples():
    
    game(row.name,row.code)
   
# sys.stdout = open('game.txt', 'w')
