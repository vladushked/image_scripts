import os
import argparse
import json

output_json = 'images.json'
domain_name = 'http://hydronautics.bmstu.ru/sauvc_images/'

def walk_through_files(path, file_extension=('.jpg', '.jpeg')):
   for (dirpath, dirnames, filenames) in os.walk(path):
      for filename in filenames:
         if filename.lower().endswith(file_extension):
            yield filename

def main(path, domain_name):
    data = []
    for fname in walk_through_files(path):
        data.append({'image':domain_name + fname})
    if os.path.isfile(output_json):
        os.remove(output_json)
    with open(output_json, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--path_to_images", required = True, help="path to directory with images")
    ap.add_argument("-d", "--domain_name", help="domain name")
    args = vars(ap.parse_args())
    path = args["path_to_images"]
    if args["domain_name"] is not None:
        domain_name = args["domain_name"]

    main(path, domain_name)