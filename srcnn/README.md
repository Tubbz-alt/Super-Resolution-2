# SRCNN


## Train

```bash
python train.py --train-file "BLAH_BLAH/91-image_x3.h5" \
                --eval-file "BLAH_BLAH/Set5_x3.h5" \
                --outputs-dir "BLAH_BLAH/outputs" \
                --scale 3 \
                --lr 1e-4 \
                --batch-size 16 \
                --num-epochs 400 \
                --num-workers 8 \
                --seed 123                
```

## Test


```bash
python test.py --weights-file "BLAH_BLAH/srcnn_x3.pth" \
               --image-file "data/butterfly_GT.bmp" \
               --scale 3
```

PSNR was calculated on the Y channel.

## Results

| Eval. Mat | Scale | SRCNN | Dataset |
|-----------|-------|-------|--------------|
| PSNR | 2 | 36.99 | Set5 |
| PSNR | 2 | 32.34 | Set14 |
| PSNR | 4 | 32.80 | Set5 |

