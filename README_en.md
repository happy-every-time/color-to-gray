# Convert a Color Image to a Black-and-White Image #
## Implemented with PIL and numpy ##

[简体中文](https://github.com/happy-every-time/color-to-gray/blob/main/README.md)
[English]()

---

### How to Run ###
Enter the following in the console:
~~~bash
python Color-to-Gray.py
~~~
Or double-click to launch it.

---

### What to Do After Launch ###
~~~bash
Set half value (Default : 100) >: 
~~~
Enter the threshold value. The default is 100.

---

~~~bash
Set Model (max, min) (Default : min) >:
~~~
Enter max or min mode.

If max mode is selected:

The code will select the maximum of the three RGB color values of the image and compare it with the threshold value.

If it is greater than the threshold, the output will be white.

If it is less than or equal to the threshold, the output will be black.

If min mode is selected:

The code will select the minimum of the three RGB color values and compare it with the threshold value.

The rest is the same as in max mode.

---

~~~bash
File Name >: 
~~~
If your image is in the Python code directory, you only need to enter the file name (including the extension).

If it is not, enter the full path.

If the file is not found, it will output:

~~~bash
File Not Found!
~~~

---

~~~bash
Smooth (y, n) (Default : y) >: 
~~~

Whether to use image smoothing.

See the algorithm details below.

---

~~~bash
Input smooth level (Default : 5) >: 
~~~

Enter the smoothing level for the smoothing algorithm.

See the algorithm details below for the rest.

---
---

### Algorithm Details ###

~~~python
for _ in range(level):
    for x in range(map_img.shape[0]):
        for y in range(map_img.shape[1]):
            if not (min(map_img[x][y]) == 255):
                try:
                    conut = ((max(map_img[x + 1][y]) / 255) + (max(map_img[x - 1][y]) / 255) + (max(map_img[x][y + 1]) / 255) + (max(map_img[x][y - 1]) / 255))
                except IndexError:
                    conut = 0
                v = min(int(255 / 4 * conut), 255)
                img[x][y][0] = v
                img[x][y][1] = v
                img[x][y][2] = v
~~~

Divide the grayscale values of the pixels above, to the left, below, and to the right of a pixel by 255, then add them together.

If the pixel is white, the quotient is 1.

If the pixel is black, the quotient is 0.

Then add the coefficients from the four directions (top, left, bottom, right) and divide by 4.

Finally, multiply by 255 and use the result as the values of the pixel's three RGB color channels.