import pandas
import statistics
import matplotlib.pyplot as plt

# Jaká je nejčastější hodnota, která na dvou kostkách padne?
# Je větší šance, že padne hodnota 12 než že padne hodnota 2? ano = 4x


kostky = pandas.read_csv('kostky.txt', header=None)
print(kostky.head())

kostky.plot(kind="hist")
plt.show()


