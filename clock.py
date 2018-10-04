from Tkinter import *
import time
import Adafruit_DHT
root = Tk()
root.attributes('-fullscreen', True)
root.geometry('800x600')
time1 = ''
humidity = 0
temperatur = 0
clock = Label(root, font=('courier', 64, 'bold'), bg='black', fg="blue")
clock.pack(fill=BOTH, expand=1)
sensor_text = Text(root, height=4, width=18, font='courierbold 42', background="#000000", fg="white")
sensor_text.insert(END, "T: \n")
sensor_text.insert(END, "H: \n")
sensor_text.insert(END, "B: \n")
sensor_text.pack(fill=BOTH, expand=1)
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
def read_sensor():
    global temperatur, humidity
    humidity, temperatur = Adafruit_DHT_read(Adafruit_DHT22, 4)
    sensor_text.insert(END, "T: %s\n" % temperatur)
    sensor_text.insert(END, "H: %s \n" % humidity)
    

tick()
root.mainloop()
