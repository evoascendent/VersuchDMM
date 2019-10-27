# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 19:36:45 2019

@author: thch1015
"""

import os
import time
import datetime
import pandas as pd
import serial
from IPython.display import clear_output
from termcolor import colored
import matplotlib.pyplot as plt

port = ''
name = 'VersuchDMM.jpg'

def connectDMM(port):
    connection = serial.Serial(port)
    print('Multimeter connected to {}'.format(port))
    return connection

def readPrimary(connection):
    connection.write(b'R1\r')
    return connection.readline().decode()

def measureRemote(nSwitch, nMeasure):
    connection = connectDMM(port)
    result = pd.DataFrame()
    for switch in range(nSwitch):
        counter = switch + 1
        measureList = []
        clear_output()
        input('Bitte bestätigen Sie Schaltvorgang {} mit ENTER'.format(counter))
        print(colored('Messung läuft! Bitte warten!', 'red'))
        for measure in range(nMeasure):
             measureList.append(readPrimary(connection))
             time.sleep(0.1)
        result = result.append(measureList, ignore_index=True)
    clear_output()
    print('Messreihenaufnahme beendet...')
    return result

def meanErrorPlot(frame):
    frame['mean']=frame.mean(axis=1)
    frame['std_dev']=frame.std(axis=1)
    frame_mean_mean = frame['mean'].mean()
    frame_mean_median = frame['mean'].median()
    frame_mean_std = frame['mean'].std()

    yData= frame['mean']
    e = frame.std_dev

    plt.figure(figsize=(16, 9))
    plt.errorbar(x=frame.index,
                 y=yData,
                 yerr=e,
                 linestyle='None',
                 marker='o',
                 ecolor='y',
                 capsize=10)
    plt.hlines(frame_mean_mean,
               frame.index[0],
               frame.index[-1],
               colors='g',
               label='Mittelwert')
    plt.hlines(frame_mean_median,
               frame.index[0],
               frame.index[-1],
               colors='m',
               label='Median')
    plt.legend(labels=['Mittelwert', 'Median', 'Messwerte(Mittelwert)'])
    cwd = os.getcwd()
    pathName = os.path.join(cwd, name)
    plt.savefig(pathName)
    plt.show()
    return frame, frame_mean_mean, frame_mean_median, frame_mean_std