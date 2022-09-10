from tkinter import *
import requests
import geocoder
from tkinter import messagebox

wn = Tk()
wn.geometry("300x200")
wn.configure(background="Lime")
a = Entry(wn)
a.configure(bd=2)
a.grid(row=0,column=1)
wn.title("Air temp")

w = "lime"

def loc():
    global lat
    global lon
    global la7
    global la9
    g = geocoder.bing(a.get(), key='ApJOpbd91RkruF7cDqJUoQxXyL6GRb1bixyMUHDlbBZ0DIiTIobA7h6aLCz6joma')
    results = g.json
    lat = results['lat']
    lon = results['lng']
    la7 = Label(wn, text=lat, background=w)
    la7.grid(row=5, column=1)
    la9 = Label(wn, text=lon, background=w)
    la9.grid(row=6, column=1)


    response = requests.get(
        'https://api.stormglass.io/v2/weather/point',
        params={
            'lat': 58.7984,
            'lng': 17.8081,
            'params': ','.join(['humidity', 'airTemperature']),
        },
        headers={
            'Authorization': '87c5d39a-3057-11ed-93b0-0242ac130002-87c5d3f4-3057-11ed-93b0-0242ac130002'
        }
    )
    data = response.json()
    print(data)
    try:
        temp = data['hours'][0]['airTemperature']['dwd']
        humi = data['hours'][0]['humidity']['dwd']
        global la3
        global la4
        la3 = Label(wn,text=temp,background=w)
        la3.grid(row=3,column=1)
        la4 = Label(wn,text=humi,background=w)
        la4.grid(row=4,column=1)

        if temp<=10:
            la0 = Label(wn,text="",background="blue")
            la0.grid(row=3,column=2)
        elif temp>10 and temp<=25:
            la0 = Label(wn, text="", background="green")
            la0.grid(row=3, column=2)
        elif temp>25 and temp<=35:
            la0 = Label(wn, text="", background="Orange")
            la0.grid(row=3, column=2)
        else:
            la0 = Label(wn, text="", background="red")
            la0.grid(row=3, column=2)

    except Exception as e:
        messagebox.showerror("Error!","Sorry,Try again later!!!")
        exit()

la6 = Label(wn, text="Latitude:",background=w)
la6.grid(row=5, column=0)

la8 = Label(wn, text="Longitude:",background=w)
la8.grid(row=6, column=0)


b1 = Button(wn,text="Enter",command=loc,background="light green")
b1.grid(row=2,column=1)

la1 = Label(wn,text="Temperature:",background=w)
la1.grid(row=3,column=0)
la2 = Label(wn,text="Humidity:",background=w)
la2.grid(row=4,column=0)

def dark():
    try:
        wn.configure(bg="black")
        la1.configure(bg="black", fg="white")
        la2.configure(bg="black", fg="white")
        la3.configure(bg="black", fg="white")
        la4.configure(bg="black", fg="white")
        la6.configure(bg="black", fg="white")
        la7.configure(bg="black", fg="white")
        la8.configure(bg="black", fg="white")
        la9.configure(bg="black", fg="white")
        la10.configure(bg="black", fg="white")
        b1.configure(bg="gray", fg="white")

    except Exception as e:
        wn.configure(bg="black")
        la1.configure(bg="black", fg="white")
        la2.configure(bg="black", fg="white")
        la6.configure(bg="black", fg="white")
        la8.configure(bg="black", fg="white")
        b1.configure(bg="gray", fg="white")
        la10.configure(bg="black", fg="white")


def light():
    try:
        wn.configure(bg=w)
        la1.configure(bg=w, fg="black")
        la2.configure(bg=w, fg="black")
        la3.configure(bg=w, fg="black")
        la4.configure(bg=w, fg="black")
        la6.configure(bg=w, fg="black")
        la7.configure(bg=w, fg="black")
        la8.configure(bg=w, fg="black")
        la9.configure(bg=w, fg="black")
        la10.configure(bg=w, fg="black")
        b1.configure(bg=w, fg="black")

    except Exception as e:
        wn.configure(bg=w)
        la1.configure(bg=w, fg="black")
        la2.configure(bg=w, fg="black")
        la6.configure(bg=w, fg="black")
        la8.configure(bg=w, fg="black")
        b1.configure(bg=w, fg="black")
        la10.configure(bg=w, fg="black")


r1 = IntVar()

Radiobutton(wn,text="Dark",background="gray",variable=r1,value=1,fg="black",command=lambda :dark()).grid(row=10,column=0)
Radiobutton(wn,text="Light",background="lime",variable=r1,value=2,command=lambda :light()).grid(row=11,column=0)


la10 = Label(wn,text="Created by Rahul",bg="lime",fg="red")
la10.grid(row=10,column=4)
wn.mainloop()