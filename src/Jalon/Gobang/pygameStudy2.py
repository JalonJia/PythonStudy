#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import pygame
import sys
import time
import random
from pygame.locals import * #引入监控键盘输入的功能


def main():
    #定义使用的颜色
    BLACK = (0, 0, 0) 
    WHITE = (255, 255, 255) 
    RED = (255, 0, 0) 
    GREEN = (0, 255, 0) 
    BLUE = (0, 0, 255)
    
    #初始化
    pygame.init() 

    #1 创建窗口
    screen = pygame.display.set_mode((485, 485+200), 0, 32)
    #填充背景色
    screen.fill(WHITE)
    
    pygame.display.set_caption('快乐五子棋')
    
    #2 创建一个背景图片
    #backgroud = pygame.image.load(r"C:\Dev\HomeTeach\SourceCode\Jalon\Gobang\pictures\background.png")
    backgroud = pygame.image.load("./pictures/background.png") #VSCode中以vscode文件为基准/SourceCode/Jalon/Gobang
    
    #窗口中放置控件
    screen.blit(backgroud, (0, 150))  
    
    '''
    #两种可显示中文的方法
    #basicFont = pygame.font.SysFont('SimHei', 48)
    #指定字体
    basicFont = pygame.font.Font(r'C:\WINDOWS\FONTS\MSYH.ttc', 48)
    
    #定义要显示的字符串，第二个参数是是否抗锯齿，第三个颜色，第四个参数是背景色
    text = basicFont.render(u'游戏说明', True, RED, BLUE)
    
    #获取text的盒子
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery
        
    #画一个矩形将文字包起来
    pygame.draw.rect(screen, RED, 
                     (text_rect.left -20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40), 0)
    
    #将Text的容器放到屏幕中间
    screen.blit(text, text_rect)
    
    
    #定义一个Box
    box1 = {'rect': pygame.Rect(300, 80, 50, 100), 'color': BLUE, 'dir': 'UPRIGHT'}
    pygame.draw.rect(screen, box1['color'], box1['rect'])
    
    '''
    
    #Sound只能用wav
    white_sound = pygame.mixer.Sound(r'./sound/white.wav')
    white_sound.play()
    
    black_sound = pygame.mixer.Sound(r'./sound/black.wav')  
    black_sound.play()
    
    
    
    pygame.mixer.music.load(r'./sound/white.mp3')
    pygame.mixer.music.play(-1, 0) #-1表示循环播放，第二个参数表示从第几秒开始播放
    #pygame.mixer.music.stop()
    
    #黑子
    black_flag = pygame.Rect(200, 200, 40, 40)
    black_flag_image = pygame.image.load('./pictures/black.jpg') 
    #放大缩小精灵大小
    black_flag_image_stretched = pygame.transform.scale(black_flag_image, (40, 40))

    #白子
    white_flag = pygame.Rect(300, 300, 40, 40)
    white_flag_image = pygame.image.load('./pictures/white2.jpg') 
    white_flag_image_stretched = pygame.transform.scale(white_flag_image, (40, 40))

    #放棋子
    screen.blit(black_flag_image_stretched, black_flag)
    screen.blit(white_flag_image_stretched, white_flag)

    main_clock = pygame.time.Clock()
    
    
    
    #检查碰撞：
    #box1.colliderect(box2)
    
    #删除列表中的元素时，要用副本
    #for food in foods[:]: 可以生成一个拷贝
        
        
    while True: #游戏主体
        #监听事件
        for event in pygame.event.get():
            if event.type == QUIT: 
                print("exit")
                pygame.quit() 
                sys.exit()     
            elif event.type == MOUSEBUTTONUP:    #鼠标事件            
                print(event) 
                print(event.pos)
                print(event.button) #button:12345左中右，上滚，下滚
                #print(event.position())        
            elif event.type == MOUSEMOTION: #鼠标滑动
                print(event)
                print(event.buttons) #左中右鼠标是否按下     
            elif event.type == KEYDOWN: #按键
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
            elif event.type == KEYUP: #按键弹起
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('Key UP')
                    
        #刷新游戏显示
        
        
        pygame.display.update() 
        main_clock.tick(40) #所有计算机上都执行每秒钟40次循环

        



if __name__ == '__main__':
    main()

