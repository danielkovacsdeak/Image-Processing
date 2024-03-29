import os
import PIL.Image
import ipywidgets

SIZE, index = 0, 0
for image_file_name in os.listdir('C:\\Users\\Afaui\\Documents\\a Tanulmányok\\Projektek\\Image Processing\\'):
    if image_file_name.endswith(".png"):
        SIZE += 1
pb = ipywidgets.IntProgress(max = SIZE - 1)
display(pb)

for image_file_name in os.listdir('C:\\Users\\Afaui\\Documents\\a Tanulmányok\\Projektek\\Image Processing\\'):
    if image_file_name.endswith(".png"):
        pb.value = index
        
        index += 1

        im = PIL.Image.open('C:\\Users\\Afaui\\Documents\\a Tanulmányok\\Projektek\\Image Processing\\' + image_file_name)
        
        width, height = im.size
        new_width = int(width / 2) # 600 dpi -> 300 dpi for both dimensions
        new_height = int(height / 2)
        
        im = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
        im.save('C:\\Users\\Afaui\\Documents\\a Tanulmányok\\Projektek\\Image Processing\\' + image_file_name)