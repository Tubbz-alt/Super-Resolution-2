# ESRGAN-pytorch

[ESRGAN: Enhanced Super-Resolution Generative Adversarial Networks](https://arxiv.org/abs/1809.00219)

### Test Code

Pass the LR directory containing low resolution images and pass  
SR directory to store the Super resolved images

```bash
python src/test.py --lr_dir LR_DIR --sr_dir SR_DIR
```

## Prepare dataset

### DIV2K dataset for training

```bash
cd datasets
python prepare_datasets.py
cd ..
```

### custom dataset

Make dataset like this; size of hr is 128x128 and size for lr is 32x32

```
datasets/
    hr/
        0001.png
        sdf.png
        0002.png
        0003.png
        0004.png
        ...
    lr/
        0001.png
        sdf.png
        0002.png
        0003.png
        0004.png
        ...
```

## how to train

Running for 10 epochs will take a lot of time, so if you are training  
on cloud provider pass 1 or 2. If you wouldn't pass anything it takes 10  
as default.

```bash
python main.py --is_perceptual_oriented True --num_epoch=10
python main.py --is_perceptual_oriented False --epoch=10
```
