import os
import glob
import sys
from pathlib import Path
from PIL import Image

image_dir = sys.argv[1] + '/**/*'
new_image_dir = 'rakkan/jpg'
files = glob.glob(image_dir)

for f in files:
    if f == '.DS_Store':
        continue
    Path(str(new_image_dir) + "/" + os.path.dirname(f)).mkdir(parents=True, exist_ok=True)
    img = Image.open(f).convert('RGB')
    img.save('%s/%s' % (new_image_dir, f.replace('.png', '.jpg')))
    img.save('%s/%s' % (new_image_dir, f.replace('.gif', '.jpg')))
    print('%s/%s' % (new_image_dir, f.replace('.png', '.jpg')))
