# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 08:58:23 2019

@author: chris
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


frame = pd.DataFrame(np.random.randint(0,10,size=(10, 25)),
                     index=['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10'])

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
    # plt.savefig(r'C:\Users\chris\Nextcloud\HSKA\WS1920\HiWi\Projekte\DMM_jupyter\plots\test.png')
    plt.show()
    return frame, frame_mean_mean, frame_mean_median, frame_mean_std

frame, mean_mean, mean_median, mean_std = meanErrorPlot(frame)

print('Ergebnisse:\n{}\n'.format(frame[['mean', 'std_dev']]))
print('Mittelwert über Messreihenmittelwerte: {0:.3f}'.format(mean_mean))
print('Median über Messreihenmittelwerte: {0:.3f}'.format(mean_median))
print('Standardabweichung der Messreihenmittelwerte: {0:.3f}'.format(mean_std))
