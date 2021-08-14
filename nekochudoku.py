import cv2
import cv2 as cv
import os
import time
from PIL import Image

# 逐帧提取视频
video_path = 'F:\download\maozhongdu.mp4'  # 视频文件地址，是视频文件
timeF = 1  # 隔timeF帧截一次图，1表示全截


images_path = video_path.split('.', 1)[0]
if not os.path.exists(images_path):  # 文件夹不存在则新建
    os.mkdir(images_path)

vc = cv2.VideoCapture(video_path) # 读入视频文件
c = 1
rat = 1
if vc.isOpened(): # 判断是否正常打开
    print('视频读取成功，正在逐帧截取...')
    while rat:  # 循环读取视频帧
        rat, frame = vc.read()  # frame为一帧图像，当frame为空时，ret返回false，否则为true
        if(c%timeF == 0 and rat == True): # 每隔timeF帧截一次图像
            cv2.imwrite(images_path + '/' +  str(c) + '.jpg',frame)
        c = c + 1
    vc.release()
    print('截取完成，图像保存在：%s' %images_path)
else:
    print('视频读取失败，请检查文件地址')



# 视频转换
ascii_char = list("!#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
WIDTH = 455
HEIGHT = 90
# WIDTH, HEIGHT = os.get_terminal_size()
# 获取控制台大小，pycharm会句柄错误，所以这里的长宽是自己调的

def get_char_from_pixel(r, g, b, alpha=255.):
    if alpha == 0:
        return ''

    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (255.0 + 1) / length
    return ascii_char[int(gray / unit)]


def ascii_pic_from_pil(path):
    text = ""
    img = Image.open(path)
    img = img.resize((WIDTH, HEIGHT), Image.NEAREST)

    for h in range(img.size[1]):
        for w in range(img.size[0]):
            text += get_char_from_pixel(*img.getpixel((w, h)))
        text += '\n'
    return text

t = time.time()
for i in range(1, 4210, 4):
    # WIDTH = os.get_terminal_size().columns
    # HEIGHT = os.get_terminal_size().lines # 获取控制台大小
    # im = ascii_pic_from_pil('./1/{}.jpg'.format(i))
    im = ascii_pic_from_pil('F:\Download\maozhongdu\{}.jpg'.format(i))
    os.system("cls")
    print(im)
    # print(i / time.time() - t)


