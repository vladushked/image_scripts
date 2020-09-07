import os
import argparse
from PIL import Image
import subprocess


output_dir = 'enhanced_images'
tmp_dir = 'tmp'


def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.lower().endswith(file_extension) and not dirpath.startswith(f"{path}/{output_dir}"):
                yield dirpath, filename


def main(path, L):
    try:
        os.mkdir(output_dir)
    except OSError:
        print(f"{output_dir}/ already created")
    else:
        print(f"Successfully created {output_dir}/")
    try:
        os.mkdir(tmp_dir)
    except OSError:
        print(f"{tmp_dir}/ already created")
    else:
        print(f"Successfully created {tmp_dir}/")
    for dirpath, filename in walk_through_files(path):
        png_filename = filename[:-4] + '.png'
        img = Image.open(os.path.join(dirpath, filename))
        img.save(tmp_dir + '/' + png_filename, 'PNG')
        bashCommand = f"screened_poisson/screened_poisson {L} {tmp_dir}/{png_filename} {tmp_dir}/sbc_{png_filename} {output_dir}/{png_filename}"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        print(filename + ' processed')
        os.remove(f'{tmp_dir}/{png_filename}')
        os.remove(f'{tmp_dir}/sbc_{png_filename}')
        img = Image.open(os.path.join(output_dir, png_filename))
        img.save(output_dir + '/' + filename, 'JPEG')
        os.remove(f'{output_dir}/{png_filename}')
    os.rmdir(f'{tmp_dir}')


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required=True,
                    help="path to directory with images")
    ap.add_argument("-l", "--screened_poisson_L", default=0.0003,
                    help="the tradeoff parameter of the functional in (0, 2]")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    L = args['screened_poisson_L']
    main(path, L)