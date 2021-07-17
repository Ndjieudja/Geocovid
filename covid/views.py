from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pandas as pd
import folium
from django.contrib.staticfiles.storage import staticfiles_storage
from requests import get
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from .utils import clustering


# Create your views here.
def home(request):
     return redirect('/map')


def logout_(request):
    logout(request)
    return redirect('/connexion')


def login_(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # verify is donne is valide
            user = authenticate(username=username, password=password)

            # if back object is not empty
            if user:
                # login of user
                login(request, user)
                return redirect('/map')

                # if object is empty
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'covid/Login.html', locals())


def create_account(request):

    if request.method == 'POST':
        form = CreateForm(request.POST)
        go = False

        if form.is_valid():
            # define various to create user
            name = request.POST['name']
            password_ = request.POST['password1']
            email = request.POST['email']

            # create user
            new_user = User.objects.create_user(name, email, password_)
            form.instance.user = new_user

            # save form
            form.save()
            go = True
            #return redirect(ma_vue)
            user = authenticate(username=name, password=password_)
            if user:
                login(request, user)
                return redirect('/map')
    else:
        form = CreateForm()

    return render(request, 'covid/user-registration .html', locals())


# filter view if user is not connecte
# @login_required(login_url='/connexion_pour_concours/') to specifie the reidrect url
@ login_required()
def maping(request):

    # opdn and read csv file
    file = staticfiles_storage.path('data/test_cluster.csv')

    data_ = pd.read_csv(file)

    # get my external ip
    ip = get('https://api.ipify.org').text

    # clustering
    # get the utils.fuctionnname ....

    # get location
    locator = Nominatim(user_agent="covid")
    location = locator.geocode('Yaounde')

    location = [location.latitude, location.longitude]

    # create map
    map = folium.Map(location=location, width=1100, height=700, zoom_start=12,
                     title='Clustering of case covid test posititve')

    data_.apply(lambda row: folium.Marker(location=[row['Longitude'], row['Latitude']],
                        icon=folium.Icon(color="orange"),
                                draggable=False).add_to(map), axis=1)

    '''data_.apply(lambda row: folium.CircleMarker(location=(row['Longitude'], row['Latitude']),
                     fill=True, color=row['Color']).add_to(map), axis=1)'''

    d_centre = staticfiles_storage.path('data/safe.csv')
    data_c = pd.read_csv(d_centre)
    #data_c= clustering(d)

    n_element = {n: data_c[data_c['Cluster'] == n][['Longitude', 'Latitude']].values for n in range(10)}
    color = ['red', 'blue', 'cyan', 'green', 'purple', 'dark', 'while', 'pink', 'beige', 'indigo']

    t_index = list()
    for n in range(10):
        if len(n_element[n]) >= 3:
            data_ = list(n_element[n])
            tab = list()
            t_index.append(n)
            for el in data_:
                tab.append([el[0], el[1]])
            user = sorted(tab)
            distance = geodesic(user[0], user[-1]).km

            data_c[data_c['Centroids'] == 1].apply(lambda row: folium.Circle(location=(el[0], el[1]),
                                    radius=distance*1000, color='red', fill=True).add_to(map), axis=1)

            #folium.Polygon(tab, fill=True, color='yellow').add_to(map)

    # insert legend inside map
    legend_html = """<div style="position:fixed; bottom:10px; left:10px; z-index:9999; font-size:14px;">&nbsp;<b>""" + 'Legend' + """</b><br>"""

    # lengend according to reuslt of covid test

    legend_html = legend_html + """&nbsp;&nbsp;""" + 'Test covid' + """<br>"""

    legend_html = legend_html + """&nbsp;<i class="fa fa-map-marker
            fa-1x" style="color:""" + 'red' + """">
            </i>&nbsp;""" + str('Positive case') + """<br>"""

    legend_html = legend_html + """&nbsp;<i class="fa fa-circle
        fa-1x" style="color:""" + 'red' + """">
        </i>&nbsp;""" + str('Cluster allarment') + """<br>"""

    legend_html = legend_html + """</div>"""

    map.get_root().html.add_child(folium.Element(legend_html))

    map = map._repr_html_()

    context = {
        'map': map,
        'user': request.user.username,
    }

    return render(request, 'covid/map.html', context)


