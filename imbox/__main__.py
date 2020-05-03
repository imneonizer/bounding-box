import os
import argparse
import shutil

abspath = lambda file_name: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), os.path.join("fonts", file_name))

# construct the command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-u", "--upload", required=True,
                help="path to .ttf file")
args = vars(ap.parse_args())


def upload_font(font_path):
    assert font_path.endswith(
        ".ttf"), "invalid file name, only .ttf files are accepted"
    shutil.copy(font_path, abspath(os.path.basename(font_path)))
    print(">> upload successful")

upload_font(args["upload"])
