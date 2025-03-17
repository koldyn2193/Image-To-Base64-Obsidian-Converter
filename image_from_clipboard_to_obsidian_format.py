from PIL import ImageGrab, Image
from io import BytesIO
import base64
import sys 
import pyperclip

def image_from_clipboard_to_obsidian():

    image = ImageGrab.grabclipboard()
    if image is None:
        print("No image in clipboard")

    if type(image) is list:
        image = Image.open(image[0])
    print(image)
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    image_bytes = buffer.getvalue()

    base64_image = base64.b64encode(image_bytes).decode()

    if len(sys.argv) >= 2:
        image_name = " ".join(sys.argv[1:])
    else:
        print("Name the image")
        return
        
    obsidian_image_format = f"![{image_name}](data:image/png;base64,{base64_image})"
    pyperclip.copy(obsidian_image_format)
    print(f"Image '{image_name}' has been converted and sent to clipboard")

if __name__ == "__main__":
    image_from_clipboard_to_obsidian()