# 图片加水印
# 功能：
# pic_watermark：基于FFT,将图片信息嵌入载体图片
# word_watermark：基于LSB,将文字信息嵌入载体图片
import cv2
import numpy as np
import random
import os
from PIL import Image


# 图片水印
class pic_watermark():
    def __init__(self, img_path=None, wm_path=None, origin_path=None, alpha=5):
        self.img_path = img_path
        self.alpha = alpha
        self.wm_path = wm_path
        self.origin_path = origin_path

    # 加水印
    def encode(self):
        if not (self.img_path and self.wm_path):
            print('[Error]:IMAGE FILE LOST...')
            return None
        img = cv2.imread(self.img_path)
        img_fft = np.fft.fft2(img)
        height, width, channel = np.shape(img)
        watermark = cv2.imread(self.wm_path)
        wm_height, wm_width = watermark.shape[0], watermark.shape[1]
        x, y = list(range(height // 2)), list(range(width // 2))
        random.seed(height + width)
        random.shuffle(x)
        random.shuffle(y)
        temp = np.zeros(img.shape)
        # 频谱中心对称，水印也要对称
        for i in range(height // 2):
            for j in range(width // 2):
                if x[i] < wm_height and y[j] < wm_width:
                    temp[i][j] = watermark[x[i]][y[j]]
                    temp[height - 1 - i][width - 1 - j] = temp[i][j]
        result_fft = img_fft + self.alpha * temp
        result = np.fft.ifft2(result_fft)
        result = np.real(result)
        if not os.path.exists('./results/FFT'):
            os.makedirs('./results/FFT')
        cv2.imwrite('./results/FFT/encode.png', result, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        print('[INFO]:Watermark Successfully...')

    # 解水印
    def decode(self):
        if not (self.img_path and self.origin_path):
            print('[Error]:IMAGE FILE LOST...')
            return None
        origin_img = cv2.imread(self.origin_path)
        img = cv2.imread(self.img_path)
        origin_img_fft = np.fft.fft2(origin_img)
        img_fft = np.fft.fft2(img)
        height, width = origin_img.shape[0], origin_img.shape[1]
        watermark = (origin_img_fft - img_fft) / self.alpha
        watermark = np.real(watermark)
        result = np.zeros(watermark.shape)
        random.seed(height + width)
        x = list(range(height // 2))
        y = list(range(width // 2))
        random.shuffle(x)
        random.shuffle(y)
        for i in range(height // 2):
            for j in range(width // 2):
                result[x[i]][y[j]] = watermark[i][j]
        if not os.path.exists('./results/FFT'):
            os.makedirs('./results/FFT')
        cv2.imwrite('./results/FFT/decode.png', result, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
        print('[INFO]:Extract Successfully...')


# 文字水印
class word_watermark():
    def __init__(self, data='我想偷偷藏点什么sjsjsjs', img_path=None):
        self.img_path = img_path
        self.data = data

    def _zero_lsb(self, img):
        pixels = list(img.getdata())
        # 将原图像最低位置置为0
        pixels_new = [(r >> 1 << 1, g >> 1 << 1, b >> 1 << 1, t >> 1 << 1) for (r, g, b, t) in pixels]
        img_new = Image.new(img.mode, img.size)
        img_new.putdata(pixels_new)
        return img_new

    # 返回固定长度的二进制码
    def _binary(self, integer):
        print(integer)
        data = "0" * (8 - (len(bin(integer)) - 2)) + bin(integer).replace('0b', '')
        print(data)
        return data

    # 二进制转UTF-8
    def _Binary2String(self, binary):
        index = 0
        string = []
        # 二进制必须去除标志位
        rec = lambda x, i: x[2:8] + (rec(x[8:], i - 1) if i > 1 else '') if x else ''
        fun = lambda x, i: x[i + 1:8] + rec(x[8:], i - 1)
        while index + 1 < len(binary):
            chartype = binary[index:].index('0')
            length = chartype * 8 if chartype else 8
            string.append(chr(int(fun(binary[index:index + length], chartype), 2)))
            index += length
        return ''.join(string)

    # 加水印
    def encode(self):
        if not (self.img_path and self.data):
            print('[Error]:IMAGE FILE OR DATA LOST...')
            return None
        img = Image.open(self.img_path)
        img_zlsb = self._zero_lsb(img)
        data_bin = ''.join(map(self._binary, bytearray(self.data, 'utf-8')))
        if len(data_bin) > len(img.getdata()) * 4:
            print('[Error]:Data too large...')
            return
        encodedPixels = [(r + int(data_bin[index * 4 + 0]),
                          g + int(data_bin[index * 4 + 1]),
                          b + int(data_bin[index * 4 + 2]),
                          t + int(data_bin[index * 4 + 3])) if index * 4 < len(data_bin) else (r, g, b, t) for
                         index, (r, g, b, t) in enumerate(list(img_zlsb.getdata()))]
        encodedImage = Image.new(img.mode, img.size)
        encodedImage.putdata(encodedPixels)
        if not os.path.exists('./results/LSB'):
            os.makedirs('./results/LSB')
        encodedImage.save('./results/LSB/encode.png')
        print('[INFO]:Watermark Successfully...')

    # 解水印
    def decode(self):
        if not (self.img_path):
            print('[Error]:IMAGE FILE OR DATA LOST...')
            return None
        img = Image.open(self.img_path)
        pixels = list(img.getdata())
        binary = ''.join([str(int(r >> 1 << 1 != r)) + str(int(g >> 1 << 1 != g)) + str(int(b >> 1 << 1 != b)) + str(
            int(t >> 1 << 1 != t)) for (r, g, b, t) in pixels])
        location = binary.find('0' * 16)
        endIndex = location + (8 - (location % 8)) if location % 8 != 0 else location
        data = self._Binary2String(binary[0: endIndex])
        print('[INFO]:Extract Successfully...')
        return data


if __name__ == '__main__':
    pic_watermark(img_path='./test.png', wm_path='./vm.png', alpha=15).encode()
    pic_watermark(img_path='./results/FFT/encode.png', origin_path='./test.png').decode()
    # word_watermark(img_path='./test.png').encode()
    # data = word_watermark(img_path='./results/LSB/encode.png').decode()
    # print(data)
