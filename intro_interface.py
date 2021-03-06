'''
Created by Victor Delvigne
ISIA Lab, Faculty of Engineering University of Mons, Mons (Belgium)
IMT Nord Europe, Villeneuve d'Ascq (France)
victor.delvigne@umons.ac.be
Source: TBD
Copyright (C) 2021 - UMons/IMT Nord Europe
This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
'''


import os
import glob
import time
import tkinter 
import numpy as np

from playsound import playsound


# Main Window
m = tkinter.Tk()
m.title("random page")
m.geometry('720x420')
tkinter.Label(m, text="Experiment Begin", fg="red", font=('Helvetica 28')).pack(pady=150)
m.after(15000, lambda:m.destroy())
m.mainloop()


# Run Videos
vid_id = 1
#vid_path = '/home/vdelv/Downloads/DREAMER_VID/*.m4v'
vid_path = 'example_vids/*.mp4'
list_vid = glob.glob(vid_path)
np.random.shuffle(list_vid)
for vid in list_vid:
    m = tkinter.Tk()
    m.title("random page")
    m.geometry('720x420')
    tkinter.Label(m, text="Video "+str(vid_id), fg="blue", font=('Helvetica 28')).pack(pady=150)
    m.after(5000, lambda:m.destroy())
    m.mainloop()
    playsound(vid, block=False)
    vid_id += 1