from tkinter import *

window = Tk()
window.title("Watermarking app")
window.minsize(650, 400)


label = Label(text="Select the image that you want to watermark", font=("Helvetica", 14))
label.grid(column=0, row=0, pady=5)

button = Button(text="Select Image")
button.grid(column=1, row=0, pady=5)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.mainloop()
