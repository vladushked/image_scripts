import os
import argparse
import datetime
from PIL import Image

output_dir = 'resized_images'

def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
         if filename.lower().endswith(file_extension) and not dirpath.startswith(f'{path}/{output_dir}'):
            yield os.path.join(dirpath, filename)
    
def main(path):
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
        img = img.resize((640,480), Image.ANTIALIAS)
        img.save(dir + '/' + str(datetime.datetime.now().date()) + str(datetime.datetime.now().time()) + '.jpg', 'JPEG')

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required = True, help="path to directory with images")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    main(path)
