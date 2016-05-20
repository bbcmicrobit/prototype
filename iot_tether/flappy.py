#!/usr/bin/python
#
# Copyright 2016 British Broadcasting Corporation and Contributors(1)
#
# (1) Contributors are listed in the AUTHORS file (please extend AUTHORS,
#     not this header)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pygame,time, sys, random
from iotoy.deviceproxy import serial_io, DeviceProxy


io = serial_io("/dev/ttyACM1", 19200, debug=False)

mb = DeviceProxy(device=io)
mb.introspect_device()


pygame.init()
display = pygame.display.set_mode([800,600])

def gprint(display, x,y, height, *what):
    font = pygame.font.Font(None, height)
    text = " ".join([ str(w) for w in what ])
    drawn_text = font.render(text , True, (255,255,255))
    display.blit(drawn_text, (x,y))
    pygame.display.flip()

def drawFlappy(display, now, x, y):

    pygame.draw.circle(display, (250,250,100), (int(x), int(y)), 30)
    pygame.draw.circle(display, (250,250,250), (int(x)+10, int(y)-10), 5)
    pygame.draw.circle(display, (0,0,0), (int(x)+10, int(y)-10), 2)

    pygame.draw.polygon(display, (150,100,50), [(int(x)+x_, int(y)+y_) for (x_,y_) in [ (30,-5),(30,+5),(40,0) ] ] )

    if int(now*10) % 2:
        pygame.draw.polygon(display, (150,150,100), [(int(x)+x_, int(y)+y_) for (x_,y_) in [ (0,0),(-20,0),(-30,-30) ] ] )
    else:
        pygame.draw.polygon(display, (150,150,100), [(int(x)+x_, int(y)+y_) for (x_,y_) in [ (0,0),(-20,0),(-30,30) ] ] )

def drawPillar(pillar):
    pos, gap, size = pillar
    pygame.draw.rect(display, (200,200,200), (pos,0,30,gap),0)
    pygame.draw.rect(display, (200,200,200), (pos,gap+size,30,600-size-gap),0)


def game():
    pillars = [[500,100,400]]
    x,y = [400, 300]
    speed = 0
    gravity = 0.5
    start_time = time.time()
    score = 0
    c = 0
    last_A = 0
    while True:
        now = time.time() - start_time

        pygame.draw.rect(display, (200,200,250), (0,0,800,600),0)
        pygame.draw.rect(display, (100,200,100), (0,300,800,300),0)

        for pillar in pillars:
            drawPillar(pillar)

        drawFlappy(display, now, x, y)

        newpillars = []
        for pillar in pillars:
            pillar[0] = pillar[0] - 10
            if pillar[0] > -30:
                newpillars.append(pillar)

        c += 1
        if c % 24 == 0:
            newpillars.append( [800, random.randint(0,10)*20, random.randint(0,4)*50+200] )

        pillars = newpillars

        gprint(display, 10, 10, 20, "Time", int(now), "Score:", score)

        pygame.display.flip()  # Make any updates to the display visible

        y = y + speed
        speed = speed + gravity

        if pygame.event.peek():
            for event in pygame.event.get():
              if event.type==pygame.QUIT: sys.exit()
              if event.type==pygame.KEYDOWN:
                 speed = speed - 6
                 if event.key == pygame.K_q:
                     sys.exit()

        if mb.getbutton("A"):
           if time.time() - last_A > 0.05:
               last_A = time.time()+0.1
               speed = speed - 6

        if mb.getbutton("B"):
            gprint(display, 30, 220, 160, "GAME OVER")
            return

        if y >= 570:
            gprint(display, 30, 220, 160, "GAME OVER")
            return
        for pillar in pillars:
            if abs((pillar[0])-(x-30))<30:
                if pillar[1] < y < pillar[1]+pillar[2]-30:
                    score += 1
                else:
                    gprint(display, 30, 220, 160, "GAME OVER")
                    return

        time.sleep(1.0/24)


while True:
    game()
    last_A = 0
    while True:
        if pygame.event.peek():
            event = pygame.event.wait()
            if event.type==pygame.QUIT: sys.exit()
            if event.type==pygame.KEYDOWN:
                break
        if mb.getbutton("A"):
           if time.time() - last_A > 0.05:
               last_A = time.time()+0.05
               break
