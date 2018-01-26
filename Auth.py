from imgurpython import ImgurClient
from datetime import datetime
from os import listdir
from os.path import isfile, join
import numpy as np
from time import sleep
from pathlib import Path
import pickle
from pprint import pprint
import credentials

creds_file = Path("./credentials.dict")
pickle_in = open(creds_file,"rb")
credentials_dict = pickle.load(pickle_in)
pprint(credentials_dict)

client_id = credentials_dict['client_id']
client_secret = credentials_dict['client_secret']
client = ImgurClient(client_id, client_secret )
#print (client.get_auth_url('pin')) #go to page and copy down pin
creds = client.refresh()
print(creds)
