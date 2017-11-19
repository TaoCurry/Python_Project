#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

"""
__author__ = "Curry"

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


def randomChar():
    ''' 生成随机的英文字符

    :return:
    '''
    return chr(random.randint(65, 90))


def randomcolor():
    ''' 生成随机颜色

    :return:
    '''
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def randomcolor2():
    '''
    
    :return: 
    '''
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240*60

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))

font = ImageFont.truetype(r'C:\Windows\Fonts\Arvo-Regular.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randomcolor())

for r in range(4):
    draw.text((60 * r + 10, 10), randomChar(), font=font, fill=randomcolor2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
