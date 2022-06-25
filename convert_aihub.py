import os
import sys
import json
import argparse
from PIL import Image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_image_dir')
    parser.add_argument('--input_label_dir')
    parser.add_argument('--output_dir')
    opt = parser.parse_args()

    images_list = os.listdir(opt.input_image_dir)
    label_list = os.listdir(opt.input_label_dir)

    with open(opt.output_dir+"gt.txt", "w") as f:
        for folder_num in images_list:
            for name in os.listdir(opt.input_label_dir):
                if name.split(".")[1] == "json":
                    name = name.split(".")[0]

                    json_path = opt.input_label_dir+name+".json"
                    with open(json_path, 'r') as file:
                        data = json.load(file)
                    
                    for i, word in enumerate(data["text"]["word"]):
                        img = Image.open(opt.input_image_dir+name+".jpg")
                        img_crop = img.crop((word["wordbox"][0], word["wordbox"][1], word["wordbox"][2], word["wordbox"][3]))
                        img_crop.save(opt.output_dir+"images/"+name+"_"+str(i)+".jpg")
                        f.write("images/"+name+"_"+str(i)+".jpg\t"+word["value"]+"\n")
