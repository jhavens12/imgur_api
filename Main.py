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

def get_files(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    image_list = []

    for x in onlyfiles:
        image_list.append(mypath+x)
    return image_list

def upload_images(image_list):
    image_ids = []
    for picture_path in image_list:
        uploaded_image = client.upload_from_path(picture_path, config=None, anon=False)
        sleep(10)
        print(uploaded_image['link'])
        image_ids.append(uploaded_image['id'])
    return image_ids

def create_album(name):
    #take name, check to see if album name exists
    #if yes, return id
    #if no, create album and return id

    config = {
    'name':  name
    }

    new_album = client.create_album(config)
    return new_album['id']

def add_to_album(album_id,image_id_list):
    result = client.album_add_images(new_album['id'],image_ids)

def get_user_albums():
    #get_account_albums(self, username, page=0)
    albums = client.get_account_albums('broadsid3',page=0)
    for x in albums:
        print(x.title)
        print(x.id)

mypath = '~/Documents/GitHub/imgur_api/Test_Photos/'
#credentials_dict = get_new_tokens(credentials_dict)
client = set_old_tokens(credentials_dict)
pprint(client.credits)

file_list = get_files(mypath) #get files to upload
image_ids = upload_images(file_list) #upload images and return list of ids
album_id = create_album("Test1") #create album and get album id
add_to_album(album_id,image_ids) #add images to album
print("www.imgur.com/a/"+album_id) #pring album link

#get_user_albums()
