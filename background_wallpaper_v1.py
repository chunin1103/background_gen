import tkinter as tk
import replicate
import requests
from io import BytesIO
from PIL import Image
import ctypes
import os
import time
import tempfile
import time

# Define the WallpaperApp class for the user interface
class WallpaperApp:
    def __init__(self, master):
        self.master = master
        master.title("Wallpaper Generator")

        # Create the prompt label and entry box        
        self.prompt_label = tk.Label(master, text="Enter your prompt:", font=("Helvetica", 14))
        self.prompt_label.pack(pady=20)

        self.prompt_entry = tk.Entry(master, font=("Helvetica", 16), width=40, bd=2, relief=tk.SOLID)
        self.prompt_entry.pack(ipady=10)

        # Create the interval label and entry box
        self.interval_label = tk.Label(master, text="Enter time interval (minutes):", font=("Helvetica", 14))
        self.interval_label.pack(pady=20)

        self.interval_entry = tk.Entry(master, font=("Helvetica", 16), width=10, bd=2, relief=tk.SOLID)
        self.interval_entry.pack(ipady=10)

        # Create the submit button and attach the command to start the wallpaper change process
        self.submit_button = tk.Button(master, text="Submit", font=("Helvetica", 14), bg="#2ecc71", fg="white", bd=0,
                                       command=self.start_wallpaper_change)
        self.submit_button.pack(pady=20, ipadx=10, ipady=5)

    # Function to start changing the wallpaper based on the user's input
    def start_wallpaper_change(self):
        prompt = self.prompt_entry.get()
        interval = int(self.interval_entry.get()) * 60  # Convert to seconds
        while True:
            set_wallpaper_from_prompt(prompt)
            time.sleep(interval)

# Function to call the image generation API with the user's prompt
def call_image_api(prompt):
    output = replicate.run(
        "tstramer/midjourney-diffusion:436b051ebd8f68d23e83d22de5e198e0995357afef113768c20f0b6fcef23c8b",
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 512,
            "scheduler": "K_EULER",
            "num_outputs": 1,
            "prompt_strength": 0.8,
        }
    )
    print("Output:", output) 
    # Output sample: ['https://replicate.delivery/pbxt/EbV9qcxCuBKFKVT3u9pGr2pYu00bnuIss31SKe2vTHnKivXIA/out-0.png']
    return output[0]          


# Function to set the wallpaper using the given image URL
def set_wallpaper(image_url):
    SPI_SETDESKWALLPAPER = 20

    # Download the image and save it to a temporary file
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    # Save the image locally for debugging purposes
    image.save("debug_image.png", "PNG")

    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        temp_filename = f.name
        image.save(f, "PNG")
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, temp_filename, 0)

    # Print the temporary file path and comment out the line to delete the temporary file
    print("Temporary file path:", temp_filename)
    time.sleep(2)  # Wait for 2 seconds before deleting the temporary file
    os.remove(temp_filename)  # Remove the temporary file


# Function to generate and set the wallpaper based on the given prompt
def set_wallpaper_from_prompt(prompt):
    image_url = call_image_api(prompt)
    set_wallpaper(image_url)

if __name__ == "__main__":
    root = tk.Tk()
    app = WallpaperApp(root)
    root.geometry("500x350")
    root.resizable(0, 0)
    root.mainloop()