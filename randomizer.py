from PIL import Image, ImageFont, ImageDraw, ExifTags
from os import listdir, stat, path
from stat import *
from random import randint
from datetime import date
import json
from colorthief import ColorThief
import colorharmonies as Color

dt, dtog, dtdig = 0x0132, 0x9003, 0x9004
scenetype = 0xA301
comment = 0x9286
subloc = 0xA214
color_thief = None

# Replace with path to font on your machine (must be .tff). I recommend 'minisystem', download at https://www.dafont.com/minisystem.font
font_path = 'PATH_TO_FONT'

class Randomizer():
    def __init__(self, folder, outfolder):
        self.folder = folder
        self.outfolder = outfolder

    def get_random_image(self):
        global color_thief
        directory = listdir(self.folder)
        num = randint(0, len(directory)-1)
        filename = f'{self.folder}{directory[num]}'
        color_thief = ColorThief(filename)
        img = Image.open(filename)
        return img, filename

    def print_date(self,img):
        w,h = img.size
        ex = img._getexif()

        date = ex[dt].split(' ')[0]
        # date = date.replace(':',':')
        #comments = bytes.decode(ex[comment])
        #filter_used = comments.split('\"')[3]

        # print('date:',date)
        # print('filter:',filter_used)
        
        font = ImageFont.truetype(font_path, 75)
        image = img.convert('RGBA')
        txt = Image.new('RGBA', image.size, (255,255,255,0))
        draw = ImageDraw.Draw(txt)

        opacity = 0.85 # percentage
        draw.text((w-600,h-150), date, fill=(255,255,255,int(255*opacity)), font=font)
        combo = Image.alpha_composite(image,txt)
        
        return combo

    def save_image(self, img, name):
        img = img.convert('RGB')
        saved_at = f'{self.outfolder}{name}'
        img.save(saved_at)
        return saved_at

    def random_display(self):
        image, filename = self.get_random_image()
        name = filename.split('/')[1]

        # Prevent from sending previously sent image
        # TODO: handle no remaining unsent images
        
        '''
        while(path.isfile(f'{self.outfolder}{name}')):
            print('TRY AGAIN')
            image, filename = self.get_random_image()
            name = filename.split('/')[1]
        '''

        image = self.print_date(image)
        saved_at = self.save_image(image, name)
        print(saved_at)
        #Image.open(saved_at).show()
        #image.show()
        return saved_at