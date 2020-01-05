# chainer-dcgan-colab

## Prepare

### download

    python3 google_images_download.py -k ""

### convert

    python convert-jpg.py images
    
    python resize.py images

    python decolor.py 224/images

    generator.py --gen result/gen_iter_24500.npz --out dist
        
## original

    https://github.com/chainer/chainer/tree/master/examples/dcgan
