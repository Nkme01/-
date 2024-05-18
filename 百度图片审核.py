import os
import shutil
from tqdm import tqdm
from aip import AipContentCensor
from PIL import Image,ImageDraw,ImageFont
print('@Nkme01 to:24.5.16 V0.0.0516.beta')
APP_ID=input("输入你的APP_ID:")  
APP_KEY=input("输入你的APP_KEY:")
SECRET_KEY=input("输入你的SECRET_KEY:")
client=AipContentCensor(APP_ID,APP_KEY,SECRET_KEY)

DHT = input("输入文件路径: ")

dir_files = os.listdir(DHT)
print('当前有', len(dir_files), '个图片文件', dir_files)

#判断有无文件冲突
while True:
    Nkme = os.path.join(input("输入新建文件路径与名字: "))  # 自定义文件夹输入地址+DHT
    if not os.path.exists(Nkme):
        os.mkdir(Nkme)  # 建一个文件夹   
        break
    else: 
        print('\n', Nkme, '已存在,换个名字')
print('\n复制图片中.....')

#定义一个函数
def generate_new_name(index):
    return f"{index:03}.{'png' if file.endswith('.png') else 'jpg' if file.endswith('.jpg') else 'webp' if file.endswith('.webp') else 'gif'}"#如果是png则返回png否者为jpg

#复制改名
index = 1
for file in tqdm(dir_files):#几个文件循环几次
    if file.endswith(('.png', '.jpg', '.webp', '.gif')):#swith语句有再处理
        new_name = generate_new_name(index)
        shutil.copyfile(os.path.join(DHT, file), os.path.join(Nkme, new_name))  # 如果在输入找到了png则放入自定义文件夹地址
        #print(file, '已复制为', new_name)
        index += 1                                                                #重命名成001.002这样的然后检索所有
    jpgid=os.path.join(Nkme, new_name)
    fo=open(jpgid,'rb')
    img=fo.read()
    fo.close()
    ssd=client.imageCensorUserDefined(img)
    #print(ssd)
    k1=jpgid
    jpg001=Image.open(k1)
    font = ImageFont.truetype("C:/Windows/Fonts/STXINWEI.TTF", 45)
    draw=ImageDraw.Draw(jpg001)
    draw.text((0,0),str(ssd),fill='red',font=font)
    jpg001.save(os.path.join(Nkme, new_name))
print("完成")   



