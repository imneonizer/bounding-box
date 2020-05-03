import os
from imbo.imbo import ImBo

abspath = lambda file_name: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.path.join("fonts", file_name))

# create fonts directory in module location
if not os.path.exists(abspath("")):
    os.makedirs(abspath(""))

__version__ = '0.1.0'
__author__ = 'imneonizer'

imbo = ImBo()
draw = imbo.draw
available_fonts = imbo.available_fonts
upload_font = imbo.upload_font
