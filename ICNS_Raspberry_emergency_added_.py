import pymssql
import pygame
import time
import sys
from datetime import datetime 

conn = pymssql.connect(host='*****', user='*****', password='*****', database='INCAL', charset='utf8')
cursor = conn.cursor()

ClassNumber="*****" #큰따옴표 안에 반 번호를 기입하세요(1학년 1반->101)

def Main(): #교실 알림 서비스 실행(조회, 쉬는시간, 점심시간, 종례, 방과 후)
    # 이 코드가 실행되는 동안 긴급 메시지는 일반 메시지로 처리됨
    pygame.init()
    infoObject = pygame.display.Info()
    font = pygame.font.SysFont('malgungothic',150)
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    Background = pygame.image.load('Inchang_icon.png')

    while True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.quit()

        cursor.execute("SELECT TOP(10) * FROM ClassNotis WHERE ClassNotiClass="+ClassNumber+"AND ClassNotiTime LIKE '%'+CONVERT(varchar(20), getDate(), 23)+'%' ORDER BY ClassNotiTime DESC")
        rows = cursor.fetchall()

        for row in rows:
            def line_change(): #알림 길이에 따라 줄바꿈 실행
                raw = row[1]
                if len(raw) > 0:
                    line1 = raw
                    text1 = font.render(line1, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2))
                if len(raw) > 12:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-75))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2+75))
                if len(raw) > 24:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-150))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2+150))
                if len(raw) > 36:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    line4 = raw[36:48]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    text4 = font.render(line4, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-225))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2-75))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2+75))
                    screen.blit(text4, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+225))
                if len(raw) > 48:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    line4 = raw[36:48]
                    line5 = raw[48:60]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    text4 = font.render(line4, True, (0,0,0))
                    text5 = font.render(line5, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-300))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2-150))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2))
                    screen.blit(text4, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+150))
                    screen.blit(text5, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+300))
            line_change()
            pygame.display.flip()
            time.sleep(5)
        break

def Emergency(): #수업시간 실행(긴급 메시지 수신)
    pygame.init()
    infoObject = pygame.display.Info()
    font = pygame.font.SysFont('malgungothic',150)
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    Background = pygame.image.load('Inchang_icon.png')

    while True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.quit()

        cursor.execute("SELECT * FROM ClassNotis WHERE ClassNotiClass="+ClassNumber+"AND ClassNotiTime LIKE '%'+CONVERT(varchar(20), getDate(), 23)+'%' AND ClassNotiEmergency=1 ORDER BY ClassNotiTime DESC")
        rows = cursor.fetchall()
        cursor.execute("UPDATE ClassNotis SET ClassNotiEmergency=0 WHERE ClassNotiClass="+ClassNumber+"AND ClassNotiEmergency=1")
        conn.commit()
        for row in rows:
            def line_change(): #알림 길이에 따라 줄바꿈 실행
                raw = row[1]
                if len(raw) > 0:
                    line1 = raw
                    text1 = font.render(line1, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2))
                if len(raw) > 12:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-75))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2+75))
                if len(raw) > 24:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-150))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2+150))
                if len(raw) > 36:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    line4 = raw[36:48]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    text4 = font.render(line4, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-225))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2-75))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2+75))
                    screen.blit(text4, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+225))
                if len(raw) > 48:
                    line1 = raw[0:12]
                    line2 = raw[12:24]
                    line3 = raw[24:36]
                    line4 = raw[36:48]
                    line5 = raw[48:60]
                    text1 = font.render(line1, True, (0,0,0))
                    text2 = font.render(line2, True, (0,0,0))
                    text3 = font.render(line3, True, (0,0,0))
                    text4 = font.render(line4, True, (0,0,0))
                    text5 = font.render(line5, True, (0,0,0))
                    screen.fill((255, 255, 255))
                    screen.blit(Background, (infoObject.current_w//2-Background.get_width()//2 ,infoObject.current_h//2-Background.get_height()//2))
                    screen.blit(text1, (infoObject.current_w//2-text1.get_width()//2 ,infoObject.current_h//2-text1.get_height()//2-300))
                    screen.blit(text2, (infoObject.current_w//2-text2.get_width()//2 ,infoObject.current_h//2-text2.get_height()//2-150))
                    screen.blit(text3, (infoObject.current_w//2-text3.get_width()//2 ,infoObject.current_h//2-text3.get_height()//2))
                    screen.blit(text4, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+150))
                    screen.blit(text5, (infoObject.current_w//2-text4.get_width()//2 ,infoObject.current_h//2-text4.get_height()//2+300))
            line_change()
            pygame.display.flip()
            time.sleep(5)
        screen.fill((0,0,0))
        pygame.display.flip()
        break

def Off(): #종료(검은화면)
    pygame.init()
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))

    while True:
        for event in pygame.event.get():
            if pygame.QUIT == event.type:
                pygame.quit()
                sys.quit()
        screen.fill((0,0,0))
        pygame.display.flip()
        time.sleep(20)
        break


while True: #시간 계산 및 출력
    Now = datetime.now()
    Time = (Now.hour*100)+Now.minute
    if 730 < Time < 810: #조회
        Main()
    elif 850 < Time < 910: #1교시 쉬는시간
        Main()
    elif 1000 < Time < 1010: #2교시 쉬는시간
        Main()
    elif 1100 < Time < 1110: #3교시 쉬는시간
        Main()
    elif 1200 < Time < 1250: #점심시간
        Main()
    elif 1340 < Time < 1350: #5교시 쉬는시간
        Main()
    elif 1440 < Time < 1450: #6교시 쉬는시간
        Main()
    elif 1540 < Time < 1600: #방과후
        Main()
    elif 1600 < Time < 2359:
        Off()
    else:
        Emergency()
