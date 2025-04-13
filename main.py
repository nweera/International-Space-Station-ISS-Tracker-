import json
import turtle
import urllib.request
import webbrowser
import geocoder
import time

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url) 
result = json.loads(response.read()) #read response brought from api
file = open("iss.txt", "w") #open file to write
file.write("there are currently " + str(result["number"]) + " astrounauts in the ISS\n") #write number of people in space
people = result["people"] #get people in space
for person in people: #for each person in space
    file.write(person["name"] + " is on board the ISS\n") #write name of each person in space
g =geocoder.ip("me") #get geolocation of the user
file.write("your location is " + str(g.latlng) + "\n") #write user location
file.close() #close file
webbrowser.open("iss.txt") #open file in browser

#setup the world map in turtle module

screen = turtle.Screen() #create screen
screen.setup(1280,720) #set screen size
screen.setworldcoordinates(-180,-90,180,90) #set world coordinates
screen.title("ISS Location") #set screen title

#load the world map
try:
    screen.bgpic("map.gif")
except turtle.TurtleGraphicsError:
    print("Error: Unable to load 'map.gif'. Please check the file path and format.")
screen.register_shape("iss.gif") #load iss image
iss = turtle.Turtle() #create turtle object
iss.shape("iss.gif") #set iss image as shape
iss.setheading(45) #set heading of iss image
iss.penup() #lift pen up

input("stop")

while True: #infinite loop
    #load the current status of the iss
    url = "http://api.open-notify.org/iss-now.json" #url for iss location
    response = urllib.request.urlopen(url) #open url
    result = json.loads(response.read()) #read response brought from api

    #extract the latitude and longitude of the iss
    lat = float(result["iss_position"]["latitude"]) #get latitude
    long = float(result["iss_position"]["longitude"]) #get longitude

    #output the latitude and longitude of the iss
    lat= float(lat) 
    long = float(long)
    print("latitude: " + str(lat)) #print latitude
    print("longitude: " + str(long)) #print longitude

    # update the iss position on the map
    iss.goto(long, lat) #goto the iss position

    #refrech each 3 seconds
    time.sleep(3) #wait for 3 seconds