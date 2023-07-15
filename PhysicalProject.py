import turtle as t
import random
import pyautogui

from Arduino import Arduino
import time
board = Arduino('9600')

#FND 세그먼트 (아두이노)
def segment():
    seg = [6, 7, 8, 9, 10, 11, 12, 13]
    d_0 = ["LOW","LOW","HIGH","HIGH","HIGH","HIGH","HIGH","HIGH"]
    d_1 = ["LOW","LOW","LOW","LOW","LOW","HIGH","HIGH","LOW"]
    d_2 = ["LOW","HIGH","LOW","HIGH","HIGH","LOW","HIGH","HIGH"]
    d_3 = ["LOW","HIGH","LOW","LOW","HIGH","HIGH","HIGH","HIGH"]
    
    board.pinMode(seg[0], "OUTPUT")
    board.pinMode(seg[1], "OUTPUT")
    board.pinMode(seg[2], "OUTPUT")
    board.pinMode(seg[3], "OUTPUT")
    board.pinMode(seg[4], "OUTPUT")
    board.pinMode(seg[5], "OUTPUT")
    board.pinMode(seg[6], "OUTPUT")
    board.pinMode(seg[7], "OUTPUT")

    a = 1
    i = 0
    while i != 8:
            board.digitalWrite(seg[i], d_3[i])
            i += a
    time.sleep(1)
    i = 0
    while i != 8:
            board.digitalWrite(seg[i], d_2[i])
            i += a
    time.sleep(1)
    i = 0
    while i != 8:
            board.digitalWrite(seg[i], d_1[i])
            i += a
    time.sleep(1)
    i = 0
    while i != 8:
            board.digitalWrite(seg[i], d_0[i])
            i += a

#성공 메시지
def message(m1,m2):
    m = t.Turtle()
    m.shape("circle")
    m.penup()
    m.goto(0,100)
    m.write(m1, False,"center",("",40))
    m.goto(0,-100)
    m.write(m2, False,"center",("",20))
    m.goto(0, -600)
       
#배경
t.title("Be careful! Turtle!")
t.setup(450, 600)
t.bgcolor("#cc723d")

#거북이 
t.shape("turtle")
t.color("darkgreen")
t.penup()
t.goto(0, -250)
t.setheading(90)

#장애물
i = 0
a = 1

o = ['s1', 's2', 's3', 's4', 's5',
     's6', 's7', 's8', 's9', 's10',
     't1', 't2', 't3', 't4', 't5',
     't6', 't7', 't8', 't9', 't10']

for obstacle in range (10):
    o[i] = t.Turtle()
    o[i].speed(0)
    o[i].shape("square")
    o[i].color("skyblue")
    o[i].penup()
    x1 = random.randrange(-150, 150, 35)
    y1 = random.randrange(-200, 0, 30)
    o[i].goto(x1,y1)
    i += a
   
for obstacle in range (10):
    o[i] = t.Turtle()
    o[i].speed(0)
    o[i].shape("triangle")
    o[i].color("green")
    o[i].penup()
    o[i].setheading(90)
    x2 = random.randrange(-150, 150, 30)
    y2 = random.randrange(50, 250, 35)
    o[i].goto(x2,y2)
    i += a
       
#깃발
f = t.Turtle()
f.shape("arrow")
f.color("red")
f.penup()
f.goto(0,240)
f.pendown()
f.goto(0, 260)

#재시작
def restart():
    t.clear()
    t.shape("turtle")
    t.color("darkgreen")
    t.penup()
    t.goto(0, -250)
    t.setheading(90)
    play()

#조이스틱 & 스위치 & RGB LED (아두이노)
X = 0
Y = 1

BUTTON = 5
board.pinMode(BUTTON, "INPUT")

RLED = 2
GLED = 3
BLED = 4
board.pinMode(RLED, "OUTPUT")
board.pinMode(GLED, "OUTPUT")
board.pinMode(BLED, "OUTPUT")
   
def play():
    t.forward(10)
    if (t.distance(o[0]) >= 12 and
        t.distance(o[1]) >= 12 and
        t.distance(o[2]) >= 12 and
        t.distance(o[3]) >= 12 and
        t.distance(o[4]) >= 12 and
        t.distance(o[5]) >= 12 and
        t.distance(o[6]) >= 12 and
        t.distance(o[7]) >= 12 and
        t.distance(o[8]) >= 12 and
        t.distance(o[9]) >= 12 and
        t.distance(o[10]) >= 12 and
        t.distance(o[11]) >= 12 and
        t.distance(o[12]) >= 12 and
        t.distance(o[13]) >= 12 and
        t.distance(o[14]) >= 12 and
        t.distance(o[15]) >= 12 and
        t.distance(o[16]) >= 12 and
        t.distance(o[17]) >= 12 and
        t.distance(o[18]) >= 12 and
        t.distance(o[19]) >= 12):
        t.ontimer(play,100)
        
    else:
        board.analogWrite(RLED, 255)
        board.analogWrite(GLED, 30)
        board.analogWrite(BLED, 0)
        
        while True:
            #time.sleep(1)
            if (board.digitalRead(BUTTON) == 1):
                print("HIGH")
                restart()
                board.analogWrite(RLED, 0)  
                board.analogWrite(GLED, 0)
                board.analogWrite(BLED, 0)
                break
       

    if t.distance(f) < 12:
        segment()
        board.analogWrite(RLED, 0)  
        board.analogWrite(GLED, 0)
        board.analogWrite(BLED, 255)
        
        message("!!!Success!!!", "Turn up the thumb^@^")
        
        
play()    
            
def turn_right():
    t.setheading(0)
def turn_up(): 
    t.setheading(90)
def turn_left(): 
    t.setheading(180)
def turn_down(): 
    t.setheading(270)

while True:
    if(board.analogRead(Y) == 0):
        print("Left");
        turn_left()
        pyautogui.press('left')

    elif(board.analogRead(X) == 0):
        print("Up");
        turn_up()
        pyautogui.press('up')
    
    if(board.analogRead(Y) == 1023):
        print("Right");
        turn_right()
        pyautogui.press('right')
        
    
    elif(board.analogRead(X) == 1023):
        print("Down");
        turn_down()
        pyautogui.press('down')


    

 
    
        
