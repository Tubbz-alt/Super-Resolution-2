import os
import shutil
from preparation.utils import download_url, unzip_zip_file, unzip_tar_file
from glob import glob


'''
Downloading the DIV2K HR and LR images and then unzipping it 
and then reformatting the images
'''
def download_dataset():
    DIV2K_HR = "http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip"
    DIV2K_LR = "http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_LR_bicubic_X4.zip"

    if not os.path.exists('temp'):
        os.makedirs('temp')

    if not os.path.exists(os.path.join('hr')):
        os.makedirs(os.path.join('hr'))
    if not os.path.exists(os.path.join('lr')):
        os.makedirs(os.path.join('lr'))

    download_url(DIV2K_HR, os.path.join('temp', 'DIV2K_HR.zip'))
    download_url(DIV2K_LR, os.path.join('temp', 'DIV2K_LR.zip'))

    print('[!] Upzip zipfile')
    unzip_zip_file(os.path.join('temp', 'DIV2K_HR.zip'), 'temp')
    unzip_zip_file(os.path.join('temp', 'DIV2K_LR.zip'), 'temp')

    print('[!] Reformat DIV2K HR')
    image_path = glob('temp/DIV2K_train_HR/*.png')
    image_path.sort()
    for index, path in enumerate(image_path):
        shutil.move(path, os.path.join('hr', f'{index:04d}.png'))

    print('[!] Reformat DIV2K LR')
    image_path = glob('temp/DIV2K_train_LR_bicubic/X4/*.png')
    image_path.sort()
    for index, path in enumerate(image_path):
        shutil.move(path, os.path.join('lr', f'{index:04d}.png'))

    shutil.rmtree('temp')
