from tkinter import *
from tkinter import ttk
from tkinter import messagebox,ttk
import tkinter as tk
from tkinter import filedialog
import platform
import psutil
import speech_recognition
from turtle import *
from pygame import mixer
from pygame.locals import *
import sqlite3 as sql
import pickle
#brightness
import screen_brightness_control as pct
#audio
from ctypes import cast,POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities,IAudioEndpointVolume
#weather
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
#clock
from time import strftime
import time
import googletrans
import wikipedia
import pyperclip
import pyttsx3

#calender
from tkcalendar import*
#open google
import pyautogui
import subprocess
import webbrowser 
import random
import turtle
import sys
import pygame
from email.message import EmailMessage
import smtplib
import os
import imghdr
import pandas
from difflib import get_close_matches
import json
root=Tk()
root.title("MAC-SOFT TOOL By Dev")
root.geometry("850x500+100+100")
root.resizable(False,False)
root.configure(bg="#292e2e")

#icon
image_icon=PhotoImage(file="image/icon.png")
root.iconphoto(False,image_icon)

body=Frame(root,width=900,height=600,bg="#d6d6d6")
body.pack(padx=20,pady=20)
#--------------------------------------------------------------------------#
lhs=Frame(body,width=310,height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
lhs.place(x=10,y=10)
photo=PhotoImage(file="image/laptop.png")
myimage=Label(lhs,image=photo,background="#f4f5f5")
myimage.place(x=2,y=20)
my_system=platform.uname()
l1=Label(lhs,text=my_system.node,bg="#f4f5f5",font=("Acumin Variable Concept" ,15, "bold"),justify="center")
l1.place(x=20,y=200)

l2=Label(lhs,text=f"Version:{my_system.version}",bg="#f4f5f5",font=("Acumin Variable Concept" ,8),justify="center")
l2.place(x=20,y=225)

l3=Label(lhs,text=f"System:{my_system.system}",bg="#f4f5f5",font=("Acumin Variable Concept" ,15),justify="center")
l3.place(x=20,y=250)

l4=Label(lhs,text=f"Machine:{my_system.machine}",bg="#f4f5f5",font=("Acumin Variable Concept" ,15),justify="center")
l4.place(x=20,y=285)

l5=Label(lhs,text=f"Total RAM Installed:{round(psutil.virtual_memory().total/1000000000,2)} GB",bg="#f4f5f5",font=("Acumin Variable Concept" ,15),justify="center")
l5.place(x=20,y=310)

l6=Label(lhs,text=f"Processor:{my_system.processor}",bg="#f4f5f5",font=("Acumin Variable Concept" ,7,"bold"),justify="center")
l6.place(x=10,y=350)

#--------------------------------------------------------------------------#
rhs=Frame(body,width=470,height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
rhs.place(x=330,y=10)
system=Label(rhs,text="System",font=("Acumin Variable Concept",15),background="#f4f5f5")
system.place(x=10,y=10)

############################ Battery ######################################
def converttime(seconds):
    minutes,seconds=divmod(seconds,60)
    hours,minutes=divmod(minutes,60)
    return"%d:%02d:%02d"%(hours,minutes,seconds)

def none():
    global battery_png,battery_label
    battery=psutil.sensors_battery()
    percent=battery.percent
    time=converttime(battery.secsleft)
    
    lb1.config(text=f"{percent}%")
    lb1_plug.config(text=f'Plug in: {str(battery.power_plugged)}')
    lb1_time.config(text=f'{time} remaining')
    battery_label=Label(rhs,background="#f4f5f5")
    battery_label.place(x=15,y=50)
    
    lb1.after(1000,none)
    if battery.power_plugged==True:
        battery_png=PhotoImage(file="image/charging.png")
        battery_label.config(image=battery_png)
    else:
        battery_png=PhotoImage(file="image/battery.png")
        battery_label.config(image=battery_png)


lb1=Label(rhs,bg="#f4f5f5",font=("Acumin Variable Concept", 40, "bold"))
lb1.place(x=200,y=40)

lb1_plug=Label(rhs,bg="#f4f5f5",font=("Acumin Variable Concept" ,10))
lb1_plug.place(x=20,y=100)

lb1_time=Label(rhs,bg="#f4f5f5",font=("Acumin Variable Concept", 15))
lb1_time.place(x=200,y=100)
none()
###################################################################################


############################Speaker ###########################################
lb1_speaker=Label(rhs,text="Speaker:",font=("arial 10 bold"),bg="#f4f5f5")
lb1_speaker.place(x=10,y=150)
volume_value=tk.DoubleVar()
def get_current_volume_value():
    return'{: .2f}'.format(volume_value.get())
def volume_changed(event):
   device=AudioUtilities.GetSpeakers()
   interface=device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)
   vol=cast(interface, POINTER(IAudioEndpointVolume))
   vol.SetMasterVolumeLevel(-float(get_current_volume_value()),None)
style=ttk.Style()
style.configure("TScale",bg="#f4f5f5")
vol=ttk.Scale(rhs,from_=60,to=0,orient='horizontal',cursor="hand2",command=volume_changed,variable=volume_value)
vol.place(x=90,y=150)
vol.set(10)
##########################################################################


###########################Brightness#######################################
lb1_brightness=Label(rhs,text="Brightness",font=("Arial 10 bold"),background="#f4f5f5")
lb1_brightness.place(x=10,y=190)
current_value=DoubleVar()
def get_current_value():
    return'{: .2f}'.format(current_value.get())
    
def brightness_changed(event):
    pct.set_brightness(get_current_value())
bright=ttk.Scale(rhs,from_=0,to=100,orient='horizontal',cursor="hand2",command=brightness_changed,variable=current_value)
bright.place(x=90,y=190)
bright.set(50)
#########################################################################
def weather():
    app1=Toplevel()
    app1.title("Weather App")
    app1.geometry("850x500+200+100")
    app1.resizable(False,False)
    #icon
    image_icon=PhotoImage(file='image/App1.png')
    app1.iconphoto(False,image_icon)
    def getweather():
        try:
            city=text_field.get()
            geolocator=Nominatim(user_agent="geoapiExercises")
            location=geolocator.geocode(city)
            obj=TimezoneFinder()
            result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
            #print(result)

            home=pytz.timezone(result)
            local_time=datetime.now(home)
            current_time=local_time.strftime("%I:%M %p")
            clock.config(text=current_time)
            name.config(text="CURRENT WEATHER:")

            # Add API Key Weather
            api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7a5218c60230d67529d572c12887acd6&unit=metric&exclude=hourly&lang=en"
            json_data=requests.get(api).json()
            condition =json_data['weather'][0]['main']
            description = json_data['weather'][0]['description']
            temp =int(json_data['main']['temp']-273.15)
            pressure=json_data['main']['pressure']
            humidity=json_data['main']['humidity']
            wind=json_data['wind']['speed']
            

            t.config(text=(temp,"°C"))
            c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

            w.config(text=(wind,"m/s"))
            h.config(text=(humidity,"%"))
            d.config(text=description)
            p.config(text=(pressure,"hPa"))


        except Exception as e:
            messagebox.showerror("Weather App","Invalid Entry!!")
    button_mode=True
    def cu():
        global button_mode
        if button_mode:
            button.config(image=off,bg="#26242f",activebackground="#26242f")
            app1.config(bg="#26242f")
            button_mode=False
        else:
            button.config(image=on,bg="white",activebackground="white")
            app1.config(bg="white")
            button_mode=True



    on=PhotoImage(file="image/light.png")
    off=PhotoImage(file="image/dark.png")
    button=Button(app1,image=on,bd=0,bg="white",activebackground="white",command=cu)
    button.place(x=550,y=200)

   


    #search box
    image_search=PhotoImage(file="image/search.png")
    searchbar_image=Label(app1,image=image_search,background="#f4f5f5")
    searchbar_image.place(x=20,y=20)
    text_field=tk.Entry(app1,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
    text_field.place(x=50,y=40)
    text_field.focus()
    image_search_icon=PhotoImage(file="image/search_icon.png")
    search_icon=Button(app1,image=image_search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getweather)
    search_icon.place(x=400,y=34)

    image_logo=PhotoImage(file="image/logo.png")
    weather_logo=Label(app1,image=image_logo,background="#f4f5f5")
    weather_logo.place(x=150,y=100)

    image_box=PhotoImage(file="image/box.png")
    information_box=Label(app1,image=image_box,bg="#f4f5f5")
    information_box.pack(padx=5,pady=5,side=BOTTOM)

    #Time
    name=Label(app1,font=("arial",15,"bold"),bg="#f4f5f5")
    name.place(x=30,y=100)
    clock=Label(app1,font=("Merriweather",20),bg="#f4f5f5")
    clock.place(x=30,y=130)
    label1=Label(app1,text="WIND",font=("Merriweather",15,"bold"),fg="White",bg="#1ab5ef")
    label1.place(x=120,y=400)

    label2=Label(app1,text="HUMIDITY",font=("Merriweather",15,"bold"),fg="White",bg="#1ab5ef")
    label2.place(x=250,y=400)

    label3=Label(app1,text="DESCRIPTION",font=("Merriweather",15,"bold"),fg="White",bg="#1ab5ef")
    label3.place(x=430,y=400)

    label4=Label(app1,text="PRESSURE",font=("Merriweather",15,"bold"),fg="White",bg="#1ab5ef")
    label4.place(x=650,y=400)

    t=Label(app1,font=("arial",50,"bold"),fg="#ee666d",bg="#f4f5f5")
    t.place(x=400,y=150)
    c=Label(app1,font=("arial",25,"bold"),bg="white")
    c.place(x=400,y=250)

    w=Label(app1,text="...",font=("arial",20,"bold"),bg="#f4f5f5")
    w.place(x=120,y=430)
    h=Label(app1,text="...",font=("arial",20,"bold"),bg="#f4f5f5")
    h.place(x=280,y=430)
    d=Label(app1,text="...",font=("arial",20,"bold"),bg="#f4f5f5")
    d.place(x=450,y=430)
    p=Label(app1,text="...",font=("arial",20,"bold"),bg="#f4f5f5")
    p.place(x=655,y=430)

    app1.mainloop()
#################################Clock####################################
def clock():
    
    
    
    time.time()
    t=Turtle()
    wn=Screen()
    
    wn.title("analog clock ")
    wn.bgcolor("black")
    wn.setup(850,600)
    t.speed(1)
    t.pensize(4)
    t.hideturtle()
    wn.tracer(0)

    def draw_clock(h,m,s,t):
        t.penup()
        t.goto(0,210)
        t.setheading(180)
        t.pencolor("grey")
        t.pendown()
        t.circle(210)
        # draw the clock marking for hand hours
        t.penup()
        t.goto(0,0)
        t.pencolor("violet")
        t.setheading(90)
        for _ in range(12):
            t.forward(190)
            t.pendown()
            t.fd(20)
            t.penup()
            t.goto(0,0)
            t.right(30)
        # draw the clock marking for minute and seconds hours
        t.penup()
        t.goto(0,0)
        t.setheading(90)
        for _ in range(60):
            t.forward(200)
            t.pendown()
            t.fd(10)
            t.penup()
            t.goto(0,0)
            t.right(6)
        # draw no on clock face
        #one
        t.penup()
        t.pencolor("yellow")
        t.goto(0,0)
        t.setheading(60)
        t.fd(145)
        t.setheading(0)
        t.fd(15)
        t.write(1,move=False,align="center",font=("arial",25,"normal"))
        
        #two
        t.penup()
        t.goto(0,0)
        t.setheading(30)
        t.fd(135)
        t.setheading(0)
        t.fd(35)
        t.write(2,move=False,align="center",font=("arial",25,"normal"))
        #three
        t.penup()
        t.goto(0,0)
        t.setheading(352)
        t.fd(150)
        t.setheading(0)
        t.fd(25)
        t.write(3,move=False,align="center",font=("arial",25,"normal"))
        #four
        t.penup()
        t.goto(0,0)
        t.setheading(315)
        t.fd(150)
        t.setheading(0)
        t.fd(45)
        t.write(4,move=False,align="center",font=("arial",25,"normal"))
        #five
        t.penup()
        t.goto(0,0)
        t.setheading(290)
        t.fd(178)
        t.setheading(0)
        t.fd(25)
        t.write(5,move=False,align="center",font=("arial",25,"normal"))
        #six
        t.penup()
        t.goto(0,0)
        t.setheading(270)
        t.fd(190)
        t.write(6,move=False,align="center",font=("arial",25,"normal"))
        #seven
        t.penup()
        t.goto(0,0)
        t.setheading(258)
        t.fd(170)
        t.setheading(180)
        t.fd(48)
        t.write(7,move=False,align="center",font=("arial",25,"normal"))
        #eight
        t.penup()
        t.goto(0,0)
        t.setheading(228)
        t.fd(150)
        t.setheading(180)
        t.fd(45)
        t.write(8,move=False,align="center",font=("arial",25,"normal"))
        #nine
        t.penup()
        t.goto(0,0)
        t.setheading(188)
        t.fd(150)
        t.setheading(180)
        t.fd(25)
        t.write(9,move=False,align="center",font=("arial",25,"normal"))
        #ten
        t.penup()
        t.goto(0,0)
        t.setheading(150)
        t.fd(135)
        t.setheading(180)
        t.fd(25)
        t.write(10,move=False,align="center",font=("arial",25,"normal"))
        #eleven
        t.penup()
        t.goto(0,0)
        t.setheading(120)
        t.fd(145)
        t.setheading(180)
        t.fd(15)
        t.write(11,move=False,align="center",font=("arial",25,"normal"))
        #twelve
        t.penup()
        t.goto(0,0)
        t.setheading(90)
        t.fd(150)
        t.write(12,move=False,align="center",font=("arial",25,"normal"))
        #draw hour hand
        t.pu()
        t.goto(0,0)
        t.pencolor("red")
        t.setheading(90)
        angle=(h/12)*360
        t.rt(angle)
        t.pendown()
        t.fd(80)
        #draw minute hand
        t.pu()
        t.goto(0,0)
        t.pencolor("blue")
        t.setheading(90)
        angle=(m/60)*360
        t.rt(angle)
        t.pendown()
        t.fd(120)
        #draw second hand
        t.pu()
        t.goto(0,0)
        t.pencolor("green")
        t.setheading(90)
        angle=(s/60)*360
        t.rt(angle)
        t.pendown()
        t.fd(160)
        #design by
        t.penup()
        t.goto(0,0)
        t.pencolor("gold")
        t.setheading(268)
        t.fd(125)
        t.setheading(0)
        t.fd(5)
        t.write("Mac",move=False,align="center",font=("arial",15,"bold"))
    while True:
        h=int(time.strftime("%I"))
        m= int(time.strftime("%M"))
        s= int(time.strftime("%S"))
        draw_clock(h,m,s,t)
        wn.update()
        time.sleep(1)
        t.clear()
    mainloop()  

#########################################################################



######################Date##############################################
def date():
    roott=Toplevel()
    roott.geometry("300x300+-10+10")
    roott.title("Calender ")
    roott.resizable(0,0)
    roott.configure(bg="lightblue")
    #icon
    image_icon=PhotoImage(file="image/App3.png")
    roott.iconphoto(False,image_icon)
    
    


    mycal=Calendar(roott,setmode="day",day_pattern='d/m/yy')
    mycal.pack(padx=15,pady=35)
    roott.mainloop()

############################################################################



#######################Mode###################################################  
button_mode=True
def mode():
    global button_mode
    if button_mode:
        lhs.config(bg="#292e2e")
        myimage.config(bg="#292e2e")
        l1.config(bg="#292e2e",fg="#d6d6d6")
        l2.config(bg="#292e2e",fg="#d6d6d6")
        l3.config(bg="#292e2e",fg="#d6d6d6")
        l4.config(bg="#292e2e",fg="#d6d6d6")
        l5.config(bg="#292e2e",fg="#d6d6d6")
        l6.config(bg="#292e2e",fg="#d6d6d6")

        
        rhb.config(background="#292e2e")
        app1.config(bg="#292e2e")
        app2.config(bg="#292e2e")
        app3.config(bg="#292e2e")
        app4.config(bg="#292e2e")
        app5.config(bg="#292e2e")
        app6.config(bg="#292e2e")
        app7.config(bg="#292e2e")
        app8.config(bg="#292e2e")
        app9.config(bg="#292e2e")
        app10.config(bg="#292e2e")
        apps.config(bg="#292e2e",fg="#d6d6d6")
        rhs.config(bg="#292e2e")
        system.config(bg="#292e2e",fg="#d6d6d6")
        lb1.config(bg="#292e2e",fg="#d6d6d6")
        lb1_plug.config(bg="#292e2e",fg="#d6d6d6")
        lb1_time.config(bg="#292e2e",fg="#d6d6d6")
        lb1_speaker.config(bg="#292e2e",fg="#d6d6d6")
        lb1_brightness.config(bg="#292e2e",fg="#d6d6d6")
       
        button_mode=False
    else:
        lhs.config(bg="#f4f5f5")
        myimage.config(bg="#f4f5f5")
        l1.config(bg="#f4f5f5",fg="#292e2e")
        l2.config(bg="#f4f5f5",fg="#292e2e")
        l3.config(bg="#f4f5f5",fg="#292e2e")
        l4.config(bg="#f4f5f5",fg="#292e2e")
        l5.config(bg="#f4f5f5",fg="#292e2e")
        l6.config(bg="#f4f5f5",fg="#292e2e")

        
        rhb.config(background="#f4f5f5")
        app1.config(bg="#f4f5f5")
        app2.config(bg="#f4f5f5")
        app3.config(bg="#f4f5f5")
        app4.config(bg="#f4f5f5")
        app5.config(bg="#f4f5f5")
        app6.config(bg="#f4f5f5")
        app7.config(bg="#f4f5f5")
        app8.config(bg="#f4f5f5")
        app9.config(bg="#f4f5f5")
        app10.config(bg="#f4f5f5")
        apps.config(bg="#f4f5f5",fg="#292e2e")
        rhs.config(bg="#f4f5f5")
        system.config(fg="#292e2e",bg="#f4f5f5")
        lb1.config(fg="#292e2e",bg="#f4f5f5")
        lb1_plug.config(fg="#292e2e",bg="#f4f5f5")
        lb1_time.config(fg="#292e2e",bg="#f4f5f5")
        lb1_speaker.config(fg="#292e2e",bg="#f4f5f5")
        lb1_brightness.config(fg="#292e2e",bg="#f4f5f5")
      
        button_mode=True
###############################################################################


################################ Game ##################################

def game():
    
    pygame.init()

    dis_Width = 600
    dis_height = 600
    gray = (0, 100, 0)
    black = (0, 255, 255)
    red = (240, 0, 0)
    green = (240,0,0)
    bright_red = (255,0,0)
    bright_green = (240,255,255)
    bright_blue = (0,0,255)
    blue = (0,0, 200)

    #create a window & Caption
    pygame.mixer.music.load("daku.mp3")
    g_display = pygame.display.set_mode((dis_Width, dis_height))
    pygame.display.set_caption("RACEO GAME")
    clock = pygame.time.Clock()
    carimg = pygame.image.load('car4.png')
    pygame.display.update()

    #create the background of the game
    backgroundimg = pygame.image.load("background.png")
    carimg_small = pygame.transform.scale(carimg, (50, 100))
    intro_background = pygame.image.load("background2.jpg")
    intro_background_sl = pygame.transform.scale(intro_background, (600,600))
    instruction_background = pygame.image.load("background3.jpg")
    instruction_background_sl=pygame.transform.scale(instruction_background, (600, 600))
    car_width = 50
    pause=False

    def intro_loop():
        intro=True
        while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    #quit()
                    #sys.exit()
            g_display.blit(intro_background_sl,(0,0))
            largetext = pygame.font.Font('freesansbold.ttf', 80)
            TextSurf, TextRect = text_object(" RACEO CAR ", largetext)
            TextRect.center = ((280, 50))
            g_display.blit(TextSurf,TextRect)
            button("START",80,500,100,50,green,bright_green,"play")
            button("QUIT",200,500,100,50,red,bright_red,"quit")
            button("INSTRUCTION",320,500,200,50,blue,bright_blue,"intro")
            pygame.display.update()
            clock.tick(100)

    def button(msg,x,y,w,h,ic,ac,action=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(g_display,ac,(x,y,w,h))
            if click[0]==1 and action!=None:
                if action=="play":
                    countdown()
                elif action=="quit":
                    pygame.quit()
                    #quit()
                    #sys.exit()
                elif action=="intro":
                    introduction()
                elif action=="menu":
                    intro_loop()
                elif action=="pause":
                    paused()
                elif action=="unpause":
                    unpaused()


        else:
            pygame.draw.rect(g_display,ic,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textsurf,textrect= text_object(msg,smalltext)
        textrect.center=((x+(w/2)),(y+(h/2)))
        g_display.blit(textsurf,textrect)


    def introduction():
        introduction = True
        while introduction:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    #quit()
                    #sys.exit()
            g_display.blit(intro_background_sl,(0,0))
            largetext= pygame.font.Font('freesansbold.ttf',60)

            smalltext= pygame.font.Font('freesansbold.ttf',18)
            mediumtext= pygame.font.Font('freesansbold.ttf',40)
            textsurf,textrect= text_object("This is an car game in which you need judge the coming cars",smalltext)
            textrect.center=((300),(180))
            TextSurf,TextRect = text_object("INSTRUCTION",largetext)
            TextRect.center=((320),(90))
            g_display.blit(TextSurf,TextRect)
            g_display.blit(textsurf,textrect)
            stextSurf,stextRect= text_object("ARROW LEFT : LEFT TURN",smalltext)
            stextRect=((85),(430))
            hTextSurf,hTextRect= text_object("ARROW RIGHT : RIGHT TURN",smalltext)
            hTextRect.center=((220),(480))
            atextSurf,atextRect = text_object("A : ACCELERATION",smalltext)
            atextRect.center= ((180),(520))
            rtexrSurf,rtextRect = text_object("B :BREAK",smalltext)
            rtextRect.center = ((140),(560))
            ptextSurf,ptextRect = text_object("CLICK ON PAUSE BUTTON : PAUSE", smalltext)
            ptextRect.center= ((240),(390))
            sTextSurf,sTextRect = text_object("CONTROLS",mediumtext)
            sTextRect.center = ((300),(270))

            g_display.blit(stextSurf,stextRect)
            g_display.blit(hTextSurf,hTextRect)
            g_display.blit(TextSurf,TextRect)
            g_display.blit(textsurf,textrect)
            g_display.blit(sTextSurf,sTextRect)
            g_display.blit(ptextSurf,ptextRect)
            g_display.blit(rtexrSurf,rtextRect)
            g_display.blit(atextSurf,atextRect)


            button("BACK",480,500,100,50,blue,bright_blue,"menu")
            pygame.display.update()
            clock.tick(30)


    def paused():
        global pause
        pygame.mixer_music.stop()

        while pause:


                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        #quit()
                        #sys.exit()
                g_display.blit(instruction_background_sl,(0,0))
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_object("PAUSED",largetext)
                TextRect.center=((dis_Width/2),(dis_height/2))
                g_display.blit(TextSurf,TextRect)
                button("CONTINUE",30,450,150,50,green,bright_green,"unpause")
                button("RESTART",200,450,150,50,blue,bright_blue,"play")
                button("MAIN MENU",370,450,200,50,red,bright_red,"menu")
                pygame.display.update()
                clock.tick(30)


    def unpaused():
        global pause
        pause=False
        if pause==False:
            pygame.mixer.music.play(-1)


    def countdown_background():
        font= pygame.font.SysFont(None,25)
        x = (dis_Width * 0.6)
        y = (dis_height * 0.93)
        g_display.blit(backgroundimg, (0,0))
        g_display.blit(carimg_small, (x, y))
        text = font.render("DODGED: 0", True, black)
        score = font.render("SCORE: 0", True, red)
        g_display.blit(text, (0, 50))
        g_display.blit(score, (0, 30))
        button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")

    def countdown():

        countdown=True

        while countdown:
               
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        #quit()
                        #sys.exit()
                g_display.fill(gray)
                countdown_background()
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_object("3",largetext)
                TextRect.center=((dis_Width/2),(dis_height/2))
                g_display.blit(TextSurf,TextRect)
                pygame.display.update()
                clock.tick(1)
                g_display.fill(gray)
                countdown_background()
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_object("2",largetext)
                TextRect.center=((dis_Width/2),(dis_height/2))
                g_display.blit(TextSurf,TextRect)
                pygame.display.update()
                clock.tick(1)
                g_display.fill(gray)
                countdown_background()
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_object("1",largetext)
                TextRect.center=((dis_Width/2),(dis_height/2))
                g_display.blit(TextSurf,TextRect)
                pygame.display.update()
                clock.tick(1)
                g_display.fill(gray)
                countdown_background()
                largetext=pygame.font.Font('freesansbold.ttf',115)
                TextSurf,TextRect=text_object("GO!!!",largetext)
                TextRect.center=((dis_Width/2),(dis_height/2))
                g_display.blit(TextSurf,TextRect)
                pygame.display.update()
                clock.tick(1)
                game_loop()


    #import all the obstracle
    def obstracle(obs_startx,obs_starty,obs):
        if obs ==0:
            obs_pic = pygame.image.load("car0.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        elif obs ==1:
            obs_pic = pygame.image.load("car2.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        elif obs ==2:
            obs_pic = pygame.image.load("car3.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        elif obs ==3:
            obs_pic = pygame.image.load("car5.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        elif obs ==5:
            obs_pic = pygame.image.load("bike.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        elif obs == 6:
            obs_pic = pygame.image.load("racecar.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))
        else:
            obs_pic = pygame.image.load("car.png")
            obs_pic_sl = pygame.transform.scale(obs_pic, (50, 100))



        g_display.blit(obs_pic_sl, (obs_startx, obs_starty))


    #Show score of the our Game
    def score_system(passed, score):
        font = pygame.font.SysFont(None, 55)
        text = font.render("passed" +str(passed),True,black)
        score = font.render("score" +str(score),True,red)
        # text = font.render("Score : " + str(count), True, black)
        # g_display.blit(text, (0, 0)

        g_display.blit(text, (0,50))
        g_display.blit(score, (0,30))






    def text_object(text,font):
        textsurface = font.render(text, True, black)
        return textsurface,textsurface.get_rect()


    def message_display(text):
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        textsurf,textrect = text_object(text, largetext)
        textrect.center = ((dis_Width/2), (dis_height/2))
        g_display.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(3)
        game_loop()


    def crash():
        
        pygame.mixer_music.stop()
        message_display("YOU CRASHED")
        
        


    def background():
        g_display.blit(backgroundimg, (0, 0))

    def car(x, y):
        g_display.blit(carimg_small, (x, y))


    # def highscore(count):
    # 	font = pygame.font.SysFont(None,20)
    # 	)

    def game_loop():
        global pause
        pygame.mixer.music.play(-1)
        x = (dis_Width*0.5)
        y = (dis_height*0.83)
        x_change = 0
        obstracle_speed = 9
        obs=0
        y_change = 0
        obs_startx= random.randrange(200, dis_Width)
        obs_starty=-575
        obs_width=50
        obs_height=100
        passed=0
        level=0
        score=0
        ax_y=15
        FPS=120


        bumped = False
        while not bumped:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   pygame.quit()
                   quit()


               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_LEFT:
                       x_change = -5
                   if event.key == pygame.K_RIGHT:
                       x_change = 5
                   if event.key == pygame.K_a:
                       obstracle_speed += 2
                   if event.key == pygame.K_b:
                       obstracle_speed -= 2
               if event.type == pygame.KEYUP:
                   if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                       x_change = 0

            x+=x_change
            pause=True
            g_display.fill(gray)


            rel_y=ax_y%backgroundimg.get_rect().width
            g_display.blit(backgroundimg, (0, rel_y - backgroundimg.get_rect().width))
            g_display.blit(backgroundimg, (600, rel_y - backgroundimg.get_rect().width))
            if rel_y<600:
                g_display.blit(backgroundimg, (0, rel_y))
                g_display.blit(backgroundimg, (600, rel_y))

            ax_y+=obstracle_speed


            obs_starty-=(obstracle_speed/4)
            obstracle(obs_startx,obs_starty,obs)
            obs_starty+=obstracle_speed
            car(x, y)
            score_system(passed, score)


            if x>600-car_width or x<10:
                crash()

            if obs_starty > dis_height:
                obs_starty = 0 - obs_height
                obs_startx = random.randrange(0, dis_Width)
                obs=random.randrange(0, 8)
                passed=passed+1
                score = score+1
                score=score+49
                if int(passed)%10 == 0:
                    level=level+1
                    obstracle_speed+2
                    largetext = pygame.font.Font("freesansbold.ttf", 80)
                    textsurf, textrect = text_object("LEVEL"+str(level),largetext)
                    textrect.center = ((dis_Width / 2), (dis_height / 2))
                    g_display.blit(textsurf, textrect)
                    pygame.display.update()
                    time.sleep(3)

            if y < obs_starty+obs_height:
                if x > obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x +car_width <obs_startx+obs_width:
                    crash()
            button("Pause",470,0,150,50,blue,bright_blue,"pause")
            pygame.display.update()
            clock.tick(50)

    intro_loop()
    game_loop()
    #pygame.quit()
    #quit()

 






#########################################################################################
def scr():
    root.iconify()
    my=pyautogui.screenshot()
    file_path=filedialog.asksaveasfilename(defaultextension=".png")
    my.save(file_path)
    



##########################################Screenshot###########################
def screenshot():
    
    engine=pyttsx3.init()

    def speak():
        
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(textarea.get(1.0,END))
        engine.runAndWait()
    def speaking():
        mixer.init()
        mixer.music.load("wiki/music2.mp3")
        mixer.music.play()
        sr=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as m:
            try:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                text=sr.recognize_google(audio)
                my_entry.insert(END,text+'.')

            except:
                pass
        
        

    def search():
        question=my_entry.get()
        language = combobox.get()

        for key, value in lang_dict.items():
            if language == value:
                wikipedia.set_lang(key)

        page=wikipedia.page(question)

        textarea.config(state=NORMAL)
        textarea.insert(END, page.content)
        textarea.config(state=DISABLED)

    def edit():
        textarea.config(state=NORMAL)

    def copy():
        content = textarea.get(0.0, END)
        pyperclip.copy(content)

    def clear():
        textarea.config(state=NORMAL)
        textarea.delete(0.0, END)
        textarea.config(state=DISABLED)

        my_entry.delete(0, END)

        combobox.set('Select Language')


    lang_dict = googletrans.LANGUAGES


    app6=Toplevel()

    app6.geometry('700x670+0+0')

    app6.title('My Wikipedia ')

    app6.config(bg='red4')

    my_label_frame = LabelFrame(app6, text="Search Wikipedia", font=('arial', 20, 'bold'), bg='brown3', fg='white')
    my_label_frame.pack(pady=10, padx=10)

    my_entry = Entry(my_label_frame, font=("Helvetica", 18), width=40)
    my_entry.pack(pady=10, padx=20)
    micimage = PhotoImage(file="wiki/mic2.png")
    m=Button(my_entry , image=micimage , font=("Helvetica", 20, 'bold'),cursor="hand2", fg="white", bg='red4',command=speaking)
    m.place(x=490)


    combobox = ttk.Combobox(my_label_frame, font=('times new roman', 18, 'bold'), justify=CENTER, width=15,
                            state='readonly')
    combobox.pack()

    combobox['values']=[e for e in lang_dict.values()]

    combobox.set('Select Language')

    search_button = Button(my_label_frame, text="SEARCH", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',
                        command=search)
    search_button.pack(padx=20, pady=10)

    my_frame = Frame(my_label_frame)
    my_frame.pack(pady=5)

    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    textarea = Text(my_frame, yscrollcommand=text_scroll.set, wrap='word', font=("Helvetica", 20), height=12
                    , bg='red4', fg='white', state=DISABLED)
    textarea.pack()

    buttonFrame = Frame(my_label_frame, bg='brown3')
    buttonFrame.pack()

    edit_button = Button(buttonFrame, text="EDIT", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                        ,command=edit)
    edit_button.grid(row=0, column=0, padx=20)

    copy_button = Button(buttonFrame, text="COPY", font=("Helvetica", 20, 'bold'), fg="white", bg='red4'
                        ,command=copy)
    copy_button.grid(row=0, column=1, padx=20)

    clear_button = Button(buttonFrame, text="CLEAR", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',command=clear)
    clear_button.grid(row=0, column=2, padx=20)
    speak=Button(buttonFrame, text="speak", font=("Helvetica", 20, 'bold'), fg="white", bg='red4',command=speak)
    speak.grid(row=0, column=3, padx=20)



    app6.mainloop()
    

    

##################################################################################



###############################File#############################################




def file():
    subprocess.Popen(r'explorer /select,"C:\path\of\folder\file"')

            
        
#####################################################################################




#####################################Dictionary##################################
def dic():

    engine=pyttsx3.init()

    def wordaudio():
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(enterwordentry.get())
        engine.runAndWait()


    def  meaningaudio():
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(textarea.get(1.0,END))
        engine.runAndWait()


    def iexit():
        voices = engine.getProperty('voices')
        engine.say('Confirm, Do you want to exit?')
        engine.setProperty('voice', voices[0].id)
        engine.runAndWait()

        
        res = messagebox.askyesno('Confirm', 'Do you want to exit?')
        if res == True:
            app44.destroy()

        else:
            pass


    def clear():
        textarea.config(state=NORMAL)
        enterwordentry.delete(0, END)
        textarea.delete(1.0, END)
        textarea.config(state=DISABLED)


    def search():
        data = json.load(open('dict/data.json'))
        word = enterwordentry.get()

        word = word.lower()

        if word in data:
            meaning = data[word]

            textarea.config(state=NORMAL)
            textarea.delete(1.0, END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')

            textarea.config(state=DISABLED)

        elif len(get_close_matches(word, data.keys())) > 0:

            close_match = get_close_matches(word, data.keys())[0]

            res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')

            if res == True:

                meaning = data[close_match]
                textarea.delete(1.0, END)
                textarea.config(state=NORMAL)
                for item in meaning:
                    textarea.insert(END, u'\u2022' + item + '\n\n')

                textarea.config(state=DISABLED)

            else:
                textarea.delete(1.0, END)
                messagebox.showinfo('Information', 'Please type a correct word')
                enterwordentry.delete(0, END)

        else:
            messagebox.showerror('Error', 'The word doesnt exist.Please double check it.')
            enterwordentry.delete(0, END)


    app44 = Toplevel()
    app44.geometry('1000x626+00+0')
    app44.title('Talking Dictionary ')

    app44.resizable(0, 0)

    bgimage = PhotoImage(file="dict/bg .png")

    bgLabel = Label(app44, image=bgimage)
    bgLabel.place(x=0, y=0)

    enterwordLabel = Label(app44, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
    enterwordLabel.place(x=530, y=20)

    enterwordentry = Entry(app44, font=('arial', 23, 'bold'), bd=8, relief=GROOVE, justify=CENTER)
    enterwordentry.place(x=510, y=80)

    enterwordentry.focus_set()

    searchimage = PhotoImage(file='dict/search.png')
    searchButton = Button(app44, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                        command=search)
    searchButton.place(x=620, y=150)

    micimage = PhotoImage(file='dict/speak.png')
    micButton = Button(app44, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                    cursor='hand2',command=wordaudio)
    micButton.place(x=710, y=153)

    meaninglabel = Label(app44, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
    meaninglabel.place(x=580, y=240)

    textarea = Text(app44, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=GROOVE, wrap='word')
    textarea.place(x=460, y=300)

    audioimage = PhotoImage(file="dict/sp.png")
    audioButton = Button(app44, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                        cursor='hand2',command=meaningaudio)
    audioButton.place(x=530, y=555)

    clearimage = PhotoImage(file='dict/clear.png')
    clearButton = Button(app44, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2'
                        , command=clear)
    clearButton.place(x=660, y=555)

    exitimage = PhotoImage(file="dict/exit .png")
    exitButton = Button(app44, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                        command=iexit)
    exitButton.place(x=790, y=555)



    app44.mainloop()




################################################################################
##################################Search########################################
def search():
    mixer.init()

    def search():
        if questionField.get()!='':
            if temp.get()=='google':
                webbrowser.open(f'https://www.google.com/search?q={questionField.get()}')

            if temp.get()=='duck':
                webbrowser.open(f'https://duckduckgo.com/?q={questionField.get()}')

            if temp.get()=='amazon':
                webbrowser.open(f'https://www.amazon.com/s?k={questionField.get()}&ref=nb_sb_noss')

            if temp.get() == 'youtube':
                webbrowser.open(f'http://youtube.com/results?search_query={questionField.get()}')

        else:
            messagebox.showerror('Error','There is nothing to be searched')


    def voice():
        mixer.music.load('music1.mp3')
        mixer.music.play()
        sr=speech_recognition.Recognizer()
        with speech_recognition.Microphone()as m:
            try:
                sr.adjust_for_ambient_noise(m, duration=0.2)
                audio=sr.listen(m)
                message = sr.recognize_google(audio)
                mixer.music.load('music2.mp3')
                mixer.music.play()
                questionField.delete(0,END)
                questionField.insert(0,message)
                search()



            except:
                pass




    app8=Toplevel()

    app8.geometry('660x70+00+00')
    app8.title('Universal Search Bar ')
    app8.iconbitmap('icon.ico')
    app8.config(bg='lightgrey')
    app8.resizable(0,0)

    temp=StringVar()

    style=ttk.Style()
    style.theme_use('default')

    queryLabel=Label(app8,text='Query',font=('arial',14,'bold'),bg='lightgrey')
    queryLabel.grid(row=0,column=0)

    questionField=Entry(app8,width=45,font=('arial',14,'bold'),bd=4,relief=SUNKEN)
    questionField.grid(padx=10,row=0,column=1)

    micImage=PhotoImage(file='mic1.png')
    micButTon=Button(app8,image=micImage,bg='lightgrey',bd=0,cursor='hand2',activebackground='lightgrey'
                    ,command=voice)
    micButTon.grid(row=0,column=2)

    searchImage=PhotoImage(file='search.png')

    searchButton=Button(app8,image=searchImage,bd=0,cursor='hand2',bg='lightgrey',activebackground='lightgrey'
                        ,command=search)
    searchButton.grid(row=0,column=3,padx=5)

    googleRadioButton=ttk.Radiobutton(app8,text='Google',value='google',variable=temp)
    googleRadioButton.place(x=75,y=40)

    duckRadioButton=ttk.Radiobutton(app8,text='Duck Duck Go',value='duck',variable=temp)
    duckRadioButton.place(x=200,y=40)

    amzonRadioButton=ttk.Radiobutton(app8,text='Amazon',value='amazon',variable=temp)
    amzonRadioButton.place(x=380,y=40)

    youtubeRadioButton=ttk.Radiobutton(app8,text='Youtube',value='youtube',variable=temp)
    youtubeRadioButton.place(x=510,y=40)

    def enter_function(value):
        searchButton.invoke()

    app8.bind('<Return>',enter_function)

    temp.set('google')





    app8.mainloop()
############################################################################



#############################Mail################################################
def mail():
    # importing modules

    check=False

    def browse():
        global final_emails
        path=filedialog.askopenfilename(initialdir='c:/',title='Select Excel File')
        if path=='':
            messagebox.showerror('Error','Please select an Excel File')

        else:
            data=pandas.read_excel(path)
            if 'Email' in data.columns:
                emails=list(data['Email'])
                final_emails=[]
                for i in emails:
                    if pandas.isnull(i)==False:
                        final_emails.append(i)

                if len(final_emails)==0:
                    messagebox.showerror('Error','File does not contain any email addresses')

                else:
                    toEntryField.config(state=NORMAL)
                    toEntryField.insert(0,os.path.basename(path))
                    toEntryField.config(state='readonly')
                    totalLabel.config(text='Total: '+str(len(final_emails)))
                    sentLabel.config(text='Sent:')
                    leftLabel.config(text='Left:')
                    failedLabel.config(text='Failed:')







    def button_check():
        if choice.get()=='multiple':
            browseButton.config(state=NORMAL)
            toEntryField.config(state='readonly')

        if choice.get()=='single':
            browseButton.config(state=DISABLED)
            toEntryField.config(state=NORMAL)



    def attachment():
        global filename,filetype,filepath,check
        check=True

        filepath=filedialog.askopenfilename(initialdir='c:/',title='Select File')
        filetype=filepath.split('.')
        filetype=filetype[1]
        filename=os.path.basename(filepath)
        textarea.insert(END,f'\n{filename}\n')



    def sendingEmail(toAddress,subject,body):
        f=open('credentials.txt','r')
        for i in f:
            credentials=i.split(',')

        message=EmailMessage()
        message['subject']=subject
        message['to']=toAddress
        message['from']=credentials[0]
        message.set_content(body)
        if check:
            if filetype=='png' or filetype=='jpg' or filetype=='jpeg':
                f=open(filepath,'rb')
                file_data=f.read()
                subtype=imghdr.what(filepath)


                message.add_attachment(file_data,maintype='image',subtype=subtype,filename=filename)

            else:
                f = open(filepath, 'rb')
                file_data = f.read()
                message.add_attachment(file_data,maintype='application',subtype='octet-stream',filename=filename)


        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(credentials[0],credentials[1])
        s.send_message(message)
        x=s.ehlo()
        if x[0]==250:
            return 'sent'
        else:
            return 'failed'






    def send_email():
        if toEntryField.get()=='' or subjectEntryField.get()=='' or textarea.get(1.0,END)=='\n':
            messagebox.showerror('Error','All Fields Are Required',parent=root)

        else:
            if choice.get()=='single':
                result=sendingEmail(toEntryField.get(),subjectEntryField.get(),textarea.get(1.0,END))
                if result=='sent':
                    messagebox.showinfo('Success','Email is sent successfuly')

                if result=='failed':
                    messagebox.showerror('Error','Email is not sent.')

            if choice.get()=='multiple':
                sent=0
                failed=0
                for x in final_emails:
                    result=sendingEmail(x,subjectEntryField.get(),textarea.get(1.0,END))
                    if result=='sent':
                        sent+=1
                    if result=='failed':
                        failed+=1

                    totalLabel.config(text='')
                    sentLabel.config(text='Sent:' + str(sent))
                    leftLabel.config(text='Left:' + str(len(final_emails) - (sent + failed)))
                    failedLabel.config(text='Failed:' + str(failed))

                    totalLabel.update()
                    sentLabel.update()
                    leftLabel.update()
                    failedLabel.update()

                messagebox.showinfo('Success','Emails are sent successfully')




    def settings():
        def clear1():
            fromEntryField.delete(0,END)
            passwordEntryField.delete(0,END)

        def save():
            if fromEntryField.get()=='' or passwordEntryField.get()=='':
                messagebox.showerror('Error','All Fields Are Required',parent=root1)

            else:
                f=open('credentials.txt','w')
                f.write(fromEntryField.get()+','+passwordEntryField.get())
                f.close()
                messagebox.showinfo('Information','CREDENTIALS SAVED SUCCESSFULLY',parent=root1)
    #Gui for setting 
        root1=Toplevel()
        root1.title('Setting')
        root1.geometry('650x340+350+90')

        root1.config(bg='dodger blue2')

        Label(root1,text='Credential Settings',image=logoImage,compound=LEFT,font=('goudy old style',40,'bold'),
            fg='white',bg='gray20').grid(padx=60)

        fromLabelFrame = LabelFrame(root1, text='From (Email Address)', font=('times new roman', 16, 'bold'), bd=5, fg='white',
                                bg='dodger blue2')
        fromLabelFrame.grid(row=1, column=0,pady=20)

        fromEntryField = Entry(fromLabelFrame, font=('times new roman', 18, 'bold'), width=30)
        fromEntryField.grid(row=0, column=0)

        passwordLabelFrame = LabelFrame(root1, text='Password', font=('times new roman', 16, 'bold'), bd=5,
                                    fg='white',
                                    bg='dodger blue2')
        passwordLabelFrame.grid(row=2, column=0, pady=20)

        passwordEntryField = Entry(passwordLabelFrame, font=('times new roman', 18, 'bold'), width=30,show='*')
        passwordEntryField.grid(row=0, column=0)

        Button(root1,text='SAVE',font=('times new roman',18,'bold'),cursor='hand2',bg='gold2',fg='black'
            ,command=save).place(x=210,y=280)
        Button(root1,text='CLEAR',font=('times new roman',18,'bold'),cursor='hand2',bg='gold2',fg='black'
            ,command=clear1).place(x=340,y=280)

        f=open('credentials.txt','r')
        for i in f:
            credentials=i.split(',')

        fromEntryField.insert(0,credentials[0])
        passwordEntryField.insert(0,credentials[1])







        root1.mainloop()

    def speak():
        mixer.init()
        mixer.music.load('music.mp3')
        mixer.music.play()
        sr=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as m:
            try:
                sr.adjust_for_ambient_noise(m,duration=0.2)
                audio=sr.listen(m)
                text=sr.recognize_google(audio)
                textarea.insert(END,text+'.')

            except:
                pass


    def iexit():
        result=messagebox.askyesno('Notification','Do you want to exit?')
        if result:
            app9.destroy()
        else:
            pass

    def clear():
        toEntryField.delete(0,END)
        subjectEntryField.delete(0,END)
        textarea.delete(1.0,END)



    #Gui
    app9=Toplevel()
    app9.title('Email sender app ')
    app9.geometry('780x620+100+50')
    app9.resizable(0,0)
    app9.config(bg='dodger blue2')

    titleFrame=Frame(app9,bg='white')
    titleFrame.grid(row=0,column=0)
    logoImage=PhotoImage(file='email.png')
    titleLabel=Label(titleFrame,text='  Email Sender',image=logoImage,compound=LEFT,font=('Goudy Old Style',28,'bold'),
                    bg='white',fg='dodger blue2')
    titleLabel.grid(row=0,column=0)
    settingImage=PhotoImage(file='setting.png')

    Button(titleFrame,image=settingImage,bd=0,bg='white',cursor='hand2',activebackground='white'
        ,command=settings).grid(row=0,column=1,padx=20)

    chooseFrame=Frame(app9,bg='dodger blue2')
    chooseFrame.grid(row=1,column=0,pady=10)
    choice=StringVar()

    singleRadioButton=Radiobutton(chooseFrame,text='Single',font=('times new roman',25,'bold')
                                ,variable=choice,value='single',bg='dodger blue2',activebackground='dodger blue2',
                                command=button_check)
    singleRadioButton.grid(row=0,column=0,padx=20)

    multipleRadioButton=Radiobutton(chooseFrame,text='Multiple',font=('times new roman',25,'bold')
                                ,variable=choice,value='multiple',bg='dodger blue2',activebackground='dodger blue2',
                                    command=button_check)
    multipleRadioButton.grid(row=0,column=1,padx=20)

    choice.set('single')

    toLabelFrame=LabelFrame(app9,text='To (Email Address)',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
    toLabelFrame.grid(row=2,column=0,padx=100)

    toEntryField=Entry(toLabelFrame,font=('times new roman',18,'bold'),width=30)
    toEntryField.grid(row=0,column=0)

    browseImage=PhotoImage(file='browse.png')

    browseButton=Button(toLabelFrame,text=' Browse',image=browseImage,compound=LEFT,font=('arial',12,'bold'),
        cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2',state=DISABLED,command=browse)
    browseButton.grid(row=0,column=1,padx=20)

    subjectLabelFrame=LabelFrame(app9,text='Subject',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
    subjectLabelFrame.grid(row=3,column=0,pady=10)

    subjectEntryField=Entry(subjectLabelFrame,font=('times new roman',18,'bold'),width=30)
    subjectEntryField.grid(row=0,column=0)

    emailLabelFrame=LabelFrame(app9,text='Compose Email',font=('times new roman',16,'bold'),bd=5,fg='white',bg='dodger blue2')
    emailLabelFrame.grid(row=4,column=0,padx=20)
    micImage=PhotoImage(file='mic.png')

    Button(emailLabelFrame,text=' Speak',image=micImage,compound=LEFT,font=('arial',12,'bold'),
        cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2',command=speak).grid(row=0,column=0)
    attachImage=PhotoImage(file='attachments.png')

    Button(emailLabelFrame,text=' Attachment',image=attachImage,compound=LEFT,font=('arial',12,'bold'),
        cursor='hand2',bd=0,bg='dodger blue2',activebackground='dodger blue2',command=attachment).grid(row=0,column=1)

    textarea=Text(emailLabelFrame,font=('times new roman',14,),height=8)
    textarea.grid(row=1,column=0,columnspan=2)

    sendImage=PhotoImage(file='send.png')
    Button(app9,image=sendImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2'
        ,command=send_email).place(x=490,y=540)

    clearImage=PhotoImage(file='clear.png')
    Button(app9,image=clearImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2'
        ,command=clear).place(x=590,y=550)

    exitImage=PhotoImage(file='exit.png')
    Button(app9,image=exitImage,bd=0,bg='dodger blue2',cursor='hand2',activebackground='dodger blue2'
        ,command=iexit).place(x=690,y=550)

    totalLabel=Label(app9,font=('times new roman',18,'bold'),bg='dodger blue2',fg='black')
    totalLabel.place(x=10,y=560)

    sentLabel=Label(app9,font=('times new roman',18,'bold'),bg='dodger blue2',fg='white')
    sentLabel.place(x=120,y=560)

    leftLabel=Label(app9,font=('times new roman',18,'bold'),bg='dodger blue2',fg='white')
    leftLabel.place(x=210,y=560)

    failedLabel=Label(app9,font=('times new roman',18,'bold'),bg='dodger blue2',fg='white')
    failedLabel.place(x=300,y=560)

    app9.mainloop()






###################################################################################



###############################To-Do List#############################################

def to_do():
    

    # defining the function to add tasks to the list  
    def add_task():  
        # getting the string from the entry field  
        task_string = task_field.get()  
        # checking whether the string is empty or not  
        if len(task_string) == 0:  
            # displaying a message box with 'Empty Field' message  
            messagebox.showerror('Error', 'Field is Empty.')  
        else:  
            # adding the string to the tasks list  
            tasks.append(task_string)  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('insert into tasks values (?)', (task_string ,))  
            # calling the function to update the list  
            list_update()  
            # deleting the entry in the entry field  
            task_field.delete(0, 'end')  
    
    # defining the function to update the list  
    def list_update():  
        # calling the function to clear the list  
        clear_list()  
        # iterating through the strings in the list  
        for task in tasks:  
            # using the insert() method to insert the tasks in the list box  
            task_listbox.insert('end', task)  
    
    # defining the function to delete a task from the list  
    def delete_task():  
        # using the try-except method  
        try:  
            # getting the selected entry from the list box  
            the_value = task_listbox.get(task_listbox.curselection())  
            # checking if the stored value is present in the tasks list  
            if the_value in tasks:  
                # removing the task from the list  
                tasks.remove(the_value)  
                # calling the function to update the list  
                list_update()  
                # using the execute() method to execute a SQL statement  
                the_cursor.execute('delete from tasks where title = ?', (the_value,))  
        except:  
            # displaying the message box with 'No Item Selected' message for an exception  
            messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
    
    # function to delete all tasks from the list  
    def delete_all_tasks():  
        # displaying a message box to ask user for confirmation  
        message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
        # if the value turns to be True  
        if message_box == True:  
            # using while loop to iterate through the tasks list until it's empty   
            while(len(tasks) != 0):  
                # using the pop() method to pop out the elements from the list  
                tasks.pop()  
            # using the execute() method to execute a SQL statement  
            the_cursor.execute('delete from tasks')  
            # calling the function to update the list  
            list_update()  
    
    # function to clear the list  
    def clear_list():  
        # using the delete method to delete all entries from the list box  
        task_listbox.delete(0, 'end')  
    
    # function to close the application  
    def close():  
        # printing the elements from the tasks list  
        print(tasks)  
        # using the destroy() method to close the application  
        guiWindow.destroy()  
    
    # function to retrieve data from the database  
    def retrieve_database():  
        # using the while loop to iterate through the elements in the tasks list  
        while(len(tasks) != 0):  
            # using the pop() method to pop out the elements from the list  
            tasks.pop()  
        # iterating through the rows in the database table  
        for row in the_cursor.execute('select title from tasks'):  
            # using the append() method to insert the titles from the table in the list  
            tasks.append(row[0])  
    
    # main function  
    if __name__ == "__main__":  
        # creating an object of the Tk() class  
        guiWindow = Toplevel()  
        # setting the title of the window  
        guiWindow.title("To-Do List Manager ")  
        # setting the geometry of the window  
        guiWindow.geometry("600x550+100+0")  
        # disabling the resizable option  
        guiWindow.resizable(0, 0)  
        # setting the background color to #FAEBD7  
        guiWindow.configure(bg = "#FAEBD7")  
    
        # using the connect() method to connect to the database  
        the_connection = sql.connect('ListOfTasks.db')  
        # creating the cursor object of the cursor class  
        the_cursor = the_connection.cursor()  
        # using the execute() method to execute a SQL statement  
        the_cursor.execute('create table if not exists tasks (title text)')  
    
        # defining an empty list  
        tasks = []  
        
        # defining frames using the tk.Frame() widget  
        header_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
        functions_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
        listbox_frame = tk.Frame(guiWindow, bg = "#FAEBD7")  
    
        # using the pack() method to place the frames in the application  
        header_frame.pack(fill = "both")  
        functions_frame.pack(side = "left", expand = True, fill = "both")  
        listbox_frame.pack(side = "right", expand = True, fill = "both")  
        
        # defining a label using the ttk.Label() widget  
        header_label = ttk.Label(  
            header_frame,  
            text = "The To-Do List",  
            font = ("Brush Script MT", "30"),  
            background = "#FAEBD7",  
            foreground = "#8B4513"  
        )  
        # using the pack() method to place the label in the application  
        header_label.pack(padx = 20, pady = 20)  
    
        # defining another label using the ttk.Label() widget  
        task_label = ttk.Label(  
            functions_frame,  
            text = "Enter the Task:",  
            font = ("Consolas", "11", "bold"),  
            background = "#FAEBD7",  
            foreground = "#000000"  
        )  
        # using the place() method to place the label in the application  
        task_label.place(x = 30, y = 40)  
        
        # defining an entry field using the ttk.Entry() widget  
        task_field = ttk.Entry(  
            functions_frame,  
            font = ("Consolas", "12"),  
            width = 18,  
            background = "#FFF8DC",  
            foreground = "#A52A2A"  
        )  
        # using the place() method to place the entry field in the application  
        task_field.place(x = 30, y = 80)  
    
        # adding buttons to the application using the ttk.Button() widget  
        add_button = ttk.Button(  
            functions_frame,  
            text = "Add Task",  
            width = 24,  
            command = add_task  
        )  
        del_button = ttk.Button(  
            functions_frame,  
            text = "Delete Task",  
            width = 24,  
            command = delete_task  
        )  
        del_all_button = ttk.Button(  
            functions_frame,  
            text = "Delete All Tasks",  
            width = 24,  
            command = delete_all_tasks  
        )  
        exit_button = ttk.Button(  
            functions_frame,  
            text = "Exit",  
            width = 24,  
            command = close  
        )  
        # using the place() method to set the position of the buttons in the application  
        add_button.place(x = 30, y = 120)  
        del_button.place(x = 30, y = 160)  
        del_all_button.place(x = 30, y = 200)  
        exit_button.place(x = 30, y = 240)  
    
        # defining a list box using the tk.Listbox() widget  
        task_listbox = tk.Listbox(  
            listbox_frame,  
            width = 36,  
            height = 23,  
            selectmode = 'SINGLE',  
            background = "#FFFFFF",  
            foreground = "#000000",  
            selectbackground = "#CD853F",  
            selectforeground = "#FFFFFF"  
        )  
        # using the place() method to place the list box in the application  
        task_listbox.place(x = 10, y = 20)  
    
        # calling some functions  
        retrieve_database()  
        list_update()  
        # using the mainloop() method to run the application  
        guiWindow.mainloop()  
        # establishing the connection with database  
        the_connection.commit() 
        the_cursor.close()  
        


##############################################################################################
            



#--------------------------------------------------------------------------#
rhb=Frame(body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickness=1)
rhb.place(x=330,y=255)
apps=Label(rhb,text='Apps',font=('Acumin Variable Concept',15),bg="#f4f5f5")
apps.place(x=10,y=10)
app_1image=PhotoImage(file="image/App1.png")
app1=Button(rhb,image=app_1image,bd=0,cursor="hand2",command=weather)
app1.place(x=15,y=50)

app_2image=PhotoImage(file="image/App2.png")
app2=Button(rhb,image=app_2image,bd=0,cursor="hand2",command=clock)
app2.place(x=100,y=50)

app_3image=PhotoImage(file="image/App3.png")
app3=Button(rhb,image=app_3image,bd=0,cursor="hand2",command=date)
app3.place(x=185,y=50)

app_4image=PhotoImage(file="image/App4.png")
app4=Button(rhs,image=app_4image,bd=0,cursor="hand2",command=mode)
app4.place(x=300,y=170)

app4image=PhotoImage(file="image/screen.png")
app44=Button(rhs,image=app4image,bd=0,cursor="hand2",command=scr)
app44.place(x=380,y=170)

app_44image=PhotoImage(file="image/dict.png")
app45=Button(rhb,image=app_44image,bd=0,cursor="hand2",command=dic)
app45.place(x=270,y=50)




app_5image=PhotoImage(file="image/App5.png")
app5=Button(rhb,image=app_5image,bd=0,cursor="hand2",command=game)
app5.place(x=355,y=50)

app_6image=PhotoImage(file="image/wiki.png")
app6=Button(rhb,image=app_6image,bd=0,cursor="hand2",command=screenshot)
app6.place(x=15,y=120)

app_7image=PhotoImage(file="image/App7.png")
app7=Button(rhb,image=app_7image,bd=0,cursor="hand2",command=file)
app7.place(x=100,y=120)

app_8image=PhotoImage(file="image/App8.png")
app8=Button(rhb,image=app_8image,bd=0,cursor="hand2",command=search)
app8.place(x=185,y=120)

app_9image=PhotoImage(file="image/App9.png")
app9=Button(rhb,image=app_9image,bd=0,cursor="hand2",command=mail)
app9.place(x=270,y=120)


app_10image=PhotoImage(file="image/App10.png")
app10=Button(rhb,image=app_10image,bd=0,cursor="hand2",command=to_do)
app10.place(x=355,y=120)







root.mainloop()



