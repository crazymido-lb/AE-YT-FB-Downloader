from tkinter import Tk, Label, N, StringVar, Entry, Button, PhotoImage, E, W, Menu
from tkinter import messagebox
import pytube
import webbrowser
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
import os
import re
import requests
import urllib.request


#Functions
def download():
    # Create message box
    clicked = messagebox.askquestion("Choose Resolution", "Do you want to download video in High resolution?\nYes = High Resolution\nNo = Low Resolution")
    if clicked == "yes":
        hddownload()
    else:
        sddownload()
        
def hddownload():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_highest_resolution()
        video.download("C:/users/Public/Videos")
        notif.config(fg="green",text="Download completed")
        notifbox = messagebox.askyesno("Download Completed", "Do you want to open file location?")
        if notifbox == 1:
            webbrowser.open('C:/users/Public/Videos')
        else:
            return
    except Exception as e:
        print(e)
        link = url.get()
        html = requests.get(link)
        try:
            link = re.search('hd.src:"(.+?)"',html.text)[1]
            urllib.request.urlretrieve(link,"c:/users/Public/Videos/Facebook.mp4")
            down_complete = messagebox.askyesno("Download Completed", "Download Completed Successfuly\nDo you want to open file location?")
            notif.config(fg="green",text="Download completed")
            notifbox = messagebox.askyesno("Download Completed", "Do you want to open file location?")
            if notifbox == 1:
                webbrowser.open('C:/users/Public/Videos')
            else:
                return
        except Exception as e:
            print(e)
            notif.config(fg="red",text="Video could not be downloaded")
            alertbox = messagebox.showerror("Error", "This video could not be downloaded.\nPlease check the link and try again.")

def sddownload():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.get_lowest_resolution()
        video.download("C:/users/Public/Videos")
        notif.config(fg="green",text="Download completed")
        notifbox = messagebox.askyesno("Download Completed", "Do you want to open file location?")
        if notifbox == 1:
            webbrowser.open('C:/users/Public/Videos')
        else:
            return
    except Exception as e:
        print(e)
        link = url.get()
        html = requests.get(link)
        try:
            link = re.search('sd.src:"(.+?)"',html.text)[1]
            urllib.request.urlretrieve(link,"c:/users/Public/Videos/Facebook.mp4")
            notif.config(fg="green",text="Download completed")
            notifbox = messagebox.askyesno("Download Completed", "Do you want to open file location?")
            if notifbox == 1:
                webbrowser.open('C:/users/Public/Videos')
            else:
                return
        except Exception as e:
            print(e)
            notif.config(fg="red",text="Video could not be downloaded")
            alertbox = messagebox.showerror("Error", "This video could not be downloaded.\nPlease check the link and try again.")

def browse():
    webbrowser.open('C:/users/Public/Videos')

def exit():
    master.quit()

def openlink():
    fblink = 'https://www.facebook.com/arbeagles'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(fblink)

def ytlink():
    ytubelink = 'https://www.youtube.com/channel/UCmcGB8PNVxig1WGye-H3ZIA'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(ytubelink)

def devlink():
    cdlink = 'https://www.facebook.com/CrazyMido8'
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
    webbrowser.get('chrome').open(cdlink)

def aboutapp():
    showinfo("About ArabEagles Videos Downloader", "This App is designed by CrazyMido for ArabEagles!\nPlease follow us on Facebook and subscribe to our YouTube channel.")

#Main Screen
master = Tk()
master.configure()
icon = PhotoImage(file = 'L:/python apps/Videos Downloader/logo2.png')
master.iconphoto(False, icon)
master.title("ArabEagles Videos Downloader")
master.resizable(width=False, height=False)
bgimage = ImageTk.PhotoImage(Image.open('L:/python apps/Videos Downloader/logo222.png'))
Label(master, image = bgimage).place(relwidth = 1, relheight = 1)

# Creat Menu
my_menu = Menu(master)
master.config(menu=my_menu)

# Add File Menu
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=master.quit)

# Add Help Menu
help_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="About", menu=help_menu)
help_menu.add_command(label="Our FaceBook Page", command=openlink)
help_menu.add_command(label="Our YouTube Channel", command=ytlink)
help_menu.add_command(label="Contact Developer", command=devlink)
help_menu.add_separator()
help_menu.add_command(label="About App", command=aboutapp)


#Labels
Label(master, text="", fg="red", font=("Times",16,"bold")).grid(sticky=W,pady=10,row=0)
Label(master,text="", fg="black", font=("Times",12,"bold")).grid(sticky=W,row=1,pady=10)
notif = Label(master, font=("Times",12))
notif.grid(sticky=W,padx=10,pady=10,row=6)
status = Label(master, text="Created by:CrazyMido - ver:1.0.0", fg="black", anchor=E)

#Vars
url = StringVar()

#Entry
Entry(master,width=50,font=("Calibri",14), bd=3, textvariable=url).grid(sticky=N,row=2,pady=10,padx=20)

#Button
Button(master,width=20,text="Download Video",font=("Calibri",12),bg="#BEBEBE",command=download).grid(sticky=N,row=3,pady=10,padx=70)
# Button(master,width=20,text="Low Resolution",font=("Calibri",12),bg="#BEBEBE",command=sddownload).grid(sticky=W,row=3,pady=10,padx=70)
Button(master,width=15,text="Folder Location",font=("Calibri",12),bg="#BEBEBE",command=browse).grid(sticky=W,row=5,padx=70,pady=10)
Button(master,width=15,text="Close",font=("Calibri",12),bg="#BEBEBE",command=exit).grid(sticky=E,row=5,padx=70,pady=10)
Button(master,width=22,text="Click here to visit our Page!",font=("Calibri",10),fg="#0000FF",bd=0,command=openlink).grid(sticky=W,row=7)
status.grid(row=7,padx=10,sticky=E)

master.mainloop()