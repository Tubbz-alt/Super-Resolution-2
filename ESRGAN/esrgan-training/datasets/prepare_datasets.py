from preparation.download_images import download_dataset
from preparation.make_patches import make_patches

if __name__ == '__main__':
    download_dataset()
    make_patches()