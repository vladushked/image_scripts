import os
import argparse
import datetime
from PIL import Image

output_dir = 'cropped_images'

def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
         if filename.lower().endswith(file_extension) and not dirpath.startswith(f'{path}/{output_dir}'):
            yield os.path.join(dirpath, filename)
    
def main(path, ratio):
    dir = output_dir
    try:
        os.mkdir(dir)
    except OSError:
        print ("%s already created" % dir)
    else:
        print ("Successfully created %s " % dir)
    for fname in walk_through_files(path):
        print(str(datetime.datetime.now().date()) + str(datetime.datetime.now().time()) + '.jpg')
        img = Image.open(fname)
        hight = img.size[1] * ratio
        width = 640 * hight / 480
        box = (0,0,width,hight)
        img = img.crop(box)
        img.save(dir + '/' + str(datetime.datetime.now().date()) + str(datetime.datetime.now().time()) + '.jpg', 'JPEG')

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required = True, help="path to directory with images")
    ap.add_argument("-r", "--ratio", default=0.9, help="FLOAT hight aspect ratio. Ex: 0.9")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    ratio = float(args["ratio"])
    main(path, ratio)
