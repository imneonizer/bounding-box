import cv2


class ReScaler():

    def resize(self, image, width=None, height=None, inter=cv2.INTER_AREA):
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

    def rescale(self, image, x1, y1, x2, y2, width=1920, height=1080):
        orig_coord = [x1, y1, x2, y2]

        # find original width and height
        h_orig, w_orig = image.shape[:2]

        if w_orig > h_orig:
            # if landsacape image resize by width
            image = self.resize(image, width=width)
        else:
            # if portrait image resize by height
            image = self.resize(image, height=height)

        # find new width and height
        h_new, w_new = image.shape[:2]

        # calculate rescaled bbox coordinates
        x1, y1, x2, y2 = [int(w_new * ((orig_coord[0]) / w_orig)),
                          int(h_new * ((orig_coord[1]) / h_orig)),
                          int(w_new * ((orig_coord[2]) / w_orig)),
                          int(h_new * ((orig_coord[3]) / h_orig))]

        return (image, x1, y1, x2, y2)
