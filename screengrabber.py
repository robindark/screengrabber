import os
import time
from PIL import Image as im
import mss
import numpy as np

if __name__ == "__main__":

    with mss.mss() as sct:

        image_format = ".gif"
        picture_counter = 0
        max_pictures = 5
        sleep_time_secs = 2

        # information of monitor
        monitor_number = 1
        mon = sct.monitors[monitor_number]

        # screen part to capture
        width = 1920
        height = 1080

        # this setting takes a centered screenshot
        # (if captured resolution < screen resolution)
        monitor = {
            "top": mon["top"] + int((mon["height"] - height) / 2),
            "left": mon["left"] + int((mon["width"] - width) / 2),
            "width": width,
            "height": height,
            "mon": monitor_number,
        }

        while True:
            sct_img = sct.grab(monitor)

            image_resized = im.frombytes(
                "RGB", sct_img.size, sct_img.bgra, "raw", "BGRX"
            )
            image_resized.save(
                "\\\mfs\mfs\kodi-sync\infoscreens\screen"
                + str(picture_counter)
                + image_format
            )

            try:
                os.remove(
                    "\\\mfs\mfs\kodi-sync\infoscreens\screen"
                    + str(5 - picture_counter)
                    + image_format
                )
            except:
                pass

            picture_counter = picture_counter + 1

            if picture_counter > max_pictures:
                picture_counter = 0

            time.sleep(sleep_time_secs)
