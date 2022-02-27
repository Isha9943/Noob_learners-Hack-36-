from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from win10toast_click import ToastNotifier
from plyer import notification
import urllib
import datetime
import schedule
import time
import webbrowser

n = ToastNotifier()
timeout = 20
t = Tk()
t.title('Reminder')
t.geometry("500x350")
img_path = "image.jpg"
img = Image.open("image.jpg")
image_size = (60,60)
img = img.resize(image_size)
tkimage = ImageTk.PhotoImage(img)
t.configure(bg='#4c83cf')


# To get directed to the link provided
def open_link(link):
    if link:
        if link.startswith('http'):
            webbrowser.open(link)
        else:
            webbrowser.open('http://'+link)
    else:
        pass


# Notification function
def notify_func(title, desc, link,timeout=20):
        n.show_toast(
            title=title,
            msg=desc,

            icon_path="image.ico",
            duration=timeout,
            callback_on_click=lambda: open_link(link)
        )

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_link = link.get()
    notification_time = date_time.get()
    FMT = '%d/%m/%y %H:%M'
    try:
        datetime.datetime.strptime(notification_time,FMT)
        if(notification_time<datetime.datetime.now().strftime(FMT)):
            messagebox.showerror("Alert", "Incorrect Time")
    except:
        messagebox.showerror("Alert","Incorrect Time Format")

    # print(get_title,get_msg,get_link,get_time_hr,get_time_min)

    if get_title == "":
        messagebox.showerror("Alert", "Title is required")
    elif get_msg == "":
        messagebox.showerror("Alert", "Description is required")
    else:
        t.destroy()
        while(datetime.datetime.now().strftime(FMT)<notification_time):
            print(datetime.datetime.now().strftime(FMT))
            time.sleep(1)
            pass
        notify_func(title=get_title,desc=get_msg,link=get_link)



img_label = Label(t, image=tkimage).grid()
# heading
heading = Label(t, text="Reminder", font=("poppins",30))
heading.place(x= 150, y=10)
heading.configure(bg='#4c83cf')

# Label - Title
t_label = Label(t, text="Title of Task", font=("poppins", 10))
t_label.place(x=12, y=80)
t_label.configure(bg='#4c83cf')

# ENTRY - Title
title = Entry(t, width="25", font=("poppins", 13))
title.place(x=123, y=80)


# Label - Message
m_label = Label(t, text="Display Message", font=("poppins", 10))
m_label.place(x=12, y=120)
m_label.configure(bg='#4c83cf')

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123, height=30, y=120)


# Label - Link
l_label = Label(t, text="Link", font=("poppins", 10))
l_label.place(x=12, y=170)
l_label.configure(bg='#4c83cf')
# ENTRY - Link
link = Entry(t, width="40", font=("poppins", 13))
link.place(x=123, y=170)


# Label - Time
time_label = Label(t, text="Time", font=("poppins", 10))
time_format = Label(t, text="(dd/mm/yy HH:mm)", font=('poppins',10))
time_label.place(x=12, y=210)
time_label.configure(bg='#4c83cf')
time_format.place(x=0,y=230)
time_format.configure(bg='#4c83cf')

# ENTRY - Time
date_time = Entry(t,width='40', font=('poppins',13))
date_time.place(x = 123, y = 210)

# Button
but = Button(t, text="SET Reminder", font=("poppins", 10, "bold"), fg="#ffffff", bg="#e61e42", width=20,
             relief="raised",
             command=get_details)
but.place(x=170, y=280)

t.resizable(0, 0)
t.mainloop()
