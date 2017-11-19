from PIL import Image
import numpy as np
import string


def read_file(file_name, words=False):
    content = []

    with open(file_name, "r") as f_read:
        for line in f_read:
            if words:
                splitted_words = line.rstrip().split()
                for single_word in splitted_words:
                    content.append(single_word.translate(None, string.punctuation))
            else:
                content.append(line.rstrip())
    
    return content


def write_annotation_file(annotations, file_name):
    with open(file_name, "w") as f_write:
        for annotation in annotations:
            f_write.write(str(annotation) + "\r\n")


def create_directory_if_not_exists(dir_name):
    import os
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def write_image(img, path):
    im = Image.fromarray(img)
    im.save(path)


def read_image(path):
    img = Image.open(path)
    return np.array(img)