import os
import glob
import sys
import traceback
from PIL import Image
from pathlib import Path

image_dir = sys.argv[1] + '/**/*'
files = glob.glob(image_dir)
SIZE = int(sys.argv[2])
LOCATION = '01-'

# for f in files:
#     try:
#         title, ext = os.path.splitext(f)
#         print(str(SIZE) + "/" + title + ext)
#         Path(LOCATION + str(SIZE) + "/" + os.path.dirname(f)).mkdir(parents=True, exist_ok=True)
#         img = Image.open(f).convert('RGB')
#         img.thumbnail((SIZE, SIZE), Image.ANTIALIAS)
#         img.save(LOCATION + str(SIZE) + "/" + title + ext)
#
#     except Exception as e:
#         print("Exception in user code:")
#         print('-' * 60)
#         traceback.print_exc(file=sys.stdout)
#         print('-' * 60)
#     finally:
#         pass

for f in files:
    try:
        title, ext = os.path.splitext(f)
        print(str(SIZE) + "/" + title + ext)
        Path(LOCATION + str(SIZE) + "/" + os.path.dirname(f)).mkdir(parents=True, exist_ok=True)
        img = Image.open(f).convert('RGB')
        img_resize = img.resize((SIZE, SIZE))
        img_resize.save(LOCATION + str(SIZE) + "/" + title + ext)

    except Exception as e:
        print("Exception in user code:")
        print('-' * 60)
        traceback.print_exc(file=sys.stdout)
        print('-' * 60)
    finally:
        pass
