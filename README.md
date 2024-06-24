This script is designed to add a watermark to an image using the Pillow library.

Usage:

1. Install the required library by running `pip install pillow` in your terminal.
2. Place the image you want to watermark in the `input_image` directory.
3. Run the script by executing the Python file.
4. Click the "Upload Image" button to add the watermark to the image.
5. The watermarked image will be saved in the `output_image` directory.

Configuration:

* The input image file is currently set to `input_image/image.jpg`. You can change this to match the name and location of your input image.
* The watermark text is currently set to `github: f-Odt`. You can change this to match your desired watermark text.
* The watermark font is currently set to `FreeSans.ttf`. You can change this to match your desired font.

Note:

* This script uses the Pillow library to manipulate images. Make sure you have Pillow installed before running the script.
* The script will create an `output_image` directory if it does not already exist.
* The script will close the window after the watermarking process is complete.
