from os import path
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


# funtion
def select_path():
    # allow user to select path
    path = filedialog.askdirectory()
    path__label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get select path
    user_path = path__label.cget("text")
    screen.title('Downloading....')

    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()

    # move file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete...')


screen = Tk()
tittle = screen.title('Youtube Downloader (by Asif EFX )')
Canvas = Canvas(screen, width=500, height=500)

Canvas.pack()

# image logo
logo_img = PhotoImage(file='yt.png')
# resize
logo_img = logo_img.subsample(22, 22)
Canvas.create_image(250, 80, image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Download link url : ", font=('Arial', 15))

# select path for saving the file
path__label = Label(screen, text="Select path for download", font=('Arial', 15))
select_btn = Button(screen, text="Select", command=select_path)

# add to window
Canvas.create_window(250, 280, window=path__label)
Canvas.create_window(250, 330, window=select_btn)

# Add widget to window
Canvas.create_window(250, 170, window=link_label)
Canvas.create_window(250, 220, window=link_field)

# Download button
download_btn = Button(screen, text="Download file", command=download_file)
# add to canvas
Canvas.create_window(250, 390, window=download_btn)

screen.mainloop()
