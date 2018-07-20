from sklearn import svm
import numpy as np
from scipy.fftpack import fft
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
LARGE_FONT = ("Verdana", 12)

seize = 1
normal = 2
file_eeg = open("C:/Users/djusu/Desktop/eegdata/S001.txt", "r")

def find_vector(file_name):
    x = 0
    rms = 0
    data_list = list()
    maximum = 0
    for line in file_name:
        if (abs(maximum) < abs(int(line))):
            maximum = abs(int(line))
        rms += int(line) ** 2
        x += 1
        data_list.append(int(line))
    
    rms = rms / x
    rms = rms ** 0.5
    transformed = fft(data_list)
    ft_maximum = 0
    for y in transformed:
        if (abs(ft_maximum) < abs(y)):
            ft_maximum = abs(y)
                        
    return [int(rms), ft_maximum]
            
matrix = []
i = 1
while (i < 10):
    file_eeg = open("C:/Users/djusu/Desktop/eegdata/S00" + str(i) + ".txt", "r")
    matrix.append(find_vector(file_eeg))
    file_eeg = open("C:/Users/djusu/Desktop/eegdata/Z00" + str(i) + ".txt", "r")
    matrix.append(find_vector(file_eeg))
    i = i + 1

categories = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
eeg_svm = svm.SVC(kernel = "linear", C = 1.0)
eeg_svm.fit(matrix, categories)

class SeizurePredictor(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        
        container.pack(side = "top", fill = "both", expand = "true")
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = { }
        
        for F in (StartPage, PageOne):
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row = 0, column = 0, sticky = "nsew")
        
        self.show_frame(StartPage)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
def predict(ent):
    """
    str_num = ""
    kind = ""
    number = input("Enter a number 1 to 200:     ")
    number = int(number)
    """
    
    number = int(ent.get())
    if (number > 100):
        number = number - 100
        kind = "Z"
    elif (number <= 100):
        kind = "S"
    if (number < 10):
        str_num = "00" + str(number)
    elif (number > 10):
        if (number < 100):
            str_num = "0" + str(number)
        else:
            str_num = str(number)
            

    file_param = open("C:/Users/djusu/Desktop/eegdata/" + kind + str_num + ".txt", "r")
    vector_tested = find_vector(file_param)
    file_param = open("C:/Users/djusu/Desktop/eegdata/" + kind + str_num + ".txt", "r")
    dat = list()
    time = list()
    leng = 0
    for line in file_param:
        if (leng > 0):
            dat.append(abs(int(line)))
            time.append(leng)
        leng = leng + 1
    plt.plot(time, dat)
    plt.show()
    if (eeg_svm.predict([vector_tested]) == seize):
        print("[Abnormal Seizure Activity]")
    else:
        print("[Normal Awake Activity]")
    #controller.show_frame(PageTwo)
        
class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Home Page", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text = "Begin Program", 
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="EEG Classification Program 1.0", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        label = tk.Label(self, text = "Enter a number 1 to 200 to choose a file:", font = LARGE_FONT)
        label.pack(pady = 10, padx = 10)
        
        
        e = tk.Entry(self)
        e.pack()
        
        button1 = tk.Button(self, text = "Choose File and Predict", 
                            command = lambda: predict(e))
        button1.pack()
        
        

"""        
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="EEG Classification Program 1.0 - Graph", font = LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text = "Back to Predicting", 
                            command = lambda: controller.show_frame(PageOne))
        button1.pack()
        
        f = Figure(figsize=(6, 6), dpi=100)
        a = f.add_subplot(111)
        a.plot()
        """
        
app = SeizurePredictor()
app.mainloop()

#testing portion
"""
file_eeg = open("C:/Users/djusu/Desktop/eegdata/" + file_kind + ".txt", "r")
        dat = list()
        time = list()
        leng = 0
        for line in file_eeg:
            dat.append(int(line))
            time.append(i)
            leng = leng + 1
        transform_data = fft(dat)
        plt.plot(time, transform_data)
"""
"""
var = 0
while (var == 0):
    kind = input("Enter Z for a normal test eeg, S for a seizure eeg, or \"stop\" to stop.")
    if (kind != "stop"):
        file_num = input("Enter a number 1 to 99 to choose a file")
        file_kind = kind + file_num
        file_eeg = open("C:/Users/djusu/Desktop/eegdata/" + file_kind + ".txt", "r")
        vector_test = find_vector(file_eeg)
        result = eeg_svm.predict([vector_test])
        if (result == seize):
            print("Seizure")
        else:
            print("Normal")
        
        leng = 0
        for line in file_eeg:
            dat.append(int(line))
            leng = leng + 1
        k = 7
        index = -1
        rms = 0
        ft_max = 0
        while (k < leng):
            a = fft(dat[(k-7):k])
            for x in a:
                if (abs(ft_max) < abs(x)):
                    ft_max = abs(x)
                    rms += x ** 2
            rms = rms / 7
            rms = rms ** 0.5
            vector_new = [rms, ft_max]
            if (eeg_svm.predict([vector_new]) == seize):
                index = k - 7
                print("Seizure indicated at time: T = " + str(index))
                break
            k = k + 7
            rms = 0
            ft_max = 0
        if (index == -1):
            print("Seizure point not found")
    elif (kind == "stop"):
        break
        """
    
"""
maybe test only for seizure point when there's an actual seizure
"""
