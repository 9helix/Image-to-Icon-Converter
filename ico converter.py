import os
from PIL import Image
import webbrowser

def ico_convert(filename):
    img=Image.open(png_path+filename)
    filename=filename.replace(filename[len(filename)-4:],'.ico')
    img.save(ico_path+filename, format='ico')
    

png_list=[]
ico_list=[]
ico='.ico'
png='.png'
this_file='png to ico.py'
dir_path = os.path.dirname(os.path.realpath(__file__))
png_path = dir_path+'\PNG/'
ico_path = dir_path+"\ICO/"

for entry in os.listdir(png_path):
    if os.path.isfile(os.path.join(png_path, entry)):
        entry=entry[:len(entry)-4]
        png_list.append(entry)

for entry in os.listdir(ico_path):
    if os.path.isfile(os.path.join(ico_path, entry)):
        entry=entry[:len(entry)-4]
        ico_list.append(entry)           

br=0
converted=[]

for file in png_list:
    if file in ico_list:
        None
    if file not in ico_list:
        filename=file+png
        ico_convert(rf'{filename}')
        br+=1
        converted.append(file)
        os.remove(png_path+filename)

f=open('log.txt','w')
if br==0:
    print('No files have been converted.')
    f.write('No files have been converted.')

else:    
    print(f'{len(converted)} files have been converted: \n')
    f.write(f'{len(converted)} files have been converted: \n')
    for i in range (len(converted)):
        print(converted[i]+'.png')
        f.write(converted[i]+'.png'+'\n')
f.close()
webbrowser.open('log.txt')


        
