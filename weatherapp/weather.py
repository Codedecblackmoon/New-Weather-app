import requests
import tkinter
import datetime
from tkinter import messagebox
from PIL import Image, ImageTk  

def weather_data(event=None):
    city_name = textfilde.get()
    
    if city_name == "Search your city":
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    api_url = "http://api.openweathermap.org/data/2.5/weather?"
    key = '7f628240c7ecf2c3259ea4a64034d24a'
    url = api_url + "appid=" + key + "&q=" + city_name

    data = requests.get(url).json()
    
    try:    
        condition = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = int(data['main']['temp'] - 273.15)
        temp_max = int(data['main']['temp_max'] - 273.15)
        temp_min = int(data['main']['temp_min'] - 273.15)
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        day, date, time = Time()
            
        final_info = condition + "\n" + str(temp) + "°C"
        final_data = "\n" + "Max_temp: "+str(temp_max) + "         Min_temp: "+str(temp_min)+"\n" + "Humidity: "+str(humidity)+"         Wind: "+str(wind)
        final_date = str(day)+"  "+str(date[0])+"  "+str(time[0])
        label1.config(text=final_info)
        icon_path = './weatherapp/weather_icons/{}.png'.format(icon)
        weather_icon = Image.open(icon_path)
        weather_icon = ImageTk.PhotoImage(weather_icon)
        image.config(image=weather_icon)
        image.image = weather_icon 
        label2.config(text=final_data)
        label.config(text=final_date)
    except:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city_name))

def Time():
    info = datetime.datetime.now()
    date = str(info).split()
    start_datetime = datetime.datetime.strptime(str(info), '%Y-%m-%d %H:%M:%S.%f')
    day = start_datetime.strftime('%A')
    time = date[1].split(".")
    return day, date , time

def on_focus_in(event):
    if textfilde.get() == "Search your city":
        textfilde.delete(0, tkinter.END)
        textfilde.config(fg="black")

def on_focus_out(event):
    if not textfilde.get():
        textfilde.insert(0, "Search your city")
        textfilde.config(fg="gray")
    
    
window = tkinter.Tk()
window.geometry("700x600") 
window.title("Weather App")
window.config(bg='#050049')

f = ("popping", 15, "bold")
t = ("popping", 35, "bold")
j = ("popping", 10, "bold")

textfilde = tkinter.Entry(window, justify="center", font=t)
textfilde.insert(0, "Search your city")  # Add placeholder text
textfilde.bind('<FocusIn>', on_focus_in)
textfilde.bind('<FocusOut>', on_focus_out)
textfilde.pack(pady=20)
textfilde.focus()
textfilde.bind('<Return>', weather_data)

# label = tkinter.Label(window, font=j)
# label.pack()
# label1 = tkinter.Label(window, font=t)
# label1.pack()
# image = tkinter.Label(window)
# image.pack()
# label2 = tkinter.Label(window, font=f)
# label2.pack()

label = tkinter.Label(window, font=j, bg='#050049', fg='white')  # Label background color
label.pack()
label1 = tkinter.Label(window, font=t, bg='#050049', fg='white')  # Label background color
label1.pack()
image = tkinter.Label(window, bg='#050049')  # Image label background color
image.pack()
label2 = tkinter.Label(window, font=f, bg='#050049', fg='white')  # Label background color
label2.pack()

if __name__ == "__main__":
    window.mainloop()