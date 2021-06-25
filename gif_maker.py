from PIL import Image as im 
import glob
import os


def create_gif(folder):
    frame = []
    new_folder = folder + "/*.png"
    img = glob.glob(new_folder)

    for i in img:
        cur_img = im.open(i)
        frame.append(cur_img)
    
    path = folder + ".gif"
    frame[0].save(path , format = "GIF" , append_images=frame[1:], save_all=True, duration=100, loop=0)


cwd = os.getcwd()
folder = os.listdir(cwd)

for x in folder:
    if os.path.isdir(x):
        create_gif(x)