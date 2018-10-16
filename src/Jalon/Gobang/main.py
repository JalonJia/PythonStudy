import pygame
import sys
import time
from pygame.locals import * #引入监控键盘输入的功能

#定义使用的颜色
BLACK = (0, 0, 0) 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
GREEN = (0, 255, 0) 
BLUE = (0, 0, 255)


#判断是否赢了
def is_win(flags):
    l_cnt = len(flags)
    flags.sort()
    #print(flags)
    if l_cnt < 5:
        return False
    
    for i in range(l_cnt):
        if five_flags_inline(flags, i):
            return True
    
    return False
        

def five_flags_inline(flags, index):
    delta_x = 31
    delta_y = 31
    flags_next_four = flags[index+1:index+5]
    if len(flags_next_four) < 4:
        return False
    
    last_x = flags[index][0]
    last_y = flags[index][1]
    
    x_add = 0
    y_add = 0
    
    #赢棋只可能是以下四种情况
    if flags_next_four[0][0] == last_x: #判断向下纵列
        x_add = 0
        y_add = delta_y            
    elif flags_next_four[0][1] == last_y: #判断向右横列
        x_add = delta_x
        y_add = 0         
    elif (flags_next_four[0][0] == last_x + delta_x) and (flags_next_four[0][1] == last_y - delta_y): #判断右上斜线/
        x_add = delta_x
        y_add = -delta_y
    elif (flags_next_four[0][0] == last_x + delta_x) and (flags_next_four[0][1] == last_y + delta_y): #判断右下斜线\
        x_add = delta_x
        y_add = delta_y
    else : #肯定没有赢
        return False
    
    for f in flags_next_four:
        last_x += x_add
        last_y += y_add
        if (last_x != f[0]) or (last_y != f[1]):
            return False
    
    return True
   
            
#判断是否赢了
def show_win(win_msg, screen):
    #指定字体
    basicFont = pygame.font.Font(r'C:\WINDOWS\FONTS\MSYH.ttc', 48)
    
    #定义要显示的字符串，第二个参数是是否抗锯齿，第三个颜色，第四个参数是背景色
    text = basicFont.render(win_msg, True, RED, BLUE)
    
    #获取text的盒子
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery
        
    #画一个矩形将文字包起来
    pygame.draw.rect(screen, RED, 
                     (text_rect.left -10, text_rect.top - 10, text_rect.width + 20, text_rect.height + 20), 0)
    
    #将Text的容器放到屏幕中间
    screen.blit(text, text_rect)
        

def main():
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
    
    b_win = False
    
    #刷新显示
    while True: #游戏主体
      
        #监听事件
        for event in pygame.event.get(): 
            if event.type == QUIT: 
                print("exit")
                pygame.quit() 
                sys.exit()                 
            elif event.type == MOUSEBUTTONUP:    #鼠标事件            
                #print(event) 
                #print(event.pos)
                #print(event.button) #button:12345左中右，上滚，下滚
                if not b_win:                
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
                if not b_win:
#                     print(event)
#                     print(event.buttons) #左中右鼠标是否按下
                    red_box['rect'] = (15 + 31*((event.pos[0])//31), 15 + 31*((event.pos[1])//31), 20, 20)
                                
        screen.blit(backgroud, (0, 0))
        #print(f'黑棋个数：{len(black_flags)}')
        #print(f'白棋个数：{len(white_flags)}')
        for f in black_flags :
            #print(f)
            screen.blit(black_flag_image_stretched, f)
        for f in white_flags :
            #print(f)
            screen.blit(white_flag_image_stretched, f)
        
        if is_win(black_flags):
            b_win = True
            show_win('黑棋胜!', screen)

        if is_win(white_flags):
            b_win = True
            show_win('白棋胜!', screen)
        
        pygame.draw.rect(screen, red_box['color'], red_box['rect'], red_box['width'])
        
        #刷新游戏显示
        pygame.display.update() 

        



if __name__ == '__main__':
    main()