import cv2


class ReScaler():

    def __init__(self):
        self.paddings = {
            'replicate': cv2.BORDER_REPLICATE,
            'reflect': cv2.BORDER_REFLECT,
            'reflect_101': cv2.BORDER_REFLECT_101,
            'wrap': cv2.BORDER_WRAP,
            'constant': cv2.BORDER_CONSTANT
        }

    @staticmethod
    def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
        # initialize the dimensions of the image to be resized and
        # grab the image dimensions
        dim = None
        (h, w) = image.shape[:2]

        # if both the width and height are None, then return the
        # original image
        if width is None and height is None:
            return image

        # check to see if the width is None
        if width is None:
            # calculate the ratio of the height and construct the
            # dimensions
            r = height / float(h)
            dim = (int(w * r), height)

        # otherwise, the height is None
        else:
            # calculate the ratio of the width and construct the
            # dimensions
            r = width / float(w)
            dim = (width, int(h * r))

        # resize the image
        resized = cv2.resize(image, dim, interpolation=inter)

        # return the resized image
        return resized

    def fit_padding(self, image, height, width, coord_list, padding=None, padding_color=(0, 0, 0)):
        if padding in self.paddings:
            padding_type = self.paddings[padding]
        else:
            if padding is not None and type(padding) not in [tuple, list, bool]:
                print("[warning] invalid padding input: '{}', please use {}".format(
                    padding, list(self.paddings)))
            padding_type = self.paddings["constant"]

        # resize image to given width maintaining aspect ratio
        new_image = self.resize(image.copy(), width=width)
        rescaled_coords = self.rescale_coord(
            image.shape, new_image.shape, coord_list)

        # check if padding is possible
        if height - new_image.shape[0] > 0:
            # add padding to height / bottom
            top, bottom, left, right, borderType = (
                0, height - new_image.shape[0], 0, 0, padding_type)
            new_image = cv2.copyMakeBorder(
                new_image, top, bottom, left, right, borderType, value=padding_color)
        else:
            # resize image to given height maintaining aspect ratio
            new_image = self.resize(image.copy(), height=height)
            rescaled_coords = self.rescale_coord(
                image.shape, new_image.shape, coord_list)

            # add padding to width / right
            top, bottom, left, right, borderType = (
                0, 0, 0, width - new_image.shape[1], padding_type)
            new_image = cv2.copyMakeBorder(
                new_image, top, bottom, left, right, borderType, value=padding_color)

        return (new_image, rescaled_coords)

    @staticmethod
    def rescale_coord(orig_res, new_res, coord_list):
        if len(coord_list) == 0 or coord_list is None:
            return

        h_orig, w_orig = orig_res[:2]
        h_new, w_new = new_res[:2]

        rescaled_coords = []
        for orig_coord in coord_list:
            new_coord = [int(w_new * ((orig_coord[0]) / w_orig)),
                         int(h_new * ((orig_coord[1]) / h_orig)),
                         int(w_new * ((orig_coord[2]) / w_orig)),
                         int(h_new * ((orig_coord[3]) / h_orig))]

            rescaled_coords.append(new_coord)

        return rescaled_coords

    def rescale(self, image, coord_list, width=None, height=None, keep_ratio=False, padding=None, padding_color=(0, 0, 0)):
        # when padding is true, force resizing cannot be done
        if padding:
            keep_ratio = True

        # store original width and height
        h_orig, w_orig = image.shape[:2]

        # check various possible cases
        if width is not None and height is None:
            # if only width is provided but not height
            # resize by width and auto calculate height
            image = self.resize(image, width=width)

        elif height is not None and width is None:
            # if only width is provided but not height
            # resize by width and auto calculate height
            image = self.resize(image, height=height)

        elif height is not None and width is not None:
            if keep_ratio is False:
                # if both height and width is provided but keep_ratio is False
                # force resize image to given width and height
                image = cv2.resize(image, (width, height),
                                   interpolation=cv2.INTER_AREA)

            else:
                # if both height and width is provided but keep_ratio is True
                # take max(img_height, img_width) and use that property to
                # resize
                if not padding:
                    # if padding is False then follow normal resizing process
                    if w_orig > h_orig:
                        # if landsacape image resize by width
                        image = self.resize(image, width=width)
                    else:
                        # if portrait image resize by height
                        image = self.resize(image, height=height)

        # if apply padding argument is passed
        if height is not None and width is not None and padding:
            # add padding to image and calculate rescaled coordinates
            image, rescaled_coords = self.fit_padding(
                image, height, width, coord_list, padding, padding_color)
        else:
            # otherwise just calculate rescaled coordinates
            rescaled_coords = self.rescale_coord(
                (h_orig, w_orig), image.shape, coord_list)

        return (image, rescaled_coords)
