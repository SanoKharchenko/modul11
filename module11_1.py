import numpy as np
import requests
# import pandas
# import matplotlib
from PIL import Image

print("Используем библтотеку 'requests'")
res = requests.get('https://ya.ru/')
print(res.content)
print(res.text)

print("Используем библтотеку 'numpy'")
mas_1 = np.array([[range(1, 5)], [range(5, 1, -1)]])
mas_2 = np.random.randint(1, 10, size=(3, 3))
print(mas_1)
print(mas_2)
print(mas_1.ndim)
print(mas_2.ndim)
print(mas_1.dtype)
print(mas_2.dtype)

print("Используем библтотеку 'pillow'")


def new_size_image(name):
    im = Image.open(name)
    w, h = im.size
    return im.resize((w//3, h//3))


image = new_size_image('skalyi-goryi-reka-les.jpg')
image = image.convert('L')
image.save('skalyi-goryi-reka-les.jpg', 'png')

image.show('NewImage')
