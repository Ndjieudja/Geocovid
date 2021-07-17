from django.contrib.gis.geoip2 import GeoIP2
import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster import vq
import math
from geopy.distance import geodesic

# fucntions helper

app_name = 'covid'


def get_ip_adress(request):
    x_forward_for = request.META.get("HTTP_X_FORWARD_FOR")

    if x_forward_for:
        ip = x_forward_for.split(",")[0]

    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def get_geoip(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    lat, lon = g.lat_lon(ip)

    return lat, lon


def get_center_coordonate(latA, longA, latB=None, lonB=None):
    coord = (latA, longA)

    if lonB:
        coord = [(latA + latB) / 2, (longA + lonB) / 2]

    return coord


def clustering(data_set):

    X = data_set[['Longitude', 'Latitude']]
    data_ = X.copy()

    kmeans = KMeans(n_clusters=12, n_init=1, init='k-means++')

    # createz column Cluster
    data_["Cluster"] = kmeans.fit_predict(data_)

    closest, distances = vq.vq(kmeans.cluster_centers_,
                               data_.drop("Cluster", axis=1).values)

    data_["Centroids"] = 0
    for i in closest:
        data_['Centroids'].iloc[i] = 1

    # add clustering info to the original data_set
    #data_set[data_set['Result'] == filter][['Cluster', 'Centroids']] = data_[['Cluster', 'Centroids']]

    # create Color_Cluster column
    lst_elements = sorted(list(data_set['Cluster'].unique()))
    lst_colors = ['black', 'cyan', 'purple', 'blue', 'red', 'pink','white', 'beige']

    '''data_set["Color"] = data_set['Result'].apply(lambda x:
                                                  lst_colors[lst_elements.index(x)])

    data_set["Color_Cluster"] = data_set['Cluster'].apply(lambda x:
                                                          lst_colors[lst_elements.index(x)])'''

    safe = pd.DataFrame(data_, columns=('Longitude', 'Latitude','Cluster', 'Centroids'))
    safe.to_csv('safe.pdf')
    return data_


def get_clustering(coord1, coord2):

    R = 6372800  # Earth radius in meters
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2

    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def circle_cluster(data_c):
    n_element = {n: data_c[data_c['Cluster'] == n][['Longitude', 'Latitude', 'Centroids']].values
                 for n in range(10)}
    collor = ['red', 'blue', 'cyan', 'green', 'purple', 'dark', 'while', 'pink', 'beige', 'indigo']

    t_distance = list()
    t_index = list()

    t_distance = list()
    t_index = list()

    for n in range(10):
        if len(n_element[n]) >= 3:
            data_ = list(n_element[n])
            tab = list()
            t_index.append(tab)
            for el in data_:
                tab.append([el[0], el[1]])
            user = sorted(tab)
            distance = geodesic(user[0], user[-1]).km

            t_distance.append(distance)

            # folium.Polygon(tab, fill=True, color='yellow').add_to(map
    return t_distance




