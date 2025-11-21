# API for astro-info: "http://api.open-notify.org/astros.json"
# API for iss location: "http://api.open-notify.org/iss-now.json"


import turtle #for making shapes and graphics
import time #for importing time related information
import webbrowser #for opening in webbrowser
import json #for acessing data in json format
import urllib #for accessing api urls
import requests #for making http requests
import geocoder #for accessing latitude and longitude of the user and satellite

'''#Importing astronaut info
astro_url = "http://api.open-notify.org/astros.json"
astro_info = requests.get(astro_url)
astro_data = astro_info.json()

#storing the astronaut data into a new file called astro.txt
file = open("astro.txt", "w")
file.write("The numbers of astronauts currently in space are:" + str(astro_data['number']) + '\n')
file.write('The current astronauts are:' + '\n')

#looping through the data to get the names of astronauts
astronauts = astro_data['people']
for person in astronauts:
    file.write(str(person['name']) + ' ' + 'on board: ' + person['craft'] + '\n')

#accessing the current location of the user and writing in txt file
user_location = geocoder.ip('me')
file.write('Current location of the user is: ' + str(user_location.latlng) + '\n')
file.close()
webbrowser.open('astro.txt') '''

#creating a turtle screen
screen = turtle.Screen()
screen.setup(1080, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

#setting Background as world map
screen.bgpic(r'D:\Python-Codes\Astronomy\iss_tracker\ezgif.com-resize (1).gif')

#iss icon
screen.register_shape(r'D:\Python-Codes\Astronomy\iss_tracker\iss-icon.gif')
iss = turtle.Turtle()
iss.shape(r'D:\Python-Codes\Astronomy\iss_tracker\iss-icon.gif')
iss.setheading(45)
iss.penup()

screen.title("ISS Tracker")

#starting the tracker
#accessing iss location and running the graphics

def update_iss():
    response = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    lat = response["latitude"]
    lon = response["longitude"]

    #x = lon * (screen.window_width() / 360)
    #y = lat * (screen.window_height() / 180)
    iss.goto(lon, lat)

    screen.ontimer(update_iss, 5000)  # call again after 7 seconds

update_iss()
turtle.mainloop()
