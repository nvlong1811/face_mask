import tkinter as tk
from tkinter import filedialog
import os
from detect import image_detect, start_video, webcam_detect
import cv2

window = tk.Tk()
window.columnconfigure(0, minsize=300)
window.rowconfigure([0, 3], minsize=100)
window.title("Nhan dien khau trang")

def open_img():
    cv2.destroyAllWindows()
    filename =filedialog.askopenfilename(filetypes=(("image file","*.png"),("image file","*.jpg"),("All files","*.*")))
    image_detect(filename)

def open_video():
    cv2.destroyAllWindows()
    filename =filedialog.askopenfilename(filetypes=(("image file","*.mp4"),("All files","*.*")))
    start_video(filename)

def open_webcam():
    webcam_detect()

read_image = tk.Button(master=window, text="Nhận diện từ hình ảnh", command=open_img)
read_image.grid(row=0, column=0)

read_video = tk.Button(master=window, text="Nhận diện từ video", command=open_video)
read_video.grid(row=1, column=0)

read_webcam = tk.Button(master=window, text="Nhận diện từ camera", command=open_webcam)
read_webcam.grid(row=2, column=0)


window.mainloop()