# pip install pillow
import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os


def upload_and_watermark():   # Function to upload and print watermark on image
    # Manually specify the input image file
    input_image = "input_image/image.jpg"

    # Open the input image
    img = Image.open(input_image)

    # Add watermark
    draw = ImageDraw.Draw(img)
    text = "github: f-Odt"
    font = ImageFont.truetype('FreeSans.ttf', 60)

    # Calculate the position for the text
    text_width, text_height = draw.textbbox((0,0), text, font=font)[2:]
    img_width, img_height = img.size
    position = (img_width - text_width - 10, img_height - text_height - 10)
    draw.text(position, text, font=font)

    # Save the output image to the "finished" directory
    output_dir = "output_image"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_image = os.path.join(output_dir, "watermarked_image.jpg")
    img.save(output_image)

    # Close window after operation
    window.destroy()


window = tk.Tk()
window.geometry("300x250")
button = tk.Button(window, text="Upload Image", command=upload_and_watermark)
button.pack()
window.mainloop()
