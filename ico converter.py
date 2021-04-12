import os

def ico_convert(filename):
    from PIL import Image
    img=Image.open(filename)
    filename=filename.replace(filename[len(filename)-4:],'.ico')
    print(filename)
    img.save(f'{filename}', format='ico')


file_list=[]
ico='.ico'
png='.png'
this_file='ico converter.py'

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename!=this_file:
            file_list.append(filename)
            
br=0
convert=[]

for i in file_list:
    file=file_list[i]
    file=file[:len(file)-4]
    if (file+ico) not in file_list:
        ico_convert(file+ico)
        br+=1
        convert.append(file+png)

if br==0:
    print('no files have been converted')

else:
    print('the following files have been converted:')
    for i in range (len(convert)):
        print(f'{convert[i]}')
        
        
