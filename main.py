import win32api
from PIL import Image, ImageOps
import mousefuncs
import time
import winsound

img = Image.open('img/invader1.bmp').convert('L')  # convert image to 8-bit grayscale
img = ImageOps.invert(img)
WIDTH, HEIGHT = img.size
# convert image data to a list of integers
data = list(img.getdata())

# convert that to 2D list (list of lists of integers)
data = [data[offset:offset + WIDTH] for offset in range(0, WIDTH * HEIGHT, WIDTH)]

test = True  # Set True for painting on a canvas (eg. paint.exe)
pixelspacing = 16
verticalspacing = 16
frequency = 1600
duration = 500
magsize = 30
ammo_needed = 0
xcount = 0

if test:
    pixelspacing = int(pixelspacing/4)
    verticalspacing = int(verticalspacing/4)
    bulletsleep = 0.001
    linesleep = 0.02
else:
    bulletsleep = 0.5
    linesleep = 0.3

for i in range(10):
    winsound.Beep(frequency, duration)

if not test:
    mousefuncs.PressButton(True, 'right')
    time.sleep(0.5)

winsound.Beep(frequency, duration)

for row in data:

    for pix in row:
        if win32api.GetKeyState(0x04) < 0:
            print('cancel inner loop')
            mousefuncs.PressButton(False, 'left')
            break
        xcount += 1

        if pix == 255:
            print('@', end='')
            # mousefuncs.ClickButton('left', 0.001)
            mousefuncs.PressButton(True, 'left')
            time.sleep(0.002)
            mousefuncs.PressButton(False, 'left')
            ammo_needed += 1

            if ammo_needed % magsize == 0 and not test:
                winsound.Beep(2500, 200)
                time.sleep(3)  # idle time to change mag
                winsound.Beep(2500, 200)
        else:
            print('.', end='')

        mousefuncs.moveRelative(pixelspacing, 0)
        time.sleep(bulletsleep)
        
    if win32api.GetKeyState(0x04) < 0:
        print('cancel')
        break

    mousefuncs.moveRelative(((xcount * pixelspacing) * -1), verticalspacing)
    time.sleep(linesleep)
    xcount = 0
    print('')

mousefuncs.PressButton(False, 'left')
mousefuncs.PressButton(False, 'right')
winsound.Beep(2000, 2000)

print(ammo_needed)
