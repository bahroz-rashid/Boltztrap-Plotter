import os
import sys
import pylab as plt
from Tkinter import *
from tkMessageBox import *
class plotter():
    @staticmethod
    def plotting(r,u,t,path_dir):
        w = []
        x = []
        y = []
        try:
            with open(os.path.join(path_dir,t+'K.txt'),'r') as file:
                data = file.readlines()
                for line in data:
                    l = line.split()
                    w.append(l)
        except IOError:
            showerror('Warning!!!', 'Enter the temperature first')
            return
        word = w[1:]
        x = [word[i][u] for i in range(len(word))]
        # y = [str(1000000*float(word[i][4])) for i in range(len(word))]
        # plt.plot(x, y, linewidth=2)
        # # plt.semilogx(x, y, linewidth = 2)
        # plt.xlim(10E17, 10E19)
        # plt.ylim(0,500)
        if r == 4:
            y = [str(1000000*float(word[i][r])) for i in range(len(word))]
        else:
            y = [word[i][r] for i in range(len(word))]
        plt.figure(1)
        if r == 2:
            plt.semilogy(x, y, linewidth=2)
        else:
            plt.plot(x, y, linewidth=2)
        plt.title('Seebeck Coefficient vs Chemical Potential')
        plt.ylabel(r'$S \;(\mu V/K$)', fontsize=20)
        if u == 10:
            plt.xlabel(r'$\mu - E_{f}$ (eV)', fontsize=20)
            plt.xlim(-1, 1)
        else:
            plt.xlabel(r'$\mu$ (Ry)', fontsize=20)
            plt.xlim(0.25, 0.5)
        plt.show()
