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
def tup_r(tup) :
    temp_list = []
    for a in tup :
        temp_list.append(round(a))
    return tuple(temp_list)
exit = False
    #4 메인이벤트
while not exit :
    clock.tick(60)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            exit = True
    screen.fill(black)
    A = tup_r((0,size[1]*2/3))
    B = tup_r(size[0],A[1])
    C = tup_r((size[0]/6,A[1]))
    D = tup_r((C[0],C[0]))
    E = tup_r((size[0]/2,D[1]))
    pygame.draw.line(screen, white,A,B,3)
    pygame.draw.line(screen, white, C,D,3)
    pygame.draw.line(screen, white, D,E,3)
#4-5 업데이트
    pygame.display.flip()
#4-6 게임종료
pygame.quit()