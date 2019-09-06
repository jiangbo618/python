#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2019/9/5 15:26
# @Author      :Jiangbo Lin
# @Filename    :Snake_food.py 
# @Description :
import pygame,sys,random,time
from pygame.locals import *\
#pygame 初始化
pygame.init()
fpsClock  = pygame.time.Clock()
#初始化窗口
#设置窗口大小
playSurface = pygame.display.set_mode((800,600))
pygame.display.set_caption("贪吃蛇")
#定义颜色
RED = pygame.Color(255,0,0)
GREEN = pygame.Color(0,255,0)
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GREY  = pygame.Color(120,120,120)
LIGHT = pygame.Color(220,220,220)
#定义游戏结束函数
def gameover(playSurface,score):
    #显示游戏结束
    #创建字体的样式以及大小
    gameover_font = pygame.font.SysFont('arial.ttf',72)
    gameover_surf = gameover_font.render('Game Over !', True,GREY)
    #设置文本的位置
    gameover_rect = gameover_surf.get_rect()
    gameover_rect.midtop = (320,125)
    #更新文本的显示
    playSurface.blit(gameover_surf,gameover_rect)
    # 创建分数字体的样式以及大小
    '''
    score_font = pygame.font.SysFont('arial.ttf',48)
    # 创建分数的颜色以及显示内容
    score_surf = score_font.render('SCORE:  '+str(score), True,GREY)
    #设置分数的位置
    score_rect = gameover_surf.get_rect()
    score_rect.midtop = (320,225)
    #更新分数文本的显示
    playSurface.blit(score_surf,score_rect)
    '''
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

def speed_contrl(speed_num):#每得5分速度提升
    if speed_num ==0:
        fpsClock.tick(5)
        pygame.display.flip()
        speed_str = 'Chick'
    elif speed_num ==1:
        fpsClock.tick(10)
        pygame.display.flip()
        speed_str = 'Middle'

    elif speed_num == 2:
        fpsClock.tick(15)
        pygame.display.flip()
        speed_str = 'Fast'

    elif speed_num == 3:
        fpsClock.tick(20)
        pygame.display.flip()
        speed_str = 'High Fast'

    elif speed_num == 4:
        fpsClock.tick(25)
        pygame.display.flip()
        speed_str = 'Monster'
    else:
        fpsClock.tick(30)
        pygame.display.flip()
        speed_str = 'Devil'

    Speed_font = pygame.font.SysFont('arial.ttf', 30)
    # 创建分数的颜色以及显示内容
    Speed_surf = Speed_font.render('Speed:  ' + speed_str, True, RED)

    Speed_rect = Speed_surf.get_rect()
    Speed_rect.midtop = (680,200)
    # 更新分数文本的显示
    playSurface.blit(Speed_surf, Speed_rect)

    score_font = pygame.font.SysFont('arial.ttf', 30)
    # 创建分数的颜色以及显示内容
    score_surf = score_font.render('Score:  ' + str(score), True, WHITE)
    # 设置分数的位置
    score_rect = score_surf.get_rect()
    score_rect.midtop = (660,300)
    # 更新分数文本的显示
    playSurface.blit(score_surf, score_rect)
    pygame.display.flip()
#贪吃蛇的初始化
snakePosition = [100,100]#定义头的位置
#初始化蛇身体，初始身体为3段
snakeSegment = [[100,100],[80,100],[60,100]]
#初始化食物
foodPosition = [300,300]
food_number = 1
#初始化贪吃蛇的运动方向
dir = 'right'
changeDir = dir
#初始化当前的分数
score = 0
speed_num = 0
#********************************************************************************
#********************************************************************************
#游戏循环体的设计
while True:
    speed_contrl(speed_num)
    #从队列中获取事件
    for event in pygame.event.get():
        #窗口关闭事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 窗口关闭事件
        elif event.type == KEYDOWN:
            if event.key ==K_RIGHT:
                changeDir = 'right'
            if event.key == K_LEFT:
                changeDir = 'left'
            if event.key ==K_UP:
                changeDir = 'up'
            if event.key ==K_DOWN:
                changeDir = 'down'
            if event.key == K_ESCAPE:
               pygame.event.post(pygame.event.Event(QUIT))

                
    #限制贪食蛇的输入方向，不能与当前的方向相反
    if changeDir == 'right' and not dir =='left':
        dir = changeDir
    if changeDir == 'up' and not dir =='down':
        dir = changeDir
    if changeDir == 'down' and not dir == 'up':
        dir = changeDir
    if changeDir == 'left' and not dir == 'right':
        dir = changeDir
    #设置移动规则
    if dir == 'right':
        snakePosition[0] += 20
    if dir == 'left':
        snakePosition[0] -= 20
    if dir == 'down':
        snakePosition[1] += 20
    if dir == 'up':
        snakePosition[1] -= 20
    #设置贪吃蛇吃完食物后的身体长度
    snakeSegment.insert(0,list(snakePosition))
    #贪食蛇吃完食物后，食物消失
    if snakePosition[0] == foodPosition[0] and snakePosition[1] == foodPosition[1]:
        food_number = 0
    else:
        snakeSegment.pop()
    if food_number == 0:
        x = random.randint(1,24)
        y =  random.randint(1,24)
        foodPosition = [x*20,y*20]
        food_number = 1
        score +=1
        if score%5 ==0 and score != 0:
            speed_num += 1
    #填充背景
    playSurface.fill(BLACK)
    pygame.draw.rect(playSurface, (0, 0, 255), (600, 0, 600, 600))
    #将贪食蛇的身体和食物 显示出来
    for postion in snakeSegment[1:]:
        #设身为白色
        pygame.draw.rect(playSurface,WHITE,Rect(postion[0],postion[1],20,20))
        #蛇头为灰色
        pygame.draw.rect(playSurface,GREEN,Rect(snakePosition[0],snakePosition[1],20,20))
        #食物为红色
        pygame.draw.rect(playSurface, RED, Rect(foodPosition[0], foodPosition[1], 20, 20))
        #设置游戏速度
        #设置游戏结束场景
        #1.超出边线
        if snakePosition[0]>580 or snakePosition[0] <0:   #X轴
            gameover(playSurface,score)

        if snakePosition[1]>580 or snakePosition[1] <0:  #Y轴
            gameover(playSurface,score)
        #2.头碰到身体
        for snakeBody in snakeSegment[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameover(playSurface, score)












