import os
import argparse
from PIL import Image

output_dir = 'cropped_images'

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
    for key, fname in enumerate(walk_through_files(path)):
        print(str(key) + '.jpg')
        img = Image.open(fname)
        hight = img.size[1] * 0.9
        width = 640 * hight / 480
        start_width = (img.size[0] - width)/2
        end_width = start_width + width
        box = (start_width,0,end_width,hight)
        img = img.crop(box)
        img.save(dir + '/' + str(key) + '.jpg', 'JPEG')

# object_detection_docker/test_images
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required = True, help="path to directory with images")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    main(path)
