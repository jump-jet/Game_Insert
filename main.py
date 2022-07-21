import pandas as pd
import csv
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H:%M:%S")

pd.options.display.max_rows = 999

df = pd.read_csv('data.csv')
df = pd.DataFrame(df)

df_provider = pd.read_csv('siam123.csv')
df_provider = pd.DataFrame(df_provider)

df_lang = pd.read_csv('lang_code.csv')
df_lang = pd.DataFrame(df_lang)

table = '`game_list`'
type_ = '1'
lang_code = 'G00100'
status = '1'
a = "` ( `"


with open("game.txt","w") as f:
     for row in df.itertuples():
          provider_name = row.provider
          result = df_provider.loc[df_provider['display'] == provider_name,'id']
          lang = df_lang.loc[df_lang['provider_name'] == provider_name,'lang_code']
          
          for result_id in result:   
               provider_id = result_id
          for lang_code in lang:
               lang_code = lang_code   
               value = f'INSERT INTO {table} (`id`,`name`,`code`,`type`,`provider_id`,`provider_name`,`lang_code`,`status`,`created`,`img`) VALUES (NULL,{repr(row.name)},{repr(row.code)},{repr(type_)},{repr(provider_id)},{repr(row.provider)},{repr(lang_code)},{repr(status)},{repr(current_time)},{repr(row.img)}); \n'
               f.write(value)
 