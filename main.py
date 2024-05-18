from tkinter import Tk, Label, Button, filedialog, simpledialog
from PIL import Image, ImageTk, ImageFont, ImageDraw

pos = (0, 0)
fill = (93, 93, 93)


def open_save_file():

    filename = filedialog.askopenfilename(title='Chose an image', filetypes=[('Image Files', '*jpeg *jpg *png')])
    if len(filename) == 0:
        pass
    else:
        img = Image.open(filename)

        text = provide_text()
        if len(text) == 0:
            text = "I'm watermark!"

        w, h = img.size
        if h > 638:
            resize_val = h / 638
            h = h / resize_val
            w = w / resize_val
        if w > 1296:
            resize_val = w / 1296
            h = h / resize_val
            w = w / resize_val
        img = img.resize((round(w), round(h)))

        drawing = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial.ttf", 14)
        drawing.text(pos, text, fill=fill, font=font)

        img.save(f"watermarked_{filename.split('/')[-1]}")

        img = ImageTk.PhotoImage(img)
        label_img = Label(window, image=img)
        label_img.image = img
        label_img.grid(row=2, column=0, columnspan=3, pady=10)


def provide_text():
    text = simpledialog.askstring(title="Watermark text", prompt="What text do you want to put on you image?:")
    return text


window = Tk()
window.title("Watermarking app")
window.minsize(650, 400)

label = Label(text="Select the image that you want to watermark", font=("Helvetica", 14))
label.grid(column=0, row=0, pady=5)

button = Button(text="Select Image", command=open_save_file)
button.grid(column=1, row=0, pady=5)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.mainloop()
