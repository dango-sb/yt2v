import tkinter as tk
from tkinter import ttk
from pytube import YouTube

save_path = 'D:\Music'

# window
root = tk.Tk()
root.title('Download Helper')
root.geometry('500x200')
root.resizable(width=False, height=False)
custom_font = ('Arial', 16)

# Function to download audio
def downloadAudio():
    url = entry.get()
    if ("https://youtu.be/" != url[:17] and "https://www.youtube.com/" != url[:24]):
        log.insert("end", 'False link.\n')
    else:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        audio_stream.download(output_path=save_path)
        original_filename = audio_stream.default_filename
        new_filename = original_filename.replace(".mp4", ".mp3")
        import os
        os.rename(os.path.join(save_path, original_filename), os.path.join(save_path, new_filename))
        log.insert("end", f'Download of {new_filename} is finished successfully.\n')
    entry.delete(0, "end")

# Function to download video
def downloadVideo():
    url = entry.get()
    if ("https://youtu.be/" != url[:17] and "https://www.youtube.com/" != url[:24]):
        log.insert("end", 'False link.\n')
    else:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        audio_stream.download(output_path=save_path)
        log.insert("end", f'Download of {audio_stream.default_filename} is finished successfully.\n')

    entry.delete(0, "end")

# Function to switch to audio download
def changeToAudio():
    downloadButton['command'] = downloadAudio
    formatLabel.config(text='Audio')

# Function to switch to video download
def changeToVideo():
    downloadButton['command'] = downloadVideo
    formatLabel.config(text='Video')

# Widgets
frame = tk.Frame(root, padx=3, pady=3)  # Create a frame with padx and pady
entry = tk.Entry(frame)
downloadButton = ttk.Button(frame, text="Download", command=downloadAudio)
log = tk.Text(root, width=40, height=10, padx=5)
formatLabel = ttk.Label(text='Audio', font=custom_font)

# Menu
menubar = tk.Menu(root)
formatSub = tk.Menu(menubar, tearoff=False)
formatSub.add_command(label='Audio', command=changeToAudio)
formatSub.add_command(label='Video', command=changeToVideo)
menubar.add_cascade(label='Format', menu=formatSub)

# Configure grid layout
root.columnconfigure((0, 1), weight=1)
root.rowconfigure((0, 1, 2, 3), weight=1)

# Place widgets
frame.grid(row=1, column=0)
formatLabel.grid(row=0, column=0)
entry.grid(row=1, column=0, sticky='wes')
downloadButton.grid(row=2, column=0, sticky='n')
log.grid(row=0, column=1, rowspan=4)

# Run
root.config(menu=menubar)
root.mainloop()