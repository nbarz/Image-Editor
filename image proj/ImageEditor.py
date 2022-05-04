from PIL import Image, ImageFilter 
import time
import os
import subprocess

#list of images
imagesJPEG = [
'raccoon1',
'raccoon2',
'raccoon3',
'raccoon4',
'raccoon5',
'raccoon6',
'raccoon7',
'raccoon8',
'raccoon9',
'raccoon10'
]


#-------------------------------------------------------------------
def select():
    #prints the list verticaly
    count = 0
    print('__choose an image__') 
    for pic in imagesJPEG:
        print(imagesJPEG[count])
        count+=1
        
    return input('file name: ')
#-------------------------------------------------------------------

def rotate():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')
        


    while True:
        try: #checks for number input
            deg = int(input('rotation in degrees: '))
            break
        except:
            print('\n')
            print('only numbers work')
            print('\n')


    try:
        with Image.open(name + ext) as im:
            im.rotate(deg).show()
    except: #if file name isnt found
        print('\n')
        print('file doesnt exist')
        print('\n')

    #saves to edited folder
    im1 = Image.open(name + ext)
    fn,fext= os.path.splitext(name + ext)
    im1.rotate(deg).save('Edited/{}.jpeg'.format(fn))
    print('File moved to Edited folder')

#-------------------------------------------------------------------
def blur():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')


    while True:
        try: #checks for number input
            amt = int(input('Blur 1-100: '))
            break
        except:
            print('\n')
            print('only numbers work')
            print('\n')


    try:
        with Image.open(name + ext) as im:
            im.filter(ImageFilter.GaussianBlur(radius = amt)).show()
    except: #if file name isnt found
        print('\n')
        print('file doesnt exist')
        print('\n')

    im1 = Image.open(name + ext)
    fn,fext= os.path.splitext(name + ext)
    im1.filter(ImageFilter.GaussianBlur(radius = amt)).save('Edited/{}.jpeg'.format(fn))
    print('File moved to Edited folder')
#-------------------------------------------------------------------
def openImg():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')

    with Image.open(name + ext) as im:
        im.show()

#-------------------------------------------------------------------
def greyscale():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')

    with Image.open(name + ext) as im:
        im.convert('L').show()

    im1 = Image.open(name + ext)
    fn,fext= os.path.splitext(name + ext)
    im1.convert('L').save('Edited/{}.jpeg'.format(fn))
    print('File moved to Edited folder')

#-------------------------------------------------------------------
def Convert():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')


    # creating a image object (main image) 
    im1 = Image.open(name + ext) 

    fn,fext= os.path.splitext(name + ext)
    im1.save('PNG/{}.png'.format(fn))
    print('File moved to PNG folder')


#-------------------------------------------------------------------
def thumb():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')

    print('''
        _SIZES_
    [1] 200x200px
    [2] 400x400px
    [3] 600x600px
    ''')
    while True:
        try:
            preset = int(input('Size preset: '))
        except:
            print('\n')
            print('no such preset')
            print('\n')
            continue
        if preset == 1:
            size = 200,200
        elif preset == 2:
            size = 400,400
        elif preset == 3:
            size = 600,600
        else:
            print('\n')
            print('no such preset')
            print('\n')
            continue
        break
        


    im1 = Image.open(name + ext)
    im1.thumbnail(size)
    im1.show()

    fn,fext= os.path.splitext(name + ext)
    im1.save('Edited/{}.jpg'.format(fn))
    print('File moved to Edited folder')

    
#-------------------------------------------------------------------
def smooth():
    ext = ''
    while True:
        name = select()
        if name in imagesJPEG:
            if name in imagesJPEG:
                ext = '.jpg'
            break
        else:
            print('\n')
            print('file not found')
            time.sleep(1)
            print('\n')



    try:
        with Image.open(name + ext) as im:
            im.filter(ImageFilter.SMOOTH_MORE).show()
    except: #if file name isnt found
        print('\n')
        print('file doesnt exist')
        print('\n')

    im1 = Image.open(name + ext)
    fn,fext= os.path.splitext(name + ext)
    im1.filter(ImageFilter.SMOOTH_MORE).save('Edited/{}.jpeg'.format(fn))
    print('File moved to Edited folder')

#-------------------------------------------------------------------

while True:
    print('''
[1] Open image
[2] Format Conversion
[3] View image list
[4] Edit Thumbnail
[5] Rotate Image
[6] Desaturate
[7] Blur
[8] Smooth (other feature)
[9] View edited
[Q] Quit
''')

    method = input('input: ')
    if method == '1':
        openImg()
    elif method == '2':
        Convert()
    elif method == '3':
        print('_PHOTOS_')
        print(imagesJPEG)
    elif method == '4':
        thumb()
    elif method == '5':
        rotate()
    elif method == '6':
        pass
        greyscale()
    elif method == '7':
        blur()
    elif method == '8':
        smooth()
    elif method == '9':
        #tether file is used to go inside folder
        subprocess.Popen(r'explorer /select,"Edited\Tether.txt"')
    elif method == 'q' or method == 'Q':
        break
    else:
        print('\n')
        print('Invalid input')
        print('\n')
#-------------------------------------------------------------------
