# Image Bounding Box

<table>
<tr>
  <td>Latest Release</td>
  <td>
    <a href="https://pypi.org/project/imbo/">
    <img src="https://img.shields.io/pypi/v/imbo.svg" alt="latest release" />
    </a>
  </td>
</tr>
<tr>
  <td>License</td>
  <td>
    <a href="https://github.com/imneonizer/imbo/blob/master/LICENSE">
    <img src="https://img.shields.io/pypi/l/bounding-box.svg" alt="license" />
    </a>
  </td>
</tr>
</table>

**IMBO** is a library to plot pretty bounding boxes with a simple Python API.  
*Please notice this lib does **not** do object detection for you, but only helps to display pretty bounding boxes with a carefully chosen set of colors.*  

![banner](docs/images/banner.png)

## Inspiration
The core idea came from [nalepae/bounding-box](https://github.com/nalepae/bounding-box) All the credits goes to **Manu NALEPA** for the core functionalities, IMBO is built on top of [bounding-box](https://pypi.org/project/bounding-box/) with more enhanced features keeping customization at focus.

## Installation
````python
>> pip install imbo
````

## API
Add the bounding box and label on an image.
 ```python
import cv2
import imbo
image = cv2.imread("example.jpg")
image = imbo.draw(image, left, top, right, bottom, label, color)
 ```

**This method takes 5 mandatory parameters:**

- `image`: A numpy array, channel last (ie. height x width x colors) with
  channels in **BGR** order (same as **openCV** format).
- `left`: A integer representing the left side of the bounding box.
- `top`: A integer representing the top side of the bounding box.
- `right`: A integer representing the right side of the bounding box.
- `bottom`: A integer representing the bottom side of the bounding box.

**It also takes 8 optional parameters:**

- `label`: A string representing the label of the bounding box, If not specified, then no label will be displayed.
- ``font_name``: You can use multiple fonts but the ``.ttf`` file must be present in the module path.
  - Available font are: `Aclonica`, `Courgette`, `Gloria`, `Kalam`, `Kaushan`, `Merienda`, `Roboto-Medium`, `Typewriter`, `Ubuntu-B`
- ``font_size``: It can be used to adjust the label text size in case if required, ``default=20``.
- ``thickness``: The thickness of bounding boxes, ``default=2``.
- ``adjust_label``: Incase while increasing the ``font_size`` or ``thickness`` the label text might get misplaced, use ``adjust_label=(x, y)`` to adjust the position.
- ``rescale``: There are time when the input image is either of very less resolution or very high resolution in such cases use ``rescale=True`` , see [this example](https://github.com/imneonizer/imbo/blob/master/docs/Rescaling%20example/Readme.md) to know how rescaling affects the output.
- `rescale_width`: Width to use when applying rescaling, `default=1920`
- `rescale_height`: Width to use when applying rescaling, `default=1920`
- `bbox_color`: RGB tuple, HEX code or a string representing the color of the bounding box.
- `label_color`: RGB tuple, HEX code or a string representing the color of the label text.

  - Possible string values are:`navy`, `blue`, `aqua`, `teal`, `olive`, `green`,
    `lime`, `yellow`, `orange`, `red`, `maroon`, `fuchsia`, `purple`,
    `black`, `gray` ,`silver` , `white`.

----

Rescale image without messing with original bounding box coordinates.

````python
import cv2
import imbo

image = cv2.imread("car.jpg")
car = (88,50,827,591)
license_plate = (337, 499, 598, 561)

coordinates = [car, license_plate]
image, coordinates = imbo.rescale(image, coordinates, width=900, height=600, padding='replicate')
````

**This method takes 3 mandatory parameters:**

- `image`: A numpy array, channel last (ie. height x width x colors) with
  channels in **BGR** order (same as **openCV** format).
- `coord_list`: A list containing bbox tuples in order of `(left, top, right, bottom)`.
- `width/height`(any one): This parameter is used to resize image and bbox accordingly while maintaining aspect ratio. Note:- if both parameters are passed at once the image will be force resized to given dimensions.

**And it takes 3 optional parameters:**

- `keep_ratio`: A *Boolean* to tell whether to maintain aspect ratio or not while resizing images and rescaling corresponding bounding boxes. useful when both `height` and `width` parameter are passed at once.

- `padding`: *String* representing padding type to apply, possible values are :

  - `replicate`, `reflect`, `reflect`, `wrap`, `constant`

- `padding_color`: *BGR tuple*, when using `padding='constant'` it can be used to set padding color.

  Here is an [example](https://github.com/imneonizer/imbo/blob/master/docs/Resize%20example/Readme.md) showing how to do custom rescaling of images and bounding boxes.

## Video Demo
![](docs/images/nitin-demo.gif)

## Image Examples
The script to plot examples of this **README** is available [here](docs/examples.py). go in root  of this git repository then write:

Below are some examples of bounding boxes plotted with this library.

 ```bash
python docs/examples.py
 ```

<table>
  <img src="docs/images/winton_imbo.png", width="800px", height="450px">
  <img src="docs/images/nao-romeo-pepper_imbo.png", width="800px", height="450px">
  <img src="docs/images/khatia_imbo.png", width="800px", height="450px">
  <img src="docs/images/selfie_imbo.png", width="800px", height="450px">
</table>

### credits
> Again, many thanks to [**@nalepae**](https://github.com/nalepae/bounding-box) for coming up with the original idea and providing some core functionalities for IMBO.
> Icon made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a>
