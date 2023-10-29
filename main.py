import tkinter as tk
from tkinter import ttk
from pytube import YouTube
import os

# create savepath file
savepath = open("savepath.txt", 'a+')
savepath_video=savepath.readline()
savepath_audio=savepath.readline()

if savepath_video == '':
    os.system("mkdir Video")
    savepath_video= os.getcwd() + '\Video'
    savepath.write(savepath_video)
    
if savepath_audio == '':
    os.system("mkdir Audio")
    savepath_audio= os.getcwd() + '\Audio'
    savepath.write(savepath_audio)
    
savepath.close()

# window
root = tk.Tk()
root.title('YT2V')
root.geometry('200x200')
root.resizable(width=False, height=False)
custom_font = ('Arial', 16)

#  Assistant functions
# TODO Error if path is incorrect in savepath.txt

def existsErr(file_path):
    if os.path.exists(file_path):
        log.configure(text="This file already exists.")
        return True
    else:
        return False
    
def validLink(url):
    return ("https://youtu.be/" != url[:17] and "https://www.youtube.com/" != url[:24])

# Function to download video 
def downloadAudio():
    url = entry.get()
    if validLink(url):
        log.configure(text='False link.')
    else:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        original_filename = audio_stream.default_filename
        
        import os
        if existsErr(os.path.join(savepath_audio, original_filename)):
            return
        
        audio_stream.download(output_path=savepath_audio)
        new_filename = original_filename.replace(".mp4", ".mp3")
        
        os.rename(os.path.join(savepath_audio, original_filename), os.path.join(savepath_audio, new_filename))
        log.configure(text = f'Download of {new_filename} is finished successfully.')
    entry.delete(0, "end")

# Function to download video
def downloadVideo():
    url = entry.get()
    if validLink(url):
        log.configure(text = "False link.")
    else:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True, file_extension="mp4").first()
        original_filename = audio_stream.default_filename
        
        import os
        if existsErr(os.path.join(savepath_audio, original_filename)):
            return
        
        audio_stream.download(output_path=savepath_video)
        log.configure(text = f'Download of {audio_stream.default_filename} is finished successfully.')
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
log = ttk.Label(root, wraplength=200)
formatLabel = ttk.Label(text='Format???', font=custom_font)

# Menu
menubar = tk.Menu(root)
formatSub = tk.Menu(menubar, tearoff=False)
formatSub.add_command(label='Audio', command=changeToAudio)
formatSub.add_command(label='Video', command=changeToVideo)
menubar.add_cascade(label='Format', menu=formatSub)

# Configure grid layout
root.columnconfigure((0), weight=1)
root.rowconfigure((0, 1, 2), weight=1)

# Place widgets
frame.grid(row=1, column=0)
formatLabel.grid(row=0, column=0)
entry.grid(row=1, column=0, sticky='wes')
downloadButton.grid(row=2, column=0, sticky='n')
log.grid(row=3, column=0, sticky='wne')

# Run
root.config(menu=menubar)
root.mainloop()