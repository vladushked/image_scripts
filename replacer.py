import os
import argparse
import datetime
from PIL import Image

output_dir = 'enhanced_images'


def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(file_extension) and not dirpath.startswith(f"{path}/{output_dir}"):
                yield filename


def main(images_to_replace, path_to_fine_images):
    try:
        os.mkdir(output_dir)
    except OSError:
        print(f"{output_dir}/ already created")
    else:
        print(f"Successfully created {output_dir}/")
    for filename in walk_through_files(images_to_replace):
        img = Image.open(os.path.join(path_to_fine_images, filename))
        print(os.path.join(images_to_replace, filename))
        img.save(os.path.join(images_to_replace, filename))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images_to_replace", required=True,
                    help="path to directory with images to replace")
    ap.add_argument("-f", "--path_to_fine_images", required=True,
                    help="path to directory with fine images")
    args = vars(ap.parse_args())
    images_to_replace = args["images_to_replace"]
    path_to_fine_images = args["path_to_fine_images"]
    main(images_to_replace, path_to_fine_images)
