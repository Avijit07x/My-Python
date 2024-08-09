import tkinter as tk
from pytube import YouTube
import customtkinter

def startDownload(option):
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        if option == "hq":
            video = ytObject.streams.get_highest_resolution()
        elif option == "lq":
            video = ytObject.streams.get_lowest_resolution()
        elif option == "audio":
            video = ytObject.streams.get_audio_only()
        else:
            return

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download('E:\Yt Videos')
        finishLabel.configure(text="Downloaded !!", text_color="Yellow")
    except:
        finishLabel.configure(text="Download Error", text_color="red")


def on_progress(stream, a, bytes_remaining):
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    perecentage_of_completion = bytes_download / total_size * 100
    per = str(int(perecentage_of_completion))
    progress.configure(text=per + '%')
    progress.update()

    # Update ProgressBar
    progressbar.set(float(perecentage_of_completion) / 100)


# System settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# window frame

window = customtkinter.CTk()
window.geometry("720x480")
window.title("Youtube Video Downloader")

# icon
window.iconbitmap("d:\icon\youtube_logo_icon_147199.ico")


# Ui
title = customtkinter.CTkLabel(window,
                               text="Insert a YouTube Link",
                               width=200,
                               height=50,
                               font=("cursive", 26))
title.pack(padx=10, pady=10)

# Link Input
url_var = tk.StringVar()
link = customtkinter.CTkEntry(window,
                              width=350,
                              height=40,
                              textvariable=url_var)
link.pack()


# Finished Downloading
finishLabel = customtkinter.CTkLabel(window, text="")
finishLabel.pack()

# Progress Percentage
progress = customtkinter.CTkLabel(window, text="0%")
progress.pack()

progressbar = customtkinter.CTkProgressBar(window, width=400)
progressbar.set(0)
progressbar.pack(padx=10, pady=10)


# HQ Video Button
download_hq = customtkinter.CTkButton(window,
                                      text="Download High Quality-Mp4",
                                      command=lambda: startDownload("hq"))
download_hq.pack(padx=10, pady=10)

# LQ Video Button
download_lq = customtkinter.CTkButton(window,
                                      text="Download Low Quality-Mp4",
                                      command=lambda: startDownload("lq"))
download_lq.pack(padx=10, pady=10)

# Audio Button
download_a = customtkinter.CTkButton(window,
                                     text="Download Mp3",
                                     command=lambda: startDownload("audio"))
download_a.pack(padx=10, pady=10)

# creator
# crt = customtkinter.CTkLabel(window,
#                              text="Made By Avijit Dey",
#                              anchor="se", font=("anka", 10))
# crt.pack(side="bottom", fill="both")


# Run window
window.mainloop()
