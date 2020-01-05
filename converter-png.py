from PIL import Image
import os
import sys
import glob
from pathlib import Path

image_dir = sys.argv[1] + '/**/*'
new_image_dir = '02-png'
files = glob.glob(image_dir)

for f in files:
    if f == '.DS_Store':
        continue
    Path(str(new_image_dir) + "/" + os.path.dirname(f)).mkdir(parents=True, exist_ok=True)

    im = Image.open(f)
    im.save('%s/%s' % (new_image_dir, f.replace('.jpg', '.png')))
    print('%s/%s' % (new_image_dir, f.replace('.jpg', '.png')))
