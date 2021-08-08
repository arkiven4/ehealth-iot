#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""@package coughtk
CoughAnalyzer GUI using tkinter
"""

# Imports system libraries
import sys
import psutil
import tkinter as tk
import subprocess as sp
from tkinter import font

# Import matplotlib libraries
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np

class BtTk():
    """CoughAnalyzer Program with GUI
    """

    btdeviceids = []
    play = None
    DarkTheme = False

    def __init__(self):
        super(BtTk, self).__init__()

        # Main Window
        self.window = tk.Tk()
        self.window.geometry("480x320")
        self.window.title("Tk CoughAnalyzer")

        # Title Label
        self.lbltitle = tk.Label(self.window, text="Cough Analyzer Program")
        self.lbltitle.pack(side=tk.TOP)

        # Button Frame
        self.btnfrm = tk.Frame(self.window)

        # Button Start to Analyze
        self.btnstart = tk.Button(self.btnfrm, text="  Start ")
        self.btnstart.pack(side=tk.LEFT)

        # Button Graph Test
        self.btntest = tk.Button(self.btnfrm, text="  Test  ")
        self.btntest.pack(side=tk.LEFT)

        # Button App Quit
        self.btnquit = tk.Button(self.btnfrm, text="  Quit  ", command=self.appquit)
        self.btnquit.pack(side=tk.LEFT)

        # Pack Button Frame
        self.btnfrm.pack(side=tk.TOP)

        # Graph Frame
        self.graphfrm = tk.Frame() 

        # Example Figure Plot
        self.fig = Figure(figsize=(5, 4), dpi=100)
        t = np.arange(0, 3, .01)
        self.fig.add_subplot(111).plot(t, 2 * np.sin(20 * np.pi * t))

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.graphfrm)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.LEFT)

        self.canvas.mpl_connect("key_press_event", self.on_key_press)

        # Pack Graph Frame
        # Must packed the last
        self.graphfrm.pack(side=tk.BOTTOM,expand=True)

        # Button Font
        btnfont = font.Font(self.btnfrm, family="Liberation Mono", size=10)
        self.lbltitle.config(font=btnfont)
        self.btnstart.config(font=btnfont)
        self.btntest.config(font=btnfont)
        self.btnquit.config(font=btnfont)

        # Dark Theme Config
        if self.DarkTheme:
            self.window.config(bg="black")
            self.lbltitle.config(bg='black', fg='white')
            self.btnstart.config(bg='black', fg='white')
            self.btntest.config(bg='black', fg='white')
            self.btnquit.config(bg='black', fg='white')
            self.btnfrm.config(bg='black')

        # Main Loop
        self.window.mainloop()

    def isrunning(self, process):
        """ Check if a process name running"""

        for proc in psutil.process_iter():
            try:
                if process.lower() in proc.name().lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def on_key_press(self,event):
        """ Test Graph Key Event"""

        key_press_handler(event, self.canvas)

    def appquit(self):
        """ Quit Program"""

        self.window.destroy()


if __name__ == "__main__":
    bttk = BtTk()
