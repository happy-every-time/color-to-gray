from sys import exit

from PIL import Image
from numpy import asarray, uint8

try:
    half = int(input('Set half value (Default : 100) >: '))
except:
    half = 100
m = (input('Set Model (max, min) (Default : min) >:') == 'max')

name = input('File Name >: ')
try:
    map_img = Image.open(name)
except FileNotFoundError:
    print('File Not Found!')
    exit(-1)

map_img = asarray(map_img.convert("RGB"))
map_array = []
if m:
    for line in map_img:
        map_line = []
        for p in line:
            if max(p) > half:
                map_line.append((255, 255, 255))
            elif max(p) <= half:
                map_line.append((0, 0, 0))
        map_array.append(map_line)
else:
    for line in map_img:
        map_line = []
        for p in line:
            if min(p) > half:
                map_line.append((255, 255, 255))
            elif min(p) <= half:
                map_line.append((0, 0, 0))
        map_array.append(map_line)

img = Image.fromarray(asarray(map_array).astype(uint8))
img.show()
img.save(f'{name}.png')

if input('Smooth (y, n) (Default : y) >: ') == 'n':
    exit()

try:
    level = int(input('Input smooth level (Default : 5) >: '))
except:
    level = 5
map_img = asarray(img.convert("RGB"))
img = map_img.copy()
for _ in range(level):
    for x in range(map_img.shape[0]):
        for y in range(map_img.shape[1]):
            if not (min(map_img[x][y]) == 255):
                try:
                    conut = ((max(map_img[x + 1][y]) / 255) + (max(map_img[x - 1][y]) / 255) +
                             (max(map_img[x][y + 1]) / 255) + (max(map_img[x][y - 1]) / 255))
                except IndexError:
                    conut = 0
                v = min(int(255 / 4 * conut), 255)
                img[x][y][0] = v
                img[x][y][1] = v
                img[x][y][2] = v

img = Image.fromarray(img.astype(uint8))
img.show()
img.save(f'{name}2.png')