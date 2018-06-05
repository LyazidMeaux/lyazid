import numpy as np

def affiche (feuille):
    print ('\n' *10)
    print ('Affichage:')
    print (feuille)

    population= feuille ['Population']
    print (np.log(population))
    surpopulation = population.apply(lambda val: val > 1)
    print (surpopulation)

    # La reindexation ne fonctionne pas vraiment
    villes = feuille['Ville']
    print (type(villes))
    villes.reindex(np.random.permutation(villes.index))
    print (villes)

    feuille.reindex([2, 0, 1])
    print (feuille)


import pandas as pd
import matplotlib.pyplot as plt
import datetime

def dessine ():
    california_housing_dataframe = pd.read_csv("https://storage.googleapis.com/mledu-datasets/california_housing_train.csv", sep=",")
    california_housing_dataframe.describe()
    california_housing_dataframe.hist('housing_median_age')
#
    plt.show()

    df2 = pd.DataFrame([], columns=['dataFor','total'])
    df2['dataFor'] = [datetime.datetime(2013, 9, 11),datetime.datetime(2013, 9, 12),datetime.datetime(2013, 9, 13),datetime.datetime(2013, 9, 14),datetime.datetime(2013, 9, 15),datetime.datetime(2013, 9, 16),datetime.datetime(2013, 9, 17)]
    df2['total'] = [11,15,17,18,19,20,21]
#
### notice date are datetimes objects and not strings
    df2.plot(kind='line')
#
    plt.figure(figsize=(20,10))
    plt.plot(df2.dataFor, df2.total, linewidth=5)
    plt.plot(df2.dataFor, df2.total, '*', markersize=20, color='red')
    plt.xticks(fontsize=20, fontweight='bold',rotation=90)
    plt.yticks(fontsize=20, fontweight='bold')
    plt.xlabel('Dates',fontsize=20, fontweight='bold')
    plt.ylabel('Total Count',fontsize=20, fontweight='bold')
    plt.title('Counts per time',fontsize=20, fontweight='bold')
    plt.tight_layout()
#
    plt.show()
#
#

