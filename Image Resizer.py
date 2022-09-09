# Image Resizer

from PIL import Image

img_choice = input('Image path: ')
image = Image.open(img_choice)
print(f'Current size: {image.size}')


def resize(s1, s2):
    resized_image = image.resize((s1, s2))
    resized_image.save(f'{s1}x{s2}.png')
    print('Done Resizing!')


s1 = int(input('Enter Width: '))
s2 = int(input('Enter Height: '))
resize(s1, s2)
