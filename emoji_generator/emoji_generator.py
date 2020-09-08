"""
infos :
    emoji_resolution = 32x32
    size < 256 kb
    depth 1 : the depth things = 25% => 8px
    depth 2 : 4px
    depth 3 : 2px
    depth 4 : 1px
    discord_background_color = rgb(54,57,63)
    bloc_background_color = rgb(53,56,61)

goal :
    actually only the rdepth_model is not generated
    generate images in 32x32 with bloc_background_color with some weid depth things left and right
    (still don't know how to do the weird depth things)
        - just copie from the image (objectif.png) and past ?
        - idea 
            left and right : dégradé de rgb(19,20,22) to bloc_background_color
            up down : (don't freaking know)
"""

import numpy as np
import cv2
import os

DISCORD_EMOJIS_EQ = {}
RESOLUTION = (32, 32, 3)  # the third dimension is for the 3 color layers
BLOC_BGC = (53, 56, 61)  # color
SELECTED_BLOC_BGC = (200, 50, 50)
DISCORD_BGC = (54, 57, 63)  # color
ALLBLOC = ['', 'r', 'l', 'u', 'd', 'rl', 'ru', 'rd',
           'lu', 'ld', 'ud', 'rlu', 'rld', 'rud', 'lud', 'rlud', 's', 'sr', 'sl', 'su', 'sd', 'srl', 'sru', 'srd', 'slu', 'sld', 'sud', 'srlu', 'srld', 'srud', 'slud', 'srlud', 'i']  # flemme de générer manuellement x)
DISCORD_EMOJIS_EQ = {i: f"{i}depth_block" for i in ALLBLOC}
DIR_PATH = os.path.dirname(os.path.realpath(__file__))


def read_rmodel():
    return cv2.imread(f"{DIR_PATH}/assets/rdepth_model.jpg")


def write_asset(depth_model, model_type):
    cv2.imwrite(f"{DIR_PATH}/assets/{model_type}depth_model.jpg", depth_model)


def read_create_model(model_type):
    if model_type == 'r':
        return read_rmodel()
    elif model_type == 'u':
        depth_model = np.rot90(read_rmodel())
        write_asset(depth_model, 'u')
        return depth_model
    elif model_type == 'd':
        depth_model = np.rot90(read_rmodel(), 3)
        write_asset(depth_model, 'd')
        return depth_model
    elif model_type == 'l':
        depth_model = np.flip(read_rmodel(), 1)
        write_asset(depth_model, 'l')
        return depth_model


def generate_base(color=BLOC_BGC):
    img = np.zeros(RESOLUTION)
    img[:, :, 0] = color[2]
    img[:, :, 1] = color[1]
    img[:, :, 2] = color[0]
    return img


def generate_r(img):
    depth_model = read_rmodel()

    assert img.shape[0] >= depth_model.shape[0] and img.shape[1] >= depth_model.shape[1]

    img[
        img.shape[0]-depth_model.shape[0]: img.shape[0],
        img.shape[1]-depth_model.shape[1]: img.shape[1],
        0
    ] = depth_model[:, :, 0]
    img[
        img.shape[0]-depth_model.shape[0]:img.shape[0],
        img.shape[1]-depth_model.shape[1]:img.shape[1],
        1
    ] = depth_model[:, :, 1]
    img[
        img.shape[0]-depth_model.shape[0]:img.shape[0],
        img.shape[1]-depth_model.shape[1]:img.shape[1],
        2
    ] = depth_model[:, :, 2]

    return img


def generate_l(img):
    depth_model = read_create_model('l')

    assert img.shape[0] >= depth_model.shape[0] and img.shape[1] >= depth_model.shape[1]

    img[
        0: depth_model.shape[0],
        0: depth_model.shape[1],
        0
    ] = depth_model[:, :, 0]
    img[
        0:depth_model.shape[0],
        0:depth_model.shape[1],
        1
    ] = depth_model[:, :, 1]
    img[
        0:depth_model.shape[0],
        0:depth_model.shape[1],
        2
    ] = depth_model[:, :, 2]

    return img


def generate_d(img):
    depth_model = read_create_model('d')

    assert img.shape[0] >= depth_model.shape[0] and img.shape[1] >= depth_model.shape[1]

    img[
        img.shape[0]-depth_model.shape[0]: img.shape[0],
        img.shape[1]-depth_model.shape[1]: img.shape[1],
        0
    ] = depth_model[:, :, 0]
    img[
        img.shape[0]-depth_model.shape[0]:img.shape[0],
        img.shape[1]-depth_model.shape[1]:img.shape[1],
        1
    ] = depth_model[:, :, 1]
    img[
        img.shape[0]-depth_model.shape[0]:img.shape[0],
        img.shape[1]-depth_model.shape[1]:img.shape[1],
        2
    ] = depth_model[:, :, 2]

    return img


def generate_u(img):
    depth_model = read_create_model('u')

    assert img.shape[0] >= depth_model.shape[0] and img.shape[1] >= depth_model.shape[1]

    img[
        0: depth_model.shape[0],
        0: depth_model.shape[1],
        0
    ] = depth_model[:, :, 0]
    img[
        0:depth_model.shape[0],
        0:depth_model.shape[1],
        1
    ] = depth_model[:, :, 1]
    img[
        0:depth_model.shape[0],
        0:depth_model.shape[1],
        2
    ] = depth_model[:, :, 2]

    return img


def generate_bloc(bloctype):
    print(f"generating {bloctype}...")
    if bloctype == "i":
        return (generate_base(DISCORD_BGC), "idepth_block")
    else:
        if 's' in bloctype:
            img = generate_base(SELECTED_BLOC_BGC)
        else:
            img = generate_base()
        if 'r' in bloctype:
            img = generate_r(img)
        if 'l' in bloctype:
            img = generate_l(img)
        if 'd' in bloctype:
            img = generate_d(img)
        if 'u' in bloctype:
            img = generate_u(img)
        return (img, f"{bloctype}depth_block")


def write_emoji(img, name):
    cv2.imwrite(f"{DIR_PATH}/emojies/{name}.png", img)


def gen_write_all():
    print('generating all emojies...')
    for bloctype in ALLBLOC:
        write_emoji(*generate_bloc(bloctype))
    print('all emojies generated')


if __name__ == "__main__":
    gen_write_all()
