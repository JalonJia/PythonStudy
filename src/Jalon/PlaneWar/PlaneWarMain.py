## -*- coding:utf-8 -*-

'''
Created on 2018年4月29日
飞机大战学习看看
凑活用吧，虽然有点难受
@author: kkvv1008
'''

import pygame
import time
from pygame.locals import * #引入监控键盘输入的功能

class HeroPlane(object):
    def __init__(self, screen_on):
        self.x = 210
        self.y = 700
        self.screen = screen_on
        self.image = pygame.image.load("./pictures/hero1.png")
        self.bullet_list = []#存储发射出去的子弹对象引用


    def display(self):    
        self.screen.blit(self.image, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move(-20)
            if bullet.is_judge():
                self.bullet_list.remove(bullet)
                
    
    def move_left(self):
        self.x -= 5
         
    def move_right(self):
        self.x += 5
        
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
    """敌机的类"""
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./pictures/enemy0.png")
        self.bullet_list = []#存储发射出去的子弹对象引用
        self.direction = "right"#用来存储飞机默认的显示方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
        
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move(20)
            if bullet.is_judge():
                self.bullet_list.remove(bullet)



    def move(self):
        
        if self.direction=="right":
            self.x += 5
        elif self.direction=="left":
            self.x -= 5

        if self.x>480-50:
            self.direction = "left"
        elif self.x<0:
            self.direction = "right"

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    
class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x+40
        self.y = y-20
        self.screen = screen_temp
        self.image = pygame.image.load("./pictures/bullet.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, delta_y):
        self.y += delta_y
    
    #判断是否超出屏幕，超出屏幕之后删除
    def is_judge(self):
        if self.y<0 or self.y>852:
            return True
        else:
            return False


def key_control(hero_temp):
    #获取事件，比如按键等，固定写法
    for event in pygame.event.get():

        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
            else:
                print(str(event.key))
    
        

def main():
    #1 创建窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)
    
    #2 创建一个背景图片
    backgroud =  pygame.image.load('./pictures/background.png')
    
    #3 创建一个飞机
    hero = HeroPlane(screen)
    
    enemy = EnemyPlane(screen)
    skip_time = 0
    
    #刷新显示
    while True:
        #窗口中放置控件
        screen.blit(backgroud, (0, 0))        
        hero.display()
        enemy.display()
               
        #刷新游戏显示
        pygame.display.update()        
        key_control(hero)
        enemy.move()
        if skip_time == 10:
            enemy.fire()
            skip_time = 0
            
        time.sleep(0.01)
        skip_time += 1
        

print(__name__)


if __name__ == '__main__':
    main()