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

    #设置落子的声音
    white_sound = pygame.mixer.Sound(r'./sound/white.wav')
    white_sound.play()
    
    black_sound = pygame.mixer.Sound(r'./sound/black.wav')  
    black_sound.play()

    #黑子
    black_flag = pygame.Rect(200, 200, 40, 40)
    black_flag_image = pygame.image.load('./pictures/black.jpg') 
    #放大缩小精灵大小
    black_flag_image_stretched = pygame.transform.scale(black_flag_image, (20, 20))

    #白子
    white_flag = pygame.Rect(300, 300, 20, 20)
    white_flag_image = pygame.image.load('./pictures/white2.jpg') 
    white_flag_image_stretched = pygame.transform.scale(white_flag_image, (20, 20))
    
    #放置棋子的红框
    red_box = {'rect': pygame.Rect(300, 80, 20, 20), 'color': RED, 'width': 1}
    
    


    #1 创建窗口
    screen = pygame.display.set_mode((485, 485), 0, 32)
    pygame.display.set_caption('快乐五子棋')
    
    #2 创建一个背景图片
    #backgroud =  pygame.image.load(r"C:\Dev\HomeTeach\SourceCode\Jalon\Gobang\pictures\background.png")
    backgroud =  pygame.image.load("./pictures/background.png") #VSCode中以vscode文件为基准/SourceCode/Jalon/Gobang
    
    white_or_black = 0 #0表示黑棋，1表示白棋
    
    white_flags = []
    black_flags = []
    
    #刷新显示
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
                
                if white_or_black == 0:
                    black_flags.append(red_box['rect'])
                    black_sound.play()
                    
                else:                    
                    white_flags.append(red_box['rect'])
                    white_sound.play()
                    print(f'白棋个数：{len(white_flags)}')
                
                white_or_black = 1 - white_or_black
                
                #print(event.position())        
            elif event.type == MOUSEMOTION: #鼠标滑动
                print(event)
                print(event.buttons) #左中右鼠标是否按下
                red_box['rect'] = (15 + 31*((event.pos[0])//31), 15 + 31*((event.pos[1])//31), 20, 20)
                        
        
        screen.blit(backgroud, (0, 0))
        #print(f'黑棋个数：{len(black_flags)}')
        #print(f'白棋个数：{len(white_flags)}')
        for x in black_flags :
            print(x)
            screen.blit(black_flag_image_stretched, x)
        for x in white_flags :
            print(x)
            screen.blit(white_flag_image_stretched, x)
            
        pygame.draw.rect(screen, red_box['color'], red_box['rect'], red_box['width'])
        
        #刷新游戏显示
        pygame.display.update() 

        



if __name__ == '__main__':
    main()