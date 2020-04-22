"""Main module."""
import cv2
import os
import shutil
from PIL import Image

def mp42images(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    n = 0
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

def images2gif(dir_path, basename, length ,ext='jpg'):
    imgs = []
    digit = len(str(length))
    base_path = os.path.join(dir_path, basename)
    n = 0
    for i in range(length):
        im = Image.open('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext))
        n += 1
        imgs.append(im.copy())
    imgs[0].save('test.gif', save_all=True, append_images=imgs[1:], duration=30, loop=0)
    shutil.rmtree('result')



def mp4togif(video_path, basename):
    dir_path = 'result'
    length = mp42images(video_path, dir_path, basename)
    images2gif(dir_path, basename, length)

mp4togif("F:\\User\Videos\\Final Fantasy XIV  A Realm Reborn\\Final Fantasy XIV  A Realm Reborn 2020.04.12 - 22.22.31.02.DVR_Trim.mp4", "sample")
