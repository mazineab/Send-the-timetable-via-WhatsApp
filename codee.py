import os
import time
import pywhatkit
from PIL import Image
import easyocr
class Code:
    def test(self):
        import numpy as np


        folder="img"
        names=os.listdir(folder)
        for x in names:
            image_path = os.path.join(folder,x)
            myimg=Image.open(image_path)
            cut=(230,70,350,100)
            newimg=myimg.crop(cut)
            img = np.array(newimg)
            reader=easyocr.Reader(['en'],gpu=True)
            res=reader.readtext(img)
            if res:
                name=res[0][1].strip()
                time.sleep(1)
                file_path = "client/data.txt"
                print(f"______________{name}____________")
                try:
                    with open(file_path, 'r') as file:
                        for line in file:
                            line_array = line.strip().split()
                            if name==line_array[0] or name==line_array[1]:
                                pywhatkit.sendwhats_image(line_array[3],image_path,line_array[2])
                                time.sleep(4)
                            else:
                                print("noooo")
                except :
                    print("file not found")
            else:
                print("Text extraction failed")



