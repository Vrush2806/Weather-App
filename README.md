# Weather-App using Tkinter Python

One can find weather report such as temperature, wind speed, humidity, pressure, description, etc. of each and every place in the world. You only need to provide name of the city in the user-friendly GUI. 

The App is created using Weather API. Application Programming Interfaces (API) provides access to current & historical data of weather on global scale. The API used is OpenWeatherMap.

Link-https://openweathermap.org/api

The icons used to depict the weather conditions can be downloaded from https://openweathermap.org/weather-conditions

### App Working

The app takes city as the input & converts it to latitude & longitude. It then converts latitude-longitude to timezone. 

Using the latitude-longitude we acquire the weather data from OpenWeatherMap API.

Syntax-https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}

First, sign-in the API & subscribe to the API which you like. After sign-in the API will generate a unique API key for its users; use it in the above syntax.

You can use any parameter you want to display from the API data like humidity, temperature, description, etc. 

The App displays whole week forecast of the required destination. Also, the app gives error message if wrong destination is entered.

### Required Modules

1.  Tkinter
2.  Pytz
3.  Geopy
4.  Timezonefinder
5.  Requests
6.  Pillow
7.  Datetime

### Screenshots


![Screenshot from 2022-09-26 18-01-46](https://user-images.githubusercontent.com/68546263/192298000-5a056717-aa50-4bed-a823-c83224193803.png)

![Screenshot from 2022-09-26 18-02-47](https://user-images.githubusercontent.com/68546263/192298010-f514ec7c-dffc-437e-9d96-82626f66e8b8.png)


