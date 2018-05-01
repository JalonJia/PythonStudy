## -*- coding:utf-8 -*-

'''
Created on 2018年4月29日
飞机大战学习看看
凑活用吧，虽然有点难受
@author: kkvv1008
'''

import pygame
import time


def main():
    #1 创建窗口
    screen = pygame.display.set_mode((480, 852), 8, 32)
    
    #2 创建一个背景图片
    backgroud =  pygame.image.load('./pictures/background.png')
    
    #3 创建一个飞机图片
    
    #刷新显示
    while True:
        screen.blit(backgroud, (0,0))
        
        pygame.display.update()
        
    


if __name__ == '__main__':
    main()