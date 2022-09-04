from PIL import Image

import os

def resize_img(dir_path_og, dir_path_rs):

    img_list = os.listdir(dir_path_og)

    for img in img_list:
        im = Image.open(dir_path_og+img)

        width, height = im.size
        img_resized = im.resize((int(width*.68), height))
        img_resized.save(dir_path_rs+img)


if __name__=="__main__":
    resize_img("pictures/original/", "pictures/resized/")