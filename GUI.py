from tkinter import *
from pytube import *

#window = Tk("YouTube Download")



'''
user_in = StringVar()
def ytsearch():
    print (user_in.get())
   # t1.insert(CENTER, user_in.get())

b1 = Button(window, text = "Search" ,command = ytsearch())
b1.grid(row = 10, column = 10)

t1 = Entry(window, textvariable= user_in)
t1.grid(row = 10, column = 3)


t1 = Text (window, height = 15, width = 30)
t1.grid(row = 3, column = 25)
'''
from pytube import YouTube

yt = YouTube(str(input("Enter the video link: ")))
videos = yt.streams.all()

s = 1
for v in videos:
    print(str(s)+". "+str(v))
    s += 1

n = int(input("Enter the number of the video: "))
vid = videos[n-1]

destination = str(input("Enter the destination: "))
vid.download(destination)

print(yt.filename+"\nHas been successfully downloaded")


#window.mainloop()

##added thru git

