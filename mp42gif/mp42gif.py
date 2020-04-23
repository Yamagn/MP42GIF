"""Main module."""
import cv2
import os
import shutil
from PIL import Image

def crop_center(im, crop_width, crop_height):
    img_width, img_height = im.size
    return im.crop(((img_width - crop_width) // 2,
                   (img_height - crop_height) // 2,
                   (img_width + crop_width) // 2,
                   (img_height + crop_height) // 2))

def mp42images(video_path, basename, quality, crop, ext='jpg'):
    dir_path = 'result'
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    while True:
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if quality == "high":
            rate = 1
        elif quality == "middle":
            rate = 3
        elif quality == "low":
            rate = 5
        else:
            rate = 1
        if ret:
            im = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if crop == "center":
                im = crop_center(im, 1120, 630)
            resized_frame = im.resize((int(im.width / rate), int(im.height / rate)))
            resized_frame.save('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext))
            n += 1
        else:
            return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def images2gif(dir_path, basename, length, ext='jpg'):
    imgs = []
    digit = len(str(length))
    images_path = 'result'
    base_path = os.path.join(images_path, basename)
    save_dir = os.path.join(dir_path, basename)
    n = 0
    while True:
        if n < length:
            im = Image.open('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext))
            n += 1
            imgs.append(im.copy())
        else:
            break
    imgs[0].save('{}.gif'.format(save_dir), save_all=True, append_images=imgs[1:], duration=30, loop=0)
    shutil.rmtree('result')



def mp4togif(video_path, dir_path, basename, quarity="high", crop="none", ext="jpg"):
    length = mp42images(video_path, basename, quarity, crop, ext)
    images2gif(dir_path, basename, length, ext)
