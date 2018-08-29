from scipy.fftpack import fft
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import sys
import tkinter as tk
from tkinter import ttk



"""
file_eeg = open("H:/eegfiles/Z011.txt", "r")
"""
"""
file_eeg = open("C:/Users/djusu/Desktop/eegdata/S011.txt")
data_list = list()
time_list = list()
i = 0
for line in file_eeg:
    data_list.append(abs(int(line)))
    time_list.append(i)
    i = i + 1
file_eeg = open("C:/Users/djusu/Desktop/eegdata/S011.txt", "r")
for line in file_eeg:
    data_list.append(abs(int(line)))
    time_list.append(i)
    i = i + 1
transformed = fft(data_list)
plt.plot(time_list, data_list)
plt.show()
"""
