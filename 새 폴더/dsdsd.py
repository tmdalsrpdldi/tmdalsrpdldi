import pygame
import math
import random

pygame.init()
size = [500, 900]
screen = pygame.display.set_mode(size)
title = "HANGMAN"
pygame.display.set_caption(title)
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
hhint_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 80)
entry_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 60)
no_font = pygame.font.Font("C:/windows/Fonts/arial.ttf", 40)

def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)

entry_text = ""
drop = False
enter_go = False
exitt = False

f = open("voca.txt", "r", encoding='UTF-8')
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
data_list = data_list[:-1]
while True:
    r_index = random.randrange(0, len(data_list))
    word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1]
    if len(word) <= 6:
        break
word = word.upper()

word_show = "_" * len(word)
try_num = 0
ok_list = []
no_list = []

k = 0

while not exitt:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exitt = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if (key_name == "return" or key_name == "enter"):
                if entry_text != "" and (ok_list + no_list).count(entry_text) == 0:
                    enter_go = True
            elif len(key_name) == 1:
                if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                    entry_text = key_name.upper()
                else:
                    entry_text = ""
            else:
                entry_text = ""
    if try_num == 8:
        drop = True
        k += 1
    if enter_go == True:
        ans = entry_text
        result = word.find(ans)
        if result == -1:
            try_num += 1
            no_list.append(ans)
        else:
            ok_list.append(ans)
            for i in range(len(word)):
                if word[i] == ans:
                    word_show = word_show[:i] + ans + word_show[i + 1:]
        enter_go = False
        entry_text = ""
    screen.fill(black)
    A = tup_r((0, size[1] * 2 / 3))
    B = ((size[0], A[1]))
    C = tup_r((size[0] / 6, A[1]))
    D = (C[0], C[0])
    E = tup_r((size[0] / 2, D[1] ))
    pygame.draw.line(screen, white, A, B, 3)
    pygame.draw.line(screen, white, C, D, 3)
    pygame.draw.line(screen, white, D, E, 3)  
    F = tup_r((E[0], E[1] + size[0] / 6))
    if drop == False:
        pygame.draw.line(screen, white, E, F, 3)
    r_head = round(size[0] / 12)
    if drop == True:
        G = (F[0], F[1] + r_head + k * 10)
    else:
        G = (F[0], F[1] + r_head)
    if try_num >= 1:
        pygame.draw.circle(screen, white, G, r_head, 3)
    H = (G[0], G[1] + r_head)
    I = (H[0], H[1] + r_head)
    if try_num >= 2:
        pygame.draw.line(screen, white, H, I, 3)
    l_arm = r_head * 2
    J = (I[0] - l_arm * math.cos(30 * math.pi / 180), (I[1] + l_arm * math.sin(30 * math.pi / 180)))
    K = (I[0] + l_arm * math.sin(30 * math.pi / 180), (I[1] + l_arm * math.cos(30 * math.pi / 180)))
    J = tup_r(J)
    K = tup_r(K)
    if try_num >= 3:
        pygame.draw.line(screen, white, I, J, 3)
    if try_num >= 4:
        pygame.draw.line(screen, white, I, K, 3)
    L = (I[0], I[1] + l_arm)
    if try_num >= 5:
        pygame.draw.line(screen, white, I, L, 3)
    l_leg = round(l_arm * 1.5)
    M = (L[0] - l_leg * math.cos(60 * math.pi / 180), (L[1] + l_leg * math.sin(60 * math.pi / 180)))
    N = (L[0] - l_leg * math.cos(60 * math.pi / 180), (L[1] + l_leg * math.sin(60 * math.pi / 180)))
    M = tup_r(M)    
    N = tup_r(N)
    if try_num >= 6:
        pygame.draw.line(screen, white, L, M, 3)
    if try_num >= 7:
        pygame.draw.line(screen, white, L, N, 3)
    if drop == False and try_num == 8:
        O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2))
        P = (O[0]+K*2, O[1])
        if P[0] > size[0]/2 + size[0]/6 :
            P = tup_r((size[0]/2 + size[0]/6, O[1]))
            drop = True
            K = 0
        pygame.draw.line(screen, red, (E[0], E[1] + size[0] / 3 + k * 10), (E[0] + size[0], E[1] + size[0] / 3 + k * 10), 3)

    hint = hhint_font.render(word_show, True, white)
    hint_size = hint.get_size()
    hint_pos = tup_r((size[0] / 2 - hint_size[0] / 2, size[1] * 5 / 6 - hint_size[1] / 2))
    screen.blit(hint, hint_pos)
    entry = entry_font.render(entry_text, True, black)
    entry_size = entry.get_size()
    entry_pos = tup_r((size[0] / 2 - entry_size[0] / 2, size[1] * 17 / 18 - entry_size[1] / 2))
    entry_bg_size = 80
    pygame.draw.rect(screen, white, tup_r(
        (size[0] / 2 - entry_bg_size / 2, size[1] * 17 / 18 - entry_bg_size / 2, entry_bg_size, entry_bg_size)))
    screen.blit(entry, entry_pos)
    no_text = " ".join(no_list)
    no = no_font.render(no_text, True, red)
    no_pos = tup_r((20, size[1] * 2 / 3 + 20))
    screen.blit(no, no_pos)

    pygame.display.flip()

pygame.quit()
