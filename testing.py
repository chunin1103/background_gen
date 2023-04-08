import os
import random
import ctypes
import time
from PIL import Image

def set_wallpaper(image_path):
    """Set the desktop wallpaper to the image at the given path"""
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, 0)

def main():
    # Set the folder path containing the images
    folder_path = "C:/MS Background"

    # Get a list of all the image files in the folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) 
                   if os.path.isfile(os.path.join(folder_path, f)) and 
                   f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

    # Loop through the images, setting each as the desktop wallpaper for a few seconds
    while True:
        image_path = random.choice(image_files)
        set_wallpaper(image_path)
        time.sleep(1000) # Change wallpaper every 10 seconds

if __name__ == "__main__":
    main()
