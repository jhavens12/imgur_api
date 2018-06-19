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
if creds_file.is_file():
#pricing import
    pickle_in = open(creds_file,"rb")
    credentials_dict = pickle.load(pickle_in)
    pprint(credentials_dict)
else:
    f=open("credentials.dict","w+") #create file
    f.close()
    credentials_dict = {} #create limits dict and variables
    credentials_dict['client_id'] = credentials.client_id
    credentials_dict['client_secret'] = credentials.client_secret

    pickle_out = open("credentials.dict","wb") #open file
    pickle.dump(credentials_dict, pickle_out) #save limits dict to file
    pickle_out.close()

def get_new_tokens(credentials_dict):
    client_id = credentials_dict['client_id']
    client_secret = credentials_dict['client_secret']
    client = ImgurClient(client_id, client_secret )
    print (client.get_auth_url('pin')) #go to page and copy down pin
    creds = client.authorize(input('Pin: '), 'pin')
    print(creds)
    credentials_dict['access_token'] = creds['access_token']
    credentials_dict['refresh_token'] = creds['refresh_token']

    client.set_user_auth(credentials_dict['access_token'], credentials_dict['refresh_token'])

    print("Access Token")
    print(creds['access_token'])
    print("Refresh Token")
    print(creds['refresh_token'])
    print()

    pickle_out = open("credentials.dict","wb") #open file
    pickle.dump(credentials_dict, pickle_out) #save limits dict to file
    pickle_out.close()

    return credentials_dict

def set_old_tokens(credentials_dict):

    client = ImgurClient(credentials_dict['client_id'],credentials_dict['client_secret'], credentials_dict['refresh_token'])
    client.set_user_auth(credentials_dict['access_token'], credentials_dict['refresh_token'])
    return client

def album_loop(page_number):
    sleep(8)
    albums = client.get_account_albums('0mega5upreme',page=page_number)
    n = 0
    album_dict = {}
    for x in albums:
        album_dict[x.title] = x.id
        n = n+1
    return album_dict,n

def get_user_albums():
    #get_account_albums(self, username, page=0)
    page_number = 0
    album_dict,count = album_loop(page_number)

    while count == 50:
        page_number = page_number + 1
        album_dict_part,count = album_loop(page_number)
        album_dict = {**album_dict, **album_dict_part}
    print("Album Count: "+str(len(list(album_dict.keys()))))
    return album_dict



#credentials_dict = get_new_tokens(credentials_dict)
client = set_old_tokens(credentials_dict)
pprint(client.credits)

final_dict = get_user_albums()
pprint(final_dict)
