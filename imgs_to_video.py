import os
import argparse
import cv2


def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
    for (dirpath, _, filenames) in os.walk(path):
        filenames = sorted(filenames)
        for filename in filenames:
            if filename.lower().endswith(file_extension):
                yield os.path.join(dirpath, filename)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required=True,
                    help="path to directory with images")
    ap.add_argument("-n", "--output_name",
                    default="video.avi", help="output name")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    name = args["output_name"]
    size = (320, 240)

    while (os.path.isfile(name)):
        idx = name.index(".")
        name = name[:idx] + "0" + name[idx:]
    print(name)
    out = cv2.VideoWriter(name, cv2.VideoWriter_fourcc(*'DIVX'), 30, size)

    for fname in walk_through_files(path):
        img = cv2.imread(fname)
        img = cv2.resize(img, size)
        out.write(img)
    out.release()
