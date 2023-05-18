import tkinter as tk
import os
import pydub
from pygame import mixer
import random


canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("400x500")
canvas.config(bg='black')

rootpath = "/home/umanshiva/Desktop/music"
pattern ="*.m4a"
played_song = []

def create_playlist(rootpath):
    music_files = [filename for filename in os.listdir(rootpath) if filename.endswith('.m4a')]
    random.shuffle(music_files)
    return music_files

def convert_to_wav(m4a_file):
    wav_file = os.path.splitext(m4a_file)[0] + '.wav'
    audio = pydub.AudioSegment.from_file(m4a_file)
    audio.export(wav_file, format='wav')
    return wav_file

playlist = create_playlist(rootpath)
    
def play_song(song_path,label):

    label.config(text=f"Now playing: {os.path.basename(song_path)}")
    mixer.init()
    mixer.music.load(song_path)
    mixer.music.play()

def stop_song():
    mixer.init()
    mixer.music.stop()

def play_random_song(rootpath,playlist,played_song,label):

    while(not playlist):
            playlist = create_playlist(rootpath)  
            random.shuffle(playlist)  
            played_songs = []

    random_song = random.choice(playlist)
    playlist.remove(random_song)
    played_song.append(random_song)
    song_path = os.path.join(rootpath,random_song)

    stop_song()
    if song_path.endswith('.m4a'):
        song_path = convert_to_wav(song_path)

    play_song(song_path,label)

    
    

label = tk.Label(canvas,text = '', bg = 'black', fg = 'yellow', font = ('poppins',10) )
label.pack(pady = 20)

playbutton = tk.Button(canvas, text='Play', command = lambda: play_random_song(rootpath,playlist,played_song,label))
playbutton.pack(pady = 20, side = 'left')


canvas.mainloop()
