from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim  #For coordinates
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests    #For HTTP Requests
import pytz
from PIL import Image, ImageTk     #Timezone calculations

root = tk.Tk()
root.title("Weather App")
root.geometry("900x545+300+200")
root.resizable(False,False)

def getWeather():
    try:
        city = text.get()
        geolocator = Nominatim(user_agent = "geoapiExercises")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng = location.longitude,lat = location.latitude)
        timezone.config(text = result)
        long_lat.config(text = f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text = current_time)

        #Weather
        api = "https://api.openweathermap.org/data/2.5/forecast?lat="+str(location.latitude)+"&lon="+str(location.longitude)+"&appid=1af5f50bf86873e936e19807b35cf297"
        json_data = requests.get(api).json()

        #Current
        temp = int(json_data['list'][0]['main']['temp']-273.15)
        humidity = json_data['list'][0]['main']['humidity']
        pressure = json_data['list'][0]['main']['pressure']
        speed = json_data['list'][0]['wind']['speed']
        desc = json_data['list'][0]['weather'][0]['description']

        t.config(text = (temp, "°C"))
        h.config(text = (humidity, "%"))
        p.config(text = (pressure, "hPa"))
        s.config(text = (speed, "m/s"))
        d.config(text = desc)

        #First Cell
        firstdayimg = json_data['list'][0]['weather'][0]['icon']
        photo1 = ImageTk.PhotoImage(file = f"icon/{firstdayimg}@2x.png")
        firstimg.config(image = photo1)
        firstimg.image = photo1
        tempday1_max = int(json_data['list'][0]['main']['temp_max']-273.15)
        tempday1_min = int(json_data['list'][0]['main']['temp_min']-273.15)
        day1temp.config(text = f"Max:{tempday1_max}\nMin:{tempday1_min}")

        #Second Cell
        seconddayimg = json_data['list'][1]['weather'][0]['icon']
        img = (Image.open(f"icon/{seconddayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo2 = ImageTk.PhotoImage(resized_img)
        secimg.config(image = photo2)
        secimg.image = photo2
        tempday2_max = int(json_data['list'][1]['main']['temp_max']-273.15)
        tempday2_min = int(json_data['list'][1]['main']['temp_min']-273.15)
        day2temp.config(text = f"Max:{tempday2_max}\nMin:{tempday2_min}")

        #Third Cell
        thirddayimg = json_data['list'][2]['weather'][0]['icon']
        img = (Image.open(f"icon/{thirddayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo3 = ImageTk.PhotoImage(resized_img)
        thirdimg.config(image = photo3)
        thirdimg.image = photo3
        tempday3_max = int(json_data['list'][2]['main']['temp_max']-273.15)
        tempday3_min = int(json_data['list'][2]['main']['temp_min']-273.15)
        day3temp.config(text = f"Max:{tempday3_max}\nMin:{tempday3_min}")

        #Fourth Cell
        fourthdayimg = json_data['list'][3]['weather'][0]['icon']
        img = (Image.open(f"icon/{fourthdayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo4 = ImageTk.PhotoImage(resized_img)
        fourthimg.config(image = photo4)
        fourthimg.image = photo4
        tempday4_max = int(json_data['list'][3]['main']['temp_max']-273.15)
        tempday4_min = int(json_data['list'][3]['main']['temp_min']-273.15)
        day4temp.config(text = f"Max:{tempday4_max}\nMin:{tempday4_min}")

        #Fifth Cell
        fifthdayimg = json_data['list'][4]['weather'][0]['icon']
        img = (Image.open(f"icon/{fifthdayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo5 = ImageTk.PhotoImage(resized_img)
        fifthimg.config(image = photo5)
        fifthimg.image = photo5
        tempday5_max = int(json_data['list'][4]['main']['temp_max']-273.15)
        tempday5_min = int(json_data['list'][4]['main']['temp_min']-273.15)
        day5temp.config(text = f"Max:{tempday5_max}\nMin:{tempday5_min}")

        #Sixth Cell
        sixthdayimg = json_data['list'][5]['weather'][0]['icon']
        img = (Image.open(f"icon/{sixthdayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo6 = ImageTk.PhotoImage(resized_img)
        sixthimg.config(image = photo6)
        sixthimg.image = photo6
        tempday6_max = int(json_data['list'][5]['main']['temp_max']-273.15)
        tempday6_min = int(json_data['list'][5]['main']['temp_min']-273.15)
        day6temp.config(text = f"Max:{tempday6_max}\nMin:{tempday6_min}")

        #Seventh Cell
        sevendayimg = json_data['list'][6]['weather'][0]['icon']
        img = (Image.open(f"icon/{sevendayimg}@2x.png"))
        resized_img = img.resize((50,50))
        photo7 = ImageTk.PhotoImage(resized_img)
        sevenimg.config(image = photo7)
        sevenimg.image = photo7
        tempday7_max = int(json_data['list'][6]['main']['temp_max']-273.15)
        tempday7_min = int(json_data['list'][6]['main']['temp_min']-273.15)
        day7temp.config(text = f"Max:{tempday7_max}\nMin:{tempday7_min}")

        #Days
        first = datetime.now()
        day1.config(text = first.strftime("%A"))

        second = first + timedelta(days = 1)
        day2.config(text = second.strftime("%A"))

        third = first + timedelta(days = 2)
        day3.config(text = third.strftime("%A"))

        fourth = first + timedelta(days = 3)
        day4.config(text = fourth.strftime("%A"))

        fifth = first + timedelta(days = 4)
        day5.config(text = fifth.strftime("%A"))

        sixth = first + timedelta(days = 5)
        day6.config(text = sixth.strftime("%A"))

        seven = first + timedelta(days = 6)
        day7.config(text = seven.strftime("%A"))
    
    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")

#Background Image
bg = PhotoImage(file = "bg1.png")
label = Label(root,image=bg)
label.place(x=0,y=0)

#Icon
rect = PhotoImage(file = "index.png")
label = Label(root,image=rect)
label.place(x=48,y=95)

label1 = Label(root,text="Temperature",font=('Helvetica',11),fg="white",bg="black")
label1.place(x=50,y=120)
label2 = Label(root,text="Humidity",font=('Helvetica',11),fg="white",bg="black")
label2.place(x=50,y=140)
label3 = Label(root,text="Pressure",font=('Helvetica',11),fg="white",bg="black")
label3.place(x=50,y=160)
label4 = Label(root,text="Wind Speed",font=('Helvetica',11),fg="white",bg="black")
label4.place(x=50,y=180)
label5 = Label(root,text="Description",font=('Helvetica',11),fg="white",bg="black")
label5.place(x=50,y=200)

#Search Bar
search = PhotoImage(file = "search.png")
label = Label(root,image = search)
label.place(x = 300, y = 150)

cloud = PhotoImage(file = "cloud.png")
label1 = Label(root,image = cloud, bg = "black")
label1.place(x = 305, y = 153)

text = tk.Entry(root,justify = 'center',width = 30,font = ('poppins',10,'bold'),border = 0,fg = "white", bg = "black")
text.place(x = 370,y = 160)
text.focus()

search_icon = PhotoImage(file = "search_icon.png")
icon = Button(image=search_icon,borderwidth=0,cursor="hand2",command = getWeather)
icon.place(x = 670, y = 155)

#Bottom Part
frame = Frame(root,width = 900,height = 170,bg = "black")
frame.pack(side = BOTTOM)

#Bottom Boxes
first = PhotoImage(file = "triangle.png")
second = PhotoImage(file = "rec1.png")

Label(frame,image = first, bg = "black").place(x = 30,y = 20)
Label(frame,image = second, bg = "black").place(x = 300,y = 10)
Label(frame,image = second, bg = "black").place(x = 400,y = 10)
Label(frame,image = second, bg = "black").place(x = 500,y = 10)
Label(frame,image = second, bg = "black").place(x = 600,y = 10)
Label(frame,image = second, bg = "black").place(x = 700,y = 10)
Label(frame,image = second, bg = "black").place(x = 800,y = 10)

#Clock
clock = Label(root,font = ("Helvetica",30,'bold'),fg = "red",bg = "peachpuff2")
clock.place(x = 30,y = 20)

#Timezone
timezone = Label(root,font = ("Helvetica",20),fg = "red", bg = "lightblue")
timezone.place(x = 650,y = 20)

long_lat = Label(root,font = ("Helvetica",10),fg = "red", bg = "lightblue")
long_lat.place(x = 650,y = 50)

#thpwd
t = Label(root,font=('Helvetica',11),fg="white",bg="black")
t.place(x=140,y=120)
h = Label(root,font=('Helvetica',11),fg="white",bg="black")
h.place(x=140,y=140)
p = Label(root,font=('Helvetica',11),fg="white",bg="black")
p.place(x=140,y=160)
s = Label(root,font=('Helvetica',11),fg="white",bg="black")
s.place(x=140,y=180)
d = Label(root,font=('Helvetica',11),fg="white",bg="black")
d.place(x=140,y=200)

#First Cell
f = Frame(root,width = 230,height = 132,bg = "olivedrab1")
f.place(x = 30,y = 390)
day1 = Label(f,font = "arial 20",bg = "olivedrab1",fg = "red")
day1.place(x = 100, y = 5)
firstimg = Label(f,bg = "olivedrab1")
firstimg.place(x = 1,y = 15)
day1temp = Label(f,bg = "olivedrab1",font = "arial 15 bold",fg = "red")
day1temp.place(x = 100,y = 50)

#Second Cell
sec = Frame(root,width = 78,height = 122,bg = "olivedrab1")
sec.place(x = 310,y = 395)
day2 = Label(sec,bg = "olivedrab1",fg = "red")
day2.place(x = 10, y = 5)
secimg = Label(sec,bg = "olivedrab1")
secimg.place(x = 7,y = 25)
day2temp = Label(sec,bg = "olivedrab1",fg= "red")
day2temp.place(x = 10,y = 70)

#Third Cell
third = Frame(root,width = 78,height = 122,bg = "olivedrab1")
third.place(x = 410,y = 395)
day3 = Label(third,bg = "olivedrab1",fg = "red")
day3.place(x = 0, y = 5)
thirdimg = Label(third,bg = "olivedrab1")
thirdimg.place(x = 7,y = 25)
day3temp = Label(third,bg = "olivedrab1",fg= "red")
day3temp.place(x = 10,y = 70)

#Fourth Cell
fourth = Frame(root,width = 78,height = 122,bg = "olivedrab1")
fourth.place(x = 510,y = 395)
day4 = Label(fourth,bg = "olivedrab1",fg = "red")
day4.place(x = 10, y = 5)
fourthimg = Label(fourth,bg = "olivedrab1")
fourthimg.place(x = 7,y = 25)
day4temp = Label(fourth,bg = "olivedrab1",fg= "red")
day4temp.place(x = 10,y = 70)

#Fifth Cell
fifth = Frame(root,width = 78,height = 122,bg = "olivedrab1")
fifth.place(x = 610,y = 395)
day5 = Label(fifth,bg = "olivedrab1",fg = "red")
day5.place(x = 13, y = 5)
fifthimg = Label(fifth,bg = "olivedrab1")
fifthimg.place(x = 7,y = 25)
day5temp = Label(fifth,bg = "olivedrab1",fg= "red")
day5temp.place(x = 10,y = 70)

#Sixth Cell
sixth = Frame(root,width = 78,height = 122,bg = "olivedrab1")
sixth.place(x = 710,y = 395)
day6 = Label(sixth,bg = "olivedrab1",fg = "red")
day6.place(x = 10, y = 5)
sixthimg = Label(sixth,bg = "olivedrab1")
sixthimg.place(x = 7,y = 25)
day6temp = Label(sixth,bg = "olivedrab1",fg= "red")
day6temp.place(x = 10,y = 70)

#Seventh Cell
seven = Frame(root,width = 78,height = 122,bg = "olivedrab1")
seven.place(x = 810,y = 395)
day7 = Label(seven,bg = "olivedrab1",fg = "red")
day7.place(x = 10, y = 5)
sevenimg = Label(seven,bg = "olivedrab1")
sevenimg.place(x = 7,y = 25)
day7temp = Label(seven,bg = "olivedrab1",fg= "red")
day7temp.place(x = 10,y = 70)


root.mainloop()