from pyimgur import Imgur
from randomizer import Randomizer
from photosender import Sender
import datetime

# Optional: create 'VSCO-Daily.txt file in same directory if you would like to log uploads
def write_to_file(data):
    link, addr = data
    f = open('VSCO-Daily.txt', 'w')
    f.write(f'{datetime.datetime.now()} SAVED {link} {addr}\n')

# Replace with your Imgur CLIENT_ID
CLIENT = 'CLIENT_ID'

# Replace with Twilio account details
ACCOUNT_ID = 'ACCOUNT_ID'
AUTH_TOKEN = 'AUTH_TOKEN'
TO_NUMBER = 'TO_NUMBER'
FROM_NUMBER = 'FROM_NUMBER'

im = Imgur(CLIENT)
s = Sender(ACCOUNT_ID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER)

# Replace with directories where (1) Images to send are located (2) Modified images are to be saved
# end directory with /
in_folder = 'in_folder/'
out_folder = 'out_folder/'

r = Randomizer(in_folder, out_folder)
path = r.random_display()
upload = im.upload_image(path, title='test')

info = upload.link_huge_thumbnail, path

s.send_img(upload.link_huge_thumbnail)

# Optional if you would like to keep track of files sent/uploaded
# write_to_file(info)

upload.delete() # Deletes upload from Imgur
