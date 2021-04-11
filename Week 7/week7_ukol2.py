# V souboru callcentrum.txt najdete několik tisíc záznamů pro call centrum,
# které udávají časy mezi jednotlivými příchozími hovory v minutách a vteřinách.
# Načtěte tato data do série v Pythonu. Časy převeďte na vteřiny a zobrazte jejich histogram a boxplot.
# Co lze z těchto dvou grafů vyčíst?
import pandas
import datetime
import matplotlib.pyplot as plt


callcentrum = pandas.read_csv('callcentrum.txt', header=None)
callcentrum=callcentrum[0].str.split(':',expand=True).astype(int)

callcentrum = callcentrum.rename(columns={0: 'minuty', 1: 'vteriny'})
print(callcentrum.head())

callcentrum['celkovy_cas'] = (callcentrum['minuty'] * 60) + callcentrum['vteriny']
callcentrum['celkovy_cas'].plot(kind='hist') #plot only for one column with the total time
plt.show()