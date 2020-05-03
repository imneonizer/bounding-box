import cv2
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import imbox
import os

def show_and_save(title, image, path):
    cv2.imwrite(path, image)
    cv2.imshow(title, image)
    print("Press 'Enter' to display the next picture...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    if "examples.py" in os.listdir():
        print("please run this script from root directory")
        print(">> python docs/examples.py")
        return

    in_path = os.path.join("docs", "images", "winton.jpg")
    out_path = os.path.join("docs", "images", "winton_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 281, 12, 744, 431, "Winton", "maroon", font_size=50)
    imbox.draw(image, 166, 149, 500, 297, "Trumpet", "yellow")
    show_and_save("Winton MARSALIS", image, out_path)

    in_path = os.path.join("docs", "images", "khatia.jpg")
    out_path = os.path.join("docs", "images", "khatia_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 280, 24, 802, 593, "Khatia", "maroon", thickness=8, font_size=40)
    imbox.draw(image, 687, 1, 1448, 648, "Piano", "gray")
    imbox.draw(image, 888, 492, 1190, 536, "Text")
    show_and_save("Khatia BUNIATISHVILI", image, out_path)

    in_path = os.path.join("docs", "images", "clarifloue.jpg")
    out_path = os.path.join("docs", "images", "clarifloue_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 69, 86, 470, 136, label="Headache designer")
    imbox.draw(image, 136, 196, 406, 234, "Text")
    imbox.draw(image, 67, 351, 471, 400, "Headache designer")
    imbox.draw(image, 130, 456, 390, 494, "Text")
    show_and_save("Clarinet", image, out_path)

    in_path = os.path.join("docs", "images", "nao-romeo-pepper.jpg")
    out_path = os.path.join("docs", "images", "nao-romeo-pepper_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 155, 152, 244, 297, "Nao", bbox_color="#ffffff")
    imbox.draw(image, 260, 6, 423, 416, "Romeo", bbox_color=(255,0,0))
    imbox.draw(image, 421, 76, 547, 402, "Pepper")
    show_and_save("Robots", image, out_path)

    in_path = os.path.join("docs", "images", "ski-paraglider.jpg")
    out_path = os.path.join("docs", "images", "ski-paraglider_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 0, 128, 645, 589, "Paraglider", bbox_color="orange")
    imbox.draw(image, 689, 442, 818, 566, "Skier", label_color="gray")
    show_and_save("Ski and paraglider", image, out_path)

    in_path = os.path.join("docs", "images", "paragliders.jpg")
    out_path = os.path.join("docs", "images", "paragliders_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 90, 228, 318, 428, "Paraglider", thickness=8, adjust_label=(-3, -20))
    imbox.draw(image, 521, 110, 656, 415, "Paraglider")
    show_and_save("Pretty Bounding Box", image, out_path)

    in_path = os.path.join("docs", "images", "selfie.jpg")
    out_path = os.path.join("docs", "images", "selfie_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 5, 7, 150, 169, "Female", "fuchsia")
    imbox.draw(image, 116, 7, 193, 113, "Male", "blue")
    imbox.draw(image, 189, 7, 291, 124, "Female", "fuchsia")
    imbox.draw(image, 288, 25, 355, 114, "Male", "blue")
    imbox.draw(image, 367, 0, 448, 92, "Male", "blue")
    imbox.draw(image, 435, 29, 506, 104, "Female", "fuchsia")
    imbox.draw(image, 497, 3, 597, 111, "Female", "fuchsia")
    imbox.draw(image, 110, 133, 213, 245, "Female", "fuchsia")
    imbox.draw(image, 176, 120, 293, 289, "Female", "fuchsia")
    imbox.draw(image, 314, 115, 470, 357, "Male", "blue")
    imbox.draw(image, 468, 72, 577, 226, "Male", "blue")
    show_and_save("The Selfie", image, out_path)

    in_path = os.path.join("docs", "images", "poimbox.jpg")
    out_path = os.path.join("docs", "images", "poimbox_imbox.png")
    image = cv2.imread(in_path, cv2.IMREAD_COLOR)
    imbox.draw(image, 76, 62, 155, 271, "Female", "fuchsia")
    imbox.draw(image, 157, 44, 288, 274, "Male", "blue")
    imbox.draw(image, 224, 64, 317, 274, "Male", "blue")
    imbox.draw(image, 290, 48, 383, 277, "Male", "blue")
    imbox.draw(image, 350, 42, 458, 276, "Female", "fuchsia")
    imbox.draw(image, 416, 17, 510, 279, "Male", "blue")
    imbox.draw(image, 482, 55, 573, 278, "Female", "fuchsia")
    imbox.draw(image, 547, 63, 615, 277, "Female", "fuchsia")
    imbox.draw(image, 608, 49, 704, 275, "Female", "fuchsia")
    imbox.draw(image, 672, 34, 767, 274, "Male", "blue")
    imbox.draw(image, 725, 62, 813, 273, "Female", "fuchsia")
    imbox.draw(image, 786, 38, 887, 267, "Male", "blue")
    imbox.draw(image, 864, 51, 959, 266, "Male", "blue")
    show_and_save("POBB", image, out_path)

if __name__ == "__main__":
    main()
