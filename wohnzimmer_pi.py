from tkinter import *
root = Tk()
root.wm_title("Wohnzimmer Wetterstation")
root.config(background = "#FFFFFF")
text_frame = Text(root, height=4, width = 20, font = 'courier 48')
text_frame.insert(END, "Temperatur")
text_frame.pack()

root.mainloop()
