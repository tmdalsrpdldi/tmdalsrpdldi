import pygame
#1 게임 초기화
pygame.init()
#2 게임창 옵션 설정 
size = [500,900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)
#3 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
exit = False
    #4 메인이벤트
while not exit :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit = True
    screen.fill(white)
    pygame.display.flip()
pygame.quit()