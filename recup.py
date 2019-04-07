import urllib.request
from lxml import etree
from FortniteAPI import User
from FortniteAPI import Stats
from FortniteAPI import Stats
from easygui import *
from tkinter import *
 


window = Tk()
 
#print(user.username) # Prints user's username
#print(user.platforms) # Prints user's available platforms
#print(user.seasons) # Prints user's seasons
#print(stats.controller.overall.kd)
#print(stats.controller.overall.kills)
#print(stats.controller.overall.deaths)

window.title("Fortnite_Tracker")

print ("enterbox()")


user = User(enterbox())
stats = Stats(user.id)	
u = (user.username)
p = (user.platforms)
s = (user.seasons)
kd = (stats.controller.overall.kd)
k = (stats.controller.overall.kills)
d = (stats.controller.overall.deaths)


nom1 = Label(window, text=u)
nom1.grid(column=0, row=0)

nom2 = Label(window, text=p)
nom2.grid(column=0, row=1)

nom3 = Label(window, text=s)
nom3.grid(column=0, row=2)

nom4 = Label(window, text=kd)
nom4.grid(column=0, row=3)

nom5 = Label(window, text=k)
nom5.grid(column=0, row=4)

nom6 = Label(window, text=d)
nom6.grid(column=0, row=5)	

window.mainloop()

#api = open("userid.txt","w")
#api.write(user.id)
#api.close()




