
from PIL import Image, ImageFilter

def main():
    with Image.open('animation/image1.jpeg') as image :
        print(image.format)
        print(image.size)
        img =image.rotate(180)
        img= img.filter(ImageFilter.BLUR)
        img= img.filter(ImageFilter.FIND_EDGES)
        img.save('animation/image2.jpeg')

main()