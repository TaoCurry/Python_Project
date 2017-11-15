#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）
"""
__author__ = "Curry"

import base64

coupon = {'id': '1231', 'goods': '001'}   # 优惠码由key：id和goods组成，value由迭代产生200个不同的值


def gen_coupon(id, goods):
    '''生成优惠码

    :param id:
    :param goods:
    :return:
    '''
    coupon['id'] = id
    coupon['goods'] = goods
    raw = '/'.join([k + ':' + v for k, v in coupon.items()])    # 使用join方法将key：value组成的list连接成字符串
    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))   # 使用Base64将字符串编码为base64编码格式的字符串，raw_64为byte类型
    c_code = raw_64.decode()    # 将byte类型的raw_64解码为str类型，后续写入txt文件以str写入
    return c_code


def save_coupon(c_code):
    ''' 将base64解码的优惠码写入文本文件中

    :param c_code: 优惠码
    :return:
    '''
    with open('C:/Users/xiatao/Desktop/test.txt', 'a') as file:
        file.write(c_code + '\n')


def show_coupon(c_code):
    print('优惠码：', c_code)


def parse_coupon(c_code):
    print('解析优惠码：', base64.urlsafe_b64decode(c_code.endcode('utf-8')))


def gen_all():
    for i in range(1000, 1200):
        c_code = gen_coupon(str(i), str(int(i // 2)))
        save_coupon(c_code)


if __name__ == '__main__':
    gen_all()
