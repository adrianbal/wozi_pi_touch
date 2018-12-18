from Tkinter import *
import time
import random
import sys
import bme680
def quit_program():
    sys.exit()
# Bosch Sensor 
sensor = bme680.BME680(bme680.I2C_ADDR_PRIMARY)
sensor.set_humidity_oversample(bme680.OS_2X)
sensor.set_pressure_oversample(bme680.OS_4X)
sensor.set_temperature_oversample(bme680.OS_8X)
sensor.set_filter(bme680.FILTER_SIZE_3)

root = Tk()
root.attributes('-fullscreen', True)
root.geometry('800x480')
root.configure(background='black')
time1 = ''

clock = Label(root, font=('arial', 82, 'bold'), bg='black', fg="blue")
clock.pack(side=TOP, fill=BOTH)

quitButton = Button(text="Quit", command=quit_program)
quitButton.pack(side = BOTTOM)

temp_display = Label(root, font=('arial', 42, 'bold'), bg='black', fg="green")
temp_display.pack(side= BOTTOM, fill=BOTH)

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
    sensor.get_sensor_data()
    output = '{0:.1f} C {1:.1f} hPa {2:.1f} %RH'.format(
                sensor.data.temperature,
                sensor.data.pressure,
                sensor.data.humidity)
    temp_display.config(text=output)
    temp_display.after(4000, get_temp_value)

tick()
get_temp_value()
root.mainloop()


