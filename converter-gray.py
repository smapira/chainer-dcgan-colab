import sys
import cv2
import glob
import os
from pathlib import Path

image_dir = sys.argv[1] + '/**/*'
new_image_dir = '03-gray'

files = glob.glob(image_dir)
for fn in files:
    if fn == '.DS_Store':
        continue
    Path(str(new_image_dir) + "/" + os.path.dirname(fn)).mkdir(parents=True, exist_ok=True)

    img_bgr = cv2.imread(fn)
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('%s/%s' % (new_image_dir, fn), img_gray)

    # img = cv2.imread(fn)
    # img_gray, _ = cv2.decolor(img)
    # cv2.imwrite('%s/%s' % (new_image_dir, fn), img_gray)
