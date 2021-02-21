from PIL import Image
import os

size_300 = (300,300)
for f in os.listdir('.'):
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext1 = os.path.splitext(f)

        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn, fext1))


# for f in os.listdir('.'):
#     if f.endswith('.jpg'):
#         i =  Image.open(f)
#         fn, fext = os.path.splitext(f)
#         i.save('PNGs/{}.png'.format(fn))


# image1 = Image.open('Marina Beach.jpg')  #Creating Image object
# image1.show()
# image1.save('Marina Beach.png') #Rename image file

