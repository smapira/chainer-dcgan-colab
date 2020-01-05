import sys
import glob
import os
from pathlib import Path
from PIL import Image
from collections import defaultdict

image_dir = sys.argv[1] + '/**/*'
new_image_dir = '04-rgb'
files = glob.glob(image_dir)

for fn in files:
    if fn == '.DS_Store':
        continue
    Path(str(new_image_dir) + "/" + os.path.dirname(fn)).mkdir(parents=True, exist_ok=True)
    img = Image.open(fn)
    rgbimg = Image.new("RGB", img.size)
    rgbimg.paste(img)

    found_colors = defaultdict(int)
    for x in range(0, rgbimg.size[0]):
        for y in range(0, rgbimg.size[1]):
            pix_val = rgbimg.getpixel((x, y))
            found_colors[pix_val] += 1

    print('%s/%s' % (new_image_dir, fn))
    rgbimg.save('%s/%s' % (new_image_dir, fn))
