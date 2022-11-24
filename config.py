import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token',5917276242:AAFSkqogSe4D3npuZGlKALyJuw-twEtMTe4'')
API_ID =  os.environ.get('api_id','21552633')
API_HASH = os.environ.get('api_hash','75c416fcdd3d5e2b2deabe4259246eb6')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','150'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','cfgelier').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc',''))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
