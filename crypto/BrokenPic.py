#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 打开图片，头部被破坏，根据 Hint 做一张 1366 * 768 的图，加上 BMP 头，得到一张很模糊的图，左上角有个二维码，中间写了一个 key。
# bmp 内的数据变化很规律，可能是块密码，试试 AES，用那个给出的 key 解密一下
# 扫一下二维码就行了

from Crypto.Cipher import AES

def getBMPheader():
    #bmp是LITTLE-ENDIAN（小字节序、低字节序）
    bfType='424d' #文件类型
    bfSize='360c 3000' #文件大小，本题3148800
    bfReserved1='0000' #保留，为0
    bfReserved2='0000' #保留，为0
    bfOffBits='3600 0000' #数据离文件头偏离量
    biSize='2800 0000' #位图信息头的大小
    biWidth='5605 0000' #宽度，本题1366
    biHeight='0003 0000' #高度，本题768
    biPlanes='0100' #颜色平面数，为1
    biBitCount='1800' #比特数/像素，本题24位
    biCompression='0000 0000' #压缩类型，0为不压缩
    biSizeImage='0000 0000' #图像的大小，本题多少无所谓
    biXPelsPerMeter='0000 0000' #水平分辨率，缺省
    biYPelsPerMeter='0000 0000' #垂直分辨率，缺省
    biClrUsed='0000 0000' #使用的颜色索引数，本题多少无所谓
    biClrImportant='0000 0000' #重要的颜色索引数，本题多少无所谓
    bmp_header=bfType+bfSize+bfReserved1+bfReserved2+bfOffBits
    bmp_header+=biSize+biWidth+biHeight+biPlanes+biBitCount+biCompression+biSizeImage
    bmp_header+=biXPelsPerMeter+biYPelsPerMeter+biClrUsed+biClrImportant
    bmp_header=bmp_header.replace(' ','')
    return bmp_header

def foo():
    ciphertext=open('res/brokenpic.bmp','rb').read() #记得有'b'
    key='PHRACK-BROKENPIC'
    obj=AES.new(key,AES.MODE_ECB)
    message=obj.decrypt(ciphertext)
    fsave=open('res/brokenpic.out.bmp','wb') #记得有'b'
    fsave.write(getBMPheader().decode('hex')+message)
    fsave.close()
    pass

if __name__ == '__main__':
    foo()
    print 'ok'