import pandas as pd
import random
from django.contrib.staticfiles.storage import staticfiles_storage


def get_street(fichier):

    streets = list()
    with open(fichier, 'r') as file:
        for el in file:
            for i in range(len(el)):
                if el[i] =='\n':
                    streets.append(el[:i])
    return streets


def hasar(name):
    return random.choice(name)


file = staticfiles_storage.path('data/data.csv')

data_ = pd.read_csv(file)

'''X = data_[["Longitude", 'Latitude']]
table = list()


for i in range(1, 11):
    if len(X)>= 1:
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(X)
        table.append(kmeans.inertia_)

plt.plot(range(1, 11), table)
plt.show()'''



'''data = data_[["Street","Longitude","Latitude", 'Color', 'Result']].reset_index(drop=True)
data.head()



result = ['positive', 'negative']
data['Result'] = 0
data['Result']=data['Result'].apply(lambda x: hasar(result))


color = ['green', 'red']
lst_elements = list(data['Result'].unique())
print(lst_elements)
data["Color"] = data["Result"].apply(lambda x: color[lst_elements.index(x)])






data= data_[['Street', 'Latitude', 'Longitude', 'Result','Color']]
print(data)'''

#data.to_csv('data.csv')











