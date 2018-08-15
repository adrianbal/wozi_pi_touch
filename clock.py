from Tkinter import *
import time
import random
import sys
def quit_program():
    sys.exit() 
root = Tk()
root.geometry('800x480')
time1 = ''
clock = Label(root, font=('arial', 60, 'bold'), bg='black', fg="blue")
clock.pack(fill=BOTH)
temp_display = Label(root, font=('arial', 42, 'bold'), bg='white', fg="blue")
humidity_display = Label(root, font=('arial', 42, 'bold'), bg='white', fg="blue")
baro_display = Label(root, font=('arial', 42, 'bold'), bg='white', fg="blue")
temp_display.pack(side= LEFT)
humidity_display.pack(side = RIGHT)
baro_display.pack(side = LEFT)
quitButton = Button(text="Quit", command=quit_program)
quitButton.pack(side = LEFT)
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
       time1 = time2
       clock.config(text=time2)
        # calls itself every 200 milliseconds
        # to update the time display as needed
        # could use >200 ms, but display gets jerky
    clock.after(200, tick)
def get_temp_value():
    temp_value = random.randrange(0,101,2)
    temp_display.config(text=temp_value)
    temp_display.after(2000, get_temp_value)
def get_humidity_value():
    humidity_value = random.randrange(0,101,2)
    humidity_display.config(text=humidity_value)
    humidity_display.after(2000, get_humidity_value)

tick()
get_temp_value()
get_humidity_value()
root.mainloop()


