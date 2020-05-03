import os
import cv2
from PIL import ImageFont
import numpy as np
from hashlib import md5
import shutil

abspath = lambda file_name: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.path.join("fonts", file_name))


class ImBo():

    def __init__(self, font_name="Roboto-Medium", font_size=20):
        self.FONT_SIZE = font_size
        self.FONT_NAME = font_name
        self.FONT = ImageFont.truetype(
            abspath(self.FONT_NAME + ".ttf"), font_size)
        self.COLOR_RGB2BGR = lambda rgb: rgb[::-1]
        self.COLOR_BGR2RGB = lambda bgr: bgr[::-1]
        self.COLOR_RGB2HEX = lambda rgb: '#' + '%02x%02x%02x' % rgb
        self.COLOR_BGR2HEX = lambda bgr: '#' + \
            '%02x%02x%02x' % self.COLOR_BGR2RGB(bgr)
        self.COLOR_HEX2RGB = lambda hx: (int(hx.lstrip("#")[0:2], 16), int(
            hx.lstrip("#")[2:4], 16), int(hx.lstrip("#")[4:6], 16))
        self.COLOR_HEX2BGR = lambda hx: self.COLOR_RGB2BGR(
            self.COLOR_HEX2RGB(hx))

        light, dark = (240, 241, 242), (0, 0, 0)
        self.COLOR_NAME_TO_RGB = dict(
            navy=((0, 38, 63), (light)),
            blue=((0, 120, 210), (light)),
            aqua=((115, 221, 252), (dark)),
            teal=((15, 205, 202), (dark)),
            olive=((52, 153, 114), (dark)),
            green=((0, 204, 84), (dark)),
            lime=((1, 255, 127), (dark)),
            yellow=((255, 216, 70), (dark)),
            orange=((255, 125, 57), (dark)),
            red=((255, 47, 65), (dark)),
            maroon=((135, 13, 75), (light)),
            fuchsia=((246, 0, 184), (dark)),
            purple=((179, 17, 193), (light)),
            black=((24, 24, 24), (light)),
            gray=((168, 168, 168), (dark)),
            silver=((220, 220, 220), (dark)),
            white=((light), (dark))
        )

        self.COLOR_NAMES = list(self.COLOR_NAME_TO_RGB)
        self.LABEL2COLOR = lambda label: self.COLOR_NAMES[
            int(md5(label.encode()).hexdigest(), 16) % len(self.COLOR_NAME_TO_RGB)]

    @property
    def available_fonts(self):
        return list(filter(lambda x: os.path.splitext(x)[1] == ".ttf", os.listdir(abspath(""))))

    def upload_font(self, font_path):
        shutil.copy(font_path, abspath(os.path.basename(font_path)))

    def check_color(self, color, label=False):
        if type(color) is str:
            if color.startswith("#"):
                # check if HEX color input
                assert len(
                    color) == 7, "incorrect HEX color value: {}".format(color)
                color = self.COLOR_HEX2BGR(color)
            else:
                # check if color name input
                if label:
                    # if label_color ends with '-contrast'
                    # return the matching background color for that name
                    if color.endswith("-contrast"):
                        color = color.replace("-contrast", "")
                        assert color in self.COLOR_NAMES, "'label_color' name must be one of [" + "-contrast, ".join(
                            self.COLOR_NAMES) + "]"
                        color = self.COLOR_RGB2BGR(
                            self.COLOR_NAME_TO_RGB[color][1])
                    else:
                        # return the color value for the name
                        assert color in self.COLOR_NAMES, "'bbox_color' name must be one of [" + ", ".join(
                            self.COLOR_NAMES) + "]"
                        color = self.COLOR_RGB2BGR(
                            self.COLOR_NAME_TO_RGB[color][0])

                else:
                    assert color in self.COLOR_NAMES, "'bbox_color' name must be one of [" + ", ".join(
                        self.COLOR_NAMES) + "]"
                    color = self.COLOR_RGB2BGR(
                        self.COLOR_NAME_TO_RGB[color][0])
        else:
            # else verify tuple length and its values
            assert type(color) in [tuple, list, set] and len(
                color) == 3, "incorrect BGR color value: {}".format(color)
            assert type(color[0]) is int and type(color[1]) is int and type(
                color[2]) is int, "color tuple items must be integer"
            color = self.COLOR_RGB2BGR(tuple(color))

        return color

    def get_label_image(self, text, font_color_tuple_bgr, background_color_tuple_bgr, font_name, font_size):
        if font_size != self.FONT_SIZE:
            self.FONT_SIZE = font_size
            self.FONT = ImageFont.truetype(
                abspath(self.FONT_NAME + ".ttf"), font_size)

        if font_name != self.FONT_NAME:
            self.FONT_NAME = font_name
            self.FONT = ImageFont.truetype(
                abspath(font_name + ".ttf"), self.FONT_SIZE)

        text_image = self.FONT.getmask(text)

        shape = list(reversed(text_image.size))
        bw_image = np.array(text_image).reshape(shape)

        color_image = lambda image, font_color, background_color: background_color + \
            (font_color - background_color) * image / 255

        image = [
            color_image(bw_image, font_color, background_color)[None, ...]
            for font_color, background_color
            in zip(font_color_tuple_bgr, background_color_tuple_bgr)
        ]

        return np.concatenate(image).transpose(1, 2, 0)

    def draw(self, image, left, top, right, bottom, label=None, bbox_color=None, label_color=None, font_name="Roboto-Medium", font_size=20, thickness=2, adjust_label=(0, 0)):
        assert type(image) is np.ndarray, "'image' parameter must be a numpy.ndarray, but given: {}".format(
            type(image))
        assert type(label) is str, "'label' must be a string"
        if len(label) == 0:
            label = None
        assert type(thickness) is int, "'thickness' must be a integer"

        # bounding box coordinates
        left, top, right, bottom = int(left), int(top), int(right), int(bottom)

        # experimental argument to override label box position
        adj_left, adj_top = adjust_label

        # storing original input arguments for later reference
        BBOX_COLOR, LABEL_COLOR = bbox_color, label_color

        if bbox_color is None and label_color is None:
            # generate bbox_color and label_color based on label text
            bbox_color, label_color = self.COLOR_NAME_TO_RGB[
                self.LABEL2COLOR(label)]
            bbox_color, label_color = self.COLOR_RGB2BGR(
                bbox_color), self.COLOR_RGB2BGR(label_color)

        if bbox_color is not None:
            # verify input bbox_color
            bbox_color = self.check_color(bbox_color)
        else:
            # generate bbox_color based on label text
            bbox_color = self.COLOR_RGB2BGR(
                self.COLOR_NAME_TO_RGB[self.LABEL2COLOR(label)][0])

        if label_color is not None:
            # verify input label_color
            label_color = self.check_color(label_color, label=True)
        else:
            # generate matching label_color for bbox_color name input
            if type(BBOX_COLOR) == str and (not BBOX_COLOR.startswith("#")):
                label_color = self.check_color(
                    BBOX_COLOR + '-contrast', label=True)
            else:
                # generate label_color based on label text
                label_color = self.COLOR_RGB2BGR(
                    self.COLOR_NAME_TO_RGB[self.LABEL2COLOR(label)][1])

        image = cv2.rectangle(image, (left, top),
                              (right, bottom), bbox_color, thickness=thickness)

        if label:
            _, image_width, _ = image.shape

            label_image = self.get_label_image(
                label, label_color, bbox_color, font_name, font_size)
            label_height, label_width, _ = label_image.shape
            rectangle_height, rectangle_width = 1 + label_height, 1 + label_width

            rectangle_bottom = top
            rectangle_left = max(
                0, min(left - 1, image_width - rectangle_width))

            rectangle_top = rectangle_bottom - rectangle_height
            rectangle_right = rectangle_left + rectangle_width

            label_top = rectangle_top + 1 + adj_top

            if rectangle_top < 0:
                rectangle_top = top
                rectangle_bottom = rectangle_top + label_height + 1
                label_top = rectangle_top + adj_top

            # label text placement position
            label_left = rectangle_left + 1 + adj_left
            label_bottom = label_top + label_height
            label_right = label_left + label_width

            rec_left_top = (rectangle_left + adj_left, rectangle_top + adj_top)
            rec_right_bottom = (rectangle_right + adj_left, rectangle_bottom)

            # rectangle fill below label text on image as a backup
            cv2.rectangle(image, rec_left_top,
                          rec_right_bottom, bbox_color, -1)
            # overwriting image array with text array
            image[label_top:label_bottom,
                  label_left:label_right, :] = label_image

        return image
