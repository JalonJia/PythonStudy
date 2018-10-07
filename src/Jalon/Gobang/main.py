import pygame
import sys
import time
from pygame.locals import * #引入监控键盘输入的功能



def main():
    #初始化
    pygame.init() 

    #1 创建窗口
    screen = pygame.display.set_mode((485, 485), 0, 32)
    pygame.display.set_caption('快乐五子棋')
    
    #2 创建一个背景图片
    #backgroud =  pygame.image.load(r"C:\Dev\HomeTeach\SourceCode\Jalon\Gobang\pictures\background.png")
    backgroud =  pygame.image.load("./pictures/background.png") #VSCode中以vscode文件为基准/SourceCode/Jalon/Gobang
    
    #3 创建一个飞机
    #hero = HeroPlane(screen)
    
    #enemy = EnemyPlane(screen)
    #skip_time = 0
    
    #刷新显示
    while True: #游戏主体
        #刷新游戏显示
        pygame.display.update() 

        #窗口中放置控件
        screen.blit(backgroud, (0, 0))        
        #hero.display()
        #enemy.display()
        
        #监听事件
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                print("exit")
                pygame.quit() 
                sys.exit()                 

        #key_control(hero)
        #enemy.move()
        #if skip_time == 10:
            #enemy.fire()
            #skip_time = 0
            
        #time.sleep(0.01)
        #skip_time += 1
        



if __name__ == '__main__':
    main()