#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

import pygame
import sys
import time
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
    #backgroud =  pygame.image.load(r"C:\Dev\HomeTeach\SourceCode\Jalon\Gobang\pictures\background.png")
    backgroud =  pygame.image.load("./pictures/background.png") #VSCode中以vscode文件为基准/SourceCode/Jalon/Gobang
    

    
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
    
    

    
    #窗口中放置控件
    screen.blit(backgroud, (0, 150))  
            
    #在屏幕上画多边形
    #最后一个参数是边框宽度，如果省略则表示填充
    pygame.draw.polygon(screen, GREEN, ((10,0), (20,20), (30,30), (100, 0), (100, 100), (0, 100)), 10)
    
    #在屏幕上画线
    pygame.draw.line(screen, BLUE, (60, 60), (120, 120), 30)
    
    #在屏幕上画圆
    pygame.draw.circle(screen, RED, (300, 350), 50, 10)
    
    #椭圆
    #元组中传递左上角坐标xy，椭圆的宽和高
    #最后一个参数是线宽，0表示填充
    pygame.draw.ellipse(screen, BLACK, (300, 250, 40, 80), 2)

    
    #矩形
    pygame.draw.rect(screen, BLUE, (200, 250, 100, 80), 2)
    
    #画一个矩形将文字包起来
    pygame.draw.rect(screen, RED, 
                     (text_rect.left -20, text_rect.top - 20, text_rect.width + 40, text_rect.height + 40), 0)

    #将Text的容器放到屏幕中间
    screen.blit(text, text_rect)
    
    #设置某个像素点的颜色
    pix_array = pygame.PixelArray(screen)
    pix_array[400][400] = BLACK
    pix_array[0][0] = BLACK
    pix_array[0][2] = BLACK
    pix_array[0][5] = BLACK    
    del pix_array #设置完之后，必须调用这句话解锁Surface对象，否则不能调用blit方法

    #刷新游戏显示
    pygame.display.update() 
        
        
    while True: #游戏主体
        #监听事件
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                print("exit")
                pygame.quit() 
                sys.exit()     
            elif event.type == MOUSEBUTTONUP:    #鼠标事件            
                print(event) 
                print(event.position())          
            elif event.type == KEYDOWN: #按键
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    

        



if __name__ == '__main__':
    main()

