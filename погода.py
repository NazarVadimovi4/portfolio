import tkinter as tk
import requests

def get_weather(city):
    api_key = "f9f888956ffdb5832b887e881693b74e"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "404":
        city_name = data["name"]
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        weather_label.place(x=390, y=150)
        weather_label.config(text=f"Погода: {weather}\n\n\nТемпература: {temp}°C\n\n\nВлажность: {humidity}%\n\n\nСкорость ветра: {wind_speed} м/с", font=("Times New Roman", 24,"italic"),bg=root["bg"])
        weat_label = tk.Label(root, text="", font=("Times New Roman",30,"bold", "italic"))
        weat_label.place(x=10, y=290)
        weat_label.config(text=f"Город: {city_name}")


    else:
        weather_label.config(text="Город не найден")



def search():
    city = city_entry.get()
    get_weather(city)

root = tk.Tk()
root.title("Прогноз погоды")
root.geometry("800x600")

# Загрузить изображение фона
bg_image = tk.PhotoImage(file="fon.png")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

city_label = tk.Label(root, text="Введите город:", font=("Helvetica", 24))
city_label.pack()

city_entry = tk.Entry(root, font=("Helvetica", 24))
city_entry.pack()

search_button = tk.Button(root, text="Поиск", command=search, font=("Helvetica", 24))
search_button.pack()

weather_label = tk.Label(root, text="", font=("Helvetica", 24))
weather_label.pack()



root.mainloop()
