import PIL
from PIL import Image

class icc:
    def recolor(path, name="bug.png", compatiblity=True):
        if compatiblity:
            #this is the safer way to do it, but it scales the image to 300x300.
            OGimage = PIL.Image.open("android.png")
            newimage = PIL.Image.open(path)
            newimage = newimage.resize(OGimage.size)
            OGimage.paste(newimage, (0,0))
            OGimage.save(name)
        else:
            #this is the unsafe way to do it, but it copies the icc profile from the model image directly
            #and tries to copy it onto the new image, this does not work most of the time for alot of images.
            #use an image with a PNG format.
            OGimage = PIL.Image.open("android.png")
            newimage = PIL.Image.open(path)
            newimage.info['icc_profile'] = OGimage.info['icc_profile']
            newimage.save(name)

icc.recolor("Ryuko.jpg")