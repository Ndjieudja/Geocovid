from django.urls import path, re_path
from .views import logout_, login_, create_account, maping, home
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler400, handler403,handler404, handler500

# enter the urls of app there

app_name = 'covid'

urlpatterns = [
    path('', home),
    path("deconnexion", logout_),
    path("connexion", login_),
    path('register', create_account),
    path('map', maping),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf.urls import (
handler400, handler403, handler404, handler500
)

